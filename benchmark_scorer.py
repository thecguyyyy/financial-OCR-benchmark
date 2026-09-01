#!/usr/bin/env python
"""Score financial-document OCR and Markdown reconstruction results.

The scorer compares a prediction Markdown file with a ground-truth Markdown
file. It evaluates tables, heading layout, text, and optional informative
chart transcriptions. Formulae remain part of the text module. A shared, model-neutral LaTeX
normalizer removes presentation-only syntax before edit-distance comparison.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

try:
    from Levenshtein import distance as _fast_levenshtein_distance  # type: ignore
except ImportError:  # Optional acceleration; the scorer keeps a pure-Python fallback.
    _fast_levenshtein_distance = None


WEIGHTS = {"table": 0.40, "title_layout": 0.20, "text": 0.40}
TITLE_LAYOUT_WEIGHTS = {
    "heading_f1": 0.80,
    "level_accuracy": 0.10,
    "order": 0.10,
}
_OPENCC_T2S: Any = None
_OPENCC_READY = False


@dataclass
class TableItem:
    """A table extracted from Markdown."""

    index: int
    kind: str
    start: int
    end: int
    raw: str
    matrix: List[List[str]]
    span_pages: Optional[Tuple[int, int]] = None
    accept_chart_representation: bool = False
    from_chart_block: bool = False
    chart_payload_index: Optional[int] = None
    chart_table_index: Optional[int] = None


@dataclass
class HeadingItem:
    """A Markdown heading with raw level and text."""

    index: int
    level: int
    text: str


@dataclass
class PredCleanupResult:
    """Prediction-only cleanup details."""

    markdown: str
    removed_line_count: int
    removed_line_examples: List[str]


@dataclass
class ScoringConfig:
    """Runtime scoring normalization and weighting options."""

    remove_pred_header_footer: bool = True
    normalize_images: bool = True
    score_charts: bool = True
    normalize_zh: str = "t2s"
    normalize_footnotes: bool = True
    normalize_punctuation: bool = True
    normalize_formulas: bool = True
    table_structure_weight: float = 0.60
    table_content_weight: float = 0.40
    table_aggregation: str = "footprint"
    module_weighting: str = "content"
    title_layout_weight: float = 0.20


DEFAULT_CONFIG = ScoringConfig()
CURRENT_CONFIG = ScoringConfig()


def clamp_score(value: float) -> float:
    """Clamp a score to the 0-100 range."""

    return max(0.0, min(100.0, value))


def round_float(value: float, digits: int = 4) -> float:
    """Round floats consistently for JSON and Markdown reports."""

    return round(float(value), digits)


def read_markdown(path: str | Path) -> str:
    """Read a Markdown file with UTF-8 first and a permissive fallback."""

    p = Path(path)
    try:
        return p.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="replace")


def normalize_text(text: str) -> str:
    """Normalize text for edit-distance comparison."""

    text = html.unescape(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[*_`~]+", "", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    cjk_or_cjk_punct = r"\u3400-\u9fff\u3001-\u303f\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65"
    text = re.sub(fr"([{cjk_or_cjk_punct}])\s+([{cjk_or_cjk_punct}])", r"\1\2", text)
    return text.strip()


class SimpleTableHTMLParser(HTMLParser):
    """Extract raw table rows and cells from an HTML table."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.rows: List[List[Dict[str, Any]]] = []
        self._in_tr = False
        self._in_cell = False
        self._current_row: List[Dict[str, Any]] = []
        self._cell_text: List[str] = []
        self._cell_rowspan = 1
        self._cell_colspan = 1

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        tag = tag.lower()
        attrs_dict = {k.lower(): v for k, v in attrs}
        if tag == "tr":
            self._in_tr = True
            self._current_row = []
        elif tag in {"td", "th"} and self._in_tr:
            self._in_cell = True
            self._cell_text = []
            self._cell_rowspan = _safe_int(attrs_dict.get("rowspan"), 1)
            self._cell_colspan = _safe_int(attrs_dict.get("colspan"), 1)
        elif tag == "br" and self._in_cell:
            self._cell_text.append(" ")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"td", "th"} and self._in_cell:
            self._current_row.append(
                {
                    "text": normalize_text("".join(self._cell_text)),
                    "rowspan": max(1, self._cell_rowspan),
                    "colspan": max(1, self._cell_colspan),
                }
            )
            self._in_cell = False
            self._cell_text = []
        elif tag == "tr" and self._in_tr:
            self.rows.append(self._current_row)
            self._current_row = []
            self._in_tr = False

    def handle_data(self, data: str) -> None:
        if self._in_cell:
            self._cell_text.append(data)


def _safe_int(value: Optional[str], default: int) -> int:
    """Parse positive integer attributes such as rowspan and colspan."""

    if value is None:
        return default
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return default
    return parsed if parsed > 0 else default


def _expand_html_spans(rows: List[List[Dict[str, Any]]]) -> List[List[str]]:
    """Expand rowspan and colspan by duplicating covered cell text."""

    grid: List[List[str]] = []
    rowspans: Dict[int, Tuple[int, str]] = {}

    for raw_row in rows:
        row: List[str] = []
        col = 0

        def fill_pending() -> None:
            nonlocal col
            while col in rowspans:
                remaining, text = rowspans[col]
                row.append(text)
                if remaining <= 1:
                    del rowspans[col]
                else:
                    rowspans[col] = (remaining - 1, text)
                col += 1

        fill_pending()
        for cell in raw_row:
            fill_pending()
            text = cell["text"]
            rowspan = int(cell["rowspan"])
            colspan = int(cell["colspan"])
            for offset in range(colspan):
                row.append(text)
                if rowspan > 1:
                    rowspans[col + offset] = (rowspan - 1, text)
            col += colspan
        fill_pending()
        if row:
            grid.append(row)

    while rowspans:
        row = []
        col = 0
        last_pending_column = max(rowspans)
        while col <= last_pending_column:
            if col in rowspans:
                remaining, text = rowspans[col]
                row.append(text)
                if remaining <= 1:
                    del rowspans[col]
                else:
                    rowspans[col] = (remaining - 1, text)
            else:
                row.append("")
            col += 1
        grid.append(row)

    return grid


def split_pipe_row(line: str) -> List[str]:
    """Split a Markdown pipe-table row into normalized cells."""

    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    parts = re.split(r"(?<!\\)\|", line)
    return [normalize_text(part.replace(r"\|", "|")) for part in parts]


def is_pipe_row(line: str) -> bool:
    """Return True if a line looks like a Markdown table row."""

    stripped = line.strip()
    return "|" in stripped and not stripped.startswith("```")


def is_pipe_separator(line: str) -> bool:
    """Return True if a line looks like a Markdown table separator row."""

    if not is_pipe_row(line):
        return False
    cells = split_pipe_row(line)
    if not cells:
        return False
    valid = 0
    for cell in cells:
        compact = cell.replace(" ", "")
        if re.fullmatch(r":?-{3,}:?", compact):
            valid += 1
    return valid == len(cells)


def parse_markdown_pipe_table(table_md: str) -> List[List[str]]:
    """Parse a Markdown pipe table into a 2D cell matrix."""

    rows: List[List[str]] = []
    for line in table_md.splitlines():
        if not is_pipe_row(line) or is_pipe_separator(line):
            continue
        rows.append(split_pipe_row(line))
    return rows


def parse_html_table(table_html: str) -> List[List[str]]:
    """Parse an HTML table into a 2D cell matrix."""

    parser = SimpleTableHTMLParser()
    parser.feed(table_html)
    parser.close()
    return _expand_html_spans(parser.rows)


def parse_table_to_matrix(table_md_or_html: str) -> List[List[str]]:
    """Normalize an HTML or Markdown table to a 2D cell matrix."""

    if re.search(r"<table\b", table_md_or_html, flags=re.I):
        return parse_html_table(table_md_or_html)
    return parse_markdown_pipe_table(table_md_or_html)


def find_cross_page_span_before(md: str, table_start: int) -> Optional[Tuple[int, int]]:
    """Find a `table spans PDF pages x-y` comment immediately before a table."""

    window_start = max(0, table_start - 500)
    prefix = md[window_start:table_start]
    matches = list(
        re.finditer(
            r"<!--\s*table\s+spans\s+PDF\s+pages\s+(\d+)\s*-\s*(\d+)\s*-->",
            prefix,
            flags=re.I,
        )
    )
    if not matches:
        return None
    last = matches[-1]
    if prefix[last.end() :].strip():
        return None
    start_page = int(last.group(1))
    end_page = int(last.group(2))
    if end_page <= start_page:
        return None
    return start_page, end_page


def _line_offsets(md: str) -> List[Tuple[int, int, str]]:
    """Return start/end offsets for each line."""

    offsets = []
    cursor = 0
    for line in md.splitlines(keepends=True):
        start = cursor
        cursor += len(line)
        offsets.append((start, cursor, line))
    if not offsets and md:
        offsets.append((0, len(md), md))
    return offsets


def _overlaps_any(start: int, end: int, spans: Sequence[Tuple[int, int]]) -> bool:
    """Return True if a span overlaps any existing span."""

    return any(start < span_end and end > span_start for span_start, span_end in spans)


def _accepts_chart_representation(md: str, table_start: int) -> bool:
    """Return whether a Gold marker allows this table to be a chart payload."""

    prefix = md[max(0, table_start - 240) : table_start]
    return bool(
        re.search(
            r"<!--\s*gold-object\s*:\s*chart-table\s*;\s*accepts\s*:\s*table\s*,\s*chart\s*-->\s*$",
            prefix,
            flags=re.I,
        )
    )


def remove_chart_table_markers(md: str) -> str:
    """Remove Gold-only chart-table policy comments from semantic scoring."""

    return re.sub(
        r"<!--\s*gold-object\s*:\s*chart-table\s*;\s*accepts\s*:\s*table\s*,\s*chart\s*-->",
        "",
        md,
        flags=re.I,
    )


def extract_tables(md: str) -> Tuple[List[TableItem], List[Tuple[int, int]]]:
    """Extract HTML and Markdown pipe tables and return their spans."""

    tables: List[TableItem] = []
    spans: List[Tuple[int, int]] = []

    for match in re.finditer(r"<table\b.*?</table\s*>", md, flags=re.I | re.S):
        raw = match.group(0)
        spans.append((match.start(), match.end()))
        tables.append(
            TableItem(
                index=-1,
                kind="html",
                start=match.start(),
                end=match.end(),
                raw=raw,
                matrix=parse_table_to_matrix(raw),
                span_pages=find_cross_page_span_before(md, match.start()),
                accept_chart_representation=_accepts_chart_representation(md, match.start()),
            )
        )

    line_info = _line_offsets(md)
    i = 0
    while i + 1 < len(line_info):
        start_i, end_i, line = line_info[i]
        start_next, end_next, next_line = line_info[i + 1]
        if _overlaps_any(start_i, end_next, spans):
            i += 1
            continue
        if is_pipe_row(line) and is_pipe_separator(next_line):
            j = i + 2
            table_end = end_next
            while j < len(line_info):
                row_start, row_end, row_line = line_info[j]
                if _overlaps_any(row_start, row_end, spans) or not is_pipe_row(row_line):
                    break
                table_end = row_end
                j += 1
            raw = md[start_i:table_end]
            spans.append((start_i, table_end))
            tables.append(
                TableItem(
                    index=-1,
                    kind="pipe",
                    start=start_i,
                    end=table_end,
                    raw=raw,
                    matrix=parse_table_to_matrix(raw),
                    span_pages=find_cross_page_span_before(md, start_i),
                    accept_chart_representation=_accepts_chart_representation(md, start_i),
                )
            )
            i = j
        else:
            i += 1

    tables.sort(key=lambda item: item.start)
    spans = sorted(spans)
    for idx, table in enumerate(tables):
        table.index = idx
    return tables, spans


def remove_tables(md: str, spans: Sequence[Tuple[int, int]]) -> str:
    """Remove table spans from Markdown while preserving surrounding text."""

    if not spans:
        return md
    chunks: List[str] = []
    cursor = 0
    for start, end in sorted(spans):
        if start < cursor:
            continue
        chunks.append(md[cursor:start])
        chunks.append("\n")
        cursor = end
    chunks.append(md[cursor:])
    return "".join(chunks)


def extract_heading_items(md: str) -> List[HeadingItem]:
    """Extract Markdown headings as level/text items."""

    items: List[HeadingItem] = []
    in_fence = False
    for line in md.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^ {0,3}(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if match:
            items.append(
                HeadingItem(
                    index=len(items),
                    level=len(match.group(1)),
                    text=match.group(2).strip(),
                )
            )
    return items


def extract_heading_levels(md: str) -> List[int]:
    """Extract Markdown heading levels as raw # counts."""

    return [item.level for item in extract_heading_items(md)]


def compress_heading_levels(levels: Sequence[int]) -> List[int]:
    """Map observed heading levels to compact relative levels."""

    mapping = {level: idx + 1 for idx, level in enumerate(sorted(set(levels)))}
    return [mapping[level] for level in levels]


def _align_level_sequences(gt_levels: Sequence[int], pred_levels: Sequence[int]) -> Tuple[float, List[Dict[str, Any]]]:
    """Align two heading-level sequences with insertion/deletion penalties."""

    n, m = len(gt_levels), len(pred_levels)
    if n == 0 and m == 0:
        return 0.0, []
    max_level = max(list(gt_levels) + list(pred_levels) + [1])
    inf = 10**9
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    back: List[List[Optional[Tuple[int, int, str, float]]]] = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0

    for i in range(n + 1):
        for j in range(m + 1):
            current = dp[i][j]
            if current >= inf:
                continue
            if i < n and current + 1.0 < dp[i + 1][j]:
                dp[i + 1][j] = current + 1.0
                back[i + 1][j] = (i, j, "missing", 1.0)
            if j < m and current + 1.0 < dp[i][j + 1]:
                dp[i][j + 1] = current + 1.0
                back[i][j + 1] = (i, j, "extra", 1.0)
            if i < n and j < m:
                cost = abs(gt_levels[i] - pred_levels[j]) / max_level
                if current + cost < dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = current + cost
                    back[i + 1][j + 1] = (i, j, "match", cost)

    ops: List[Dict[str, Any]] = []
    i, j = n, m
    while i > 0 or j > 0:
        prev = back[i][j]
        if prev is None:
            break
        pi, pj, op, cost = prev
        item: Dict[str, Any] = {"op": op, "cost": cost}
        if op == "match":
            item.update(
                {
                    "gt_index": pi,
                    "pred_index": pj,
                    "gt_level": gt_levels[pi],
                    "pred_level": pred_levels[pj],
                }
            )
        elif op == "missing":
            item.update({"gt_index": pi, "gt_level": gt_levels[pi]})
        else:
            item.update({"pred_index": pj, "pred_level": pred_levels[pj]})
        ops.append(item)
        i, j = pi, pj
    ops.reverse()
    return dp[n][m], ops


def _heading_text_similarity(a: str, b: str) -> float:
    """Return normalized heading text similarity for alignment only."""

    a_norm = normalize_text(a)
    b_norm = normalize_text(b)
    if not a_norm and not b_norm:
        return 1.0
    if not a_norm or not b_norm:
        return 0.0
    return max(0.0, min(1.0, 1.0 - normalized_edit_distance(a_norm, b_norm)))


def _align_heading_items(
    gt_items: Sequence[HeadingItem],
    pred_items: Sequence[HeadingItem],
    gt_relative: Sequence[int],
    pred_relative: Sequence[int],
) -> Tuple[float, List[Dict[str, Any]]]:
    """Align headings by text anchors while preserving document order."""

    n, m = len(gt_items), len(pred_items)
    if n == 0 and m == 0:
        return 0.0, []
    inf = 10**9
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    back: List[List[Optional[Tuple[int, int, str, float]]]] = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0.0

    for i in range(n + 1):
        for j in range(m + 1):
            current = dp[i][j]
            if current >= inf:
                continue
            if i < n and current + 1.0 < dp[i + 1][j]:
                dp[i + 1][j] = current + 1.0
                back[i + 1][j] = (i, j, "missing", 1.0)
            if j < m and current + 1.0 < dp[i][j + 1]:
                dp[i][j + 1] = current + 1.0
                back[i][j + 1] = (i, j, "extra", 1.0)
            if i < n and j < m:
                similarity = _heading_text_similarity(gt_items[i].text, pred_items[j].text)
                match_cost = 1.0 - similarity
                if similarity < 0.20:
                    match_cost = 1.10
                if current + match_cost < dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = current + match_cost
                    back[i + 1][j + 1] = (i, j, "match", match_cost)

    ops: List[Dict[str, Any]] = []
    i, j = n, m
    while i > 0 or j > 0:
        prev = back[i][j]
        if prev is None:
            break
        pi, pj, op, cost = prev
        item: Dict[str, Any] = {"op": op, "cost": cost}
        if op == "match":
            similarity = _heading_text_similarity(gt_items[pi].text, pred_items[pj].text)
            item.update(
                {
                    "gt_index": pi,
                    "pred_index": pj,
                    "gt_level": gt_relative[pi],
                    "pred_level": pred_relative[pj],
                    "text_similarity": round_float(similarity),
                    "gt_text_preview": gt_items[pi].text[:80],
                    "pred_text_preview": pred_items[pj].text[:80],
                }
            )
        elif op == "missing":
            item.update(
                {
                    "gt_index": pi,
                    "gt_level": gt_relative[pi],
                    "gt_text_preview": gt_items[pi].text[:80],
                }
            )
        else:
            item.update(
                {
                    "pred_index": pj,
                    "pred_level": pred_relative[pj],
                    "pred_text_preview": pred_items[pj].text[:80],
                }
            )
        ops.append(item)
        i, j = pi, pj
    ops.reverse()
    return dp[n][m], ops


def score_title_layout(
    gt_levels: Sequence[int],
    pred_levels: Sequence[int],
    gt_headings: Optional[Sequence[HeadingItem]] = None,
    pred_headings: Optional[Sequence[HeadingItem]] = None,
) -> Dict[str, Any]:
    """Score title layout using anchor-based alignment and relative heading levels."""

    if gt_headings is None:
        gt_headings = [HeadingItem(index=i, level=level, text="") for i, level in enumerate(gt_levels)]
    if pred_headings is None:
        pred_headings = [HeadingItem(index=i, level=level, text="") for i, level in enumerate(pred_levels)]

    gt_relative = compress_heading_levels(gt_levels)
    pred_relative = compress_heading_levels(pred_levels)
    cost, ops = _align_heading_items(gt_headings, pred_headings, gt_relative, pred_relative)

    matches = [op for op in ops if op["op"] == "match"]
    missing = [op for op in ops if op["op"] == "missing"]
    extra = [op for op in ops if op["op"] == "extra"]
    mismatches = [
        op
        for op in matches
        if op.get("gt_level") != op.get("pred_level")
    ]

    matched_count = len(matches)
    if not gt_relative and not pred_relative:
        heading_f1 = 100.0
        level_accuracy = 100.0
        order_score = 100.0
    else:
        precision = matched_count / max(len(pred_relative), 1)
        recall = matched_count / max(len(gt_relative), 1)
        heading_f1 = 0.0 if precision + recall == 0 else 2.0 * precision * recall / (precision + recall) * 100.0
        max_level = max(list(gt_relative) + list(pred_relative) + [1])
        level_sims = [
            1.0 - abs(op["gt_level"] - op["pred_level"]) / max(max_level - 1, 1)
            for op in matches
        ]
        level_accuracy = sum(level_sims) / len(level_sims) * 100.0 if level_sims else 0.0
        order_score = matched_count / max(len(gt_relative), len(pred_relative), 1) * 100.0

    score = clamp_score(
        heading_f1 * TITLE_LAYOUT_WEIGHTS["heading_f1"]
        + level_accuracy * TITLE_LAYOUT_WEIGHTS["level_accuracy"]
        + order_score * TITLE_LAYOUT_WEIGHTS["order"]
    )

    issues: List[str] = []
    if mismatches:
        issues.append(f"{len(mismatches)} aligned headings have different relative levels.")
    if missing:
        issues.append(f"{len(missing)} GT headings are missing.")
    if extra:
        issues.append(f"{len(extra)} predicted headings are extra.")
    if not issues:
        issues.append("No heading layout penalty.")

    return {
        "title_scoring_method": "anchor_heading_f1_level_accuracy_order",
        "title_layout_weights": dict(TITLE_LAYOUT_WEIGHTS),
        "gt_raw_heading_levels": list(gt_levels),
        "pred_raw_heading_levels": list(pred_levels),
        "gt_relative_heading_levels": gt_relative,
        "pred_relative_heading_levels": pred_relative,
        "title_layout_score": round_float(score),
        "heading_f1_score": round_float(heading_f1),
        "level_accuracy_score": round_float(level_accuracy),
        "order_score": round_float(order_score),
        "alignment_cost": round_float(cost),
        "missing_heading_count": len(missing),
        "extra_heading_count": len(extra),
        "level_mismatch_count": len(mismatches),
        "issues": issues,
        "alignment": ops[:100],
    }


def strip_heading_markers_keep_text(md: str) -> str:
    """Remove Markdown heading markers while preserving heading text."""

    lines = []
    for line in md.splitlines():
        match = re.match(r"^( {0,3})#{1,6}\s+(.*?)\s*#*\s*$", line)
        if match:
            lines.append(match.group(2).strip())
        else:
            lines.append(line)
    return "\n".join(lines)


def levenshtein_distance(a: str, b: str) -> int:
    """Compute exact Levenshtein distance, with an optional native fast path."""

    if a == b:
        return 0
    if _fast_levenshtein_distance is not None:
        return int(_fast_levenshtein_distance(a, b))
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)

    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        current = [i]
        for j, cb in enumerate(b, start=1):
            insert_cost = current[j - 1] + 1
            delete_cost = previous[j] + 1
            replace_cost = previous[j - 1] + (0 if ca == cb else 1)
            current.append(min(insert_cost, delete_cost, replace_cost))
        previous = current
    return previous[-1]


def normalized_edit_distance(a: str, b: str) -> float:
    """Return levenshtein_distance(a, b) / max(len(a), len(b), 1)."""

    a_norm = normalize_text(a)
    b_norm = normalize_text(b)
    denom = max(len(a_norm), len(b_norm), 1)
    return levenshtein_distance(a_norm, b_norm) / denom


def normalize_chinese_variants(text: str) -> str:
    """Normalize Traditional/Simplified Chinese variants when OpenCC is available."""

    if CURRENT_CONFIG.normalize_zh == "none":
        return text
    global _OPENCC_T2S, _OPENCC_READY
    if not _OPENCC_READY:
        try:
            from opencc import OpenCC  # type: ignore

            _OPENCC_T2S = OpenCC("t2s")
        except Exception:
            _OPENCC_T2S = None
        _OPENCC_READY = True
    if _OPENCC_T2S is None:
        return text
    try:
        return _OPENCC_T2S.convert(text)
    except Exception:
        return text


def normalize_footnote_markers(text: str) -> str:
    """Remove common inline footnote/superscript markers from body text."""

    if not CURRENT_CONFIG.normalize_footnotes:
        return text
    text = re.sub(
        r"<sup\b[^>]*>\s*[\[\(（]?\s*[0-9A-Za-z０-９一二三四五六七八九十]+\s*[\]\)）]?\s*</sup>",
        "",
        text,
        flags=re.I,
    )
    text = re.sub(r"\$\s*\^\s*\{\s*[0-9A-Za-z０-９一二三四五六七八九十]+\s*\}\s*\$", "", text)
    text = re.sub(r"\^\{\s*[0-9A-Za-z０-９一二三四五六七八九十]+\s*\}", "", text)
    text = re.sub(r"(?i)\b(SSP\d+-\d+\.\d)[0-9]\b", r"\1", text)
    text = re.sub(r"\[\s*(?:注)?[0-9０-９]{1,3}\s*\]", "", text)
    return text


def normalize_punctuation_variants(text: str) -> str:
    """Normalize low-value punctuation variants for body comparison."""

    if not CURRENT_CONFIG.normalize_punctuation:
        return text
    translation = str.maketrans(
        {
            "\u201c": '"',
            "\u201d": '"',
            "\u2018": "'",
            "\u2019": "'",
            "\u300c": '"',
            "\u300d": '"',
            "\u300e": '"',
            "\u300f": '"',
            "\uff1a": ":",
            "\uff1b": ";",
            "\uff0c": ",",
            "\u3001": ",",
            "\uff08": "(",
            "\uff09": ")",
            "\u3014": "(",
            "\u3015": ")",
            "\u3010": "[",
            "\u3011": "]",
            "\u2014": "-",
            "\u2013": "-",
            "\u2212": "-",
            "\uff0d": "-",
        }
    )
    text = text.translate(translation)
    text = re.sub(r"[-]{2,}", "-", text)
    text = re.sub(r"(?<=[\u3400-\u9fff]),(?=[\u3400-\u9fff])", "", text)
    return text


_FORMULA_WRAPPER_COMMANDS = (
    "mathrm",
    "mathbf",
    "mathit",
    "mathsf",
    "mathtt",
    "mathcal",
    "mathbb",
    "text",
    "textrm",
    "textit",
    "textbf",
    "operatorname",
    "boldsymbol",
    "bm",
    "rm",
    "bf",
    "it",
    "cal",
)

_FORMULA_COMMAND_MAP = {
    "frac": "FRAC",
    "dfrac": "FRAC",
    "tfrac": "FRAC",
    "sqrt": "SQRT",
    "sum": "SUM",
    "prod": "PROD",
    "int": "INT",
    "lim": "LIM",
    "log": "LOG",
    "ln": "LN",
    "exp": "EXP",
    "sin": "SIN",
    "cos": "COS",
    "tan": "TAN",
    "min": "MIN",
    "max": "MAX",
    "Delta": "DELTA",
    "delta": "delta",
    "alpha": "alpha",
    "beta": "beta",
    "gamma": "gamma",
    "lambda": "lambda",
    "mu": "mu",
    "sigma": "sigma",
    "theta": "theta",
    "pi": "pi",
    "rho": "rho",
    "xi": "xi",
    "omega": "omega",
    "infty": "INF",
    "approx": "APPROX",
    "sim": "SIM",
    "simeq": "APPROX",
    "equiv": "EQUIV",
    "neq": "NEQ",
    "ne": "NEQ",
    "le": "LE",
    "leq": "LE",
    "ge": "GE",
    "geq": "GE",
    "times": "MUL",
    "cdot": "MUL",
    "div": "DIV",
    "pm": "PLUSMINUS",
    "mp": "MINUSPLUS",
    "to": "TO",
    "rightarrow": "TO",
    "leftarrow": "FROM",
}


def _unwrap_formula_style_commands(formula: str) -> str:
    """Remove presentation-only wrappers while preserving their arguments."""

    wrappers = "|".join(_FORMULA_WRAPPER_COMMANDS)
    pattern = re.compile(rf"\\(?:{wrappers})\s*\{{([^{{}}]*)\}}")
    previous = None
    while previous != formula:
        previous = formula
        formula = pattern.sub(r"\1", formula)
    return formula


def _canonicalize_formula_payload(formula: str) -> str:
    """Return a compact semantic token string for one LaTeX formula.

    This intentionally preserves variables, numbers, grouping, subscripts,
    superscripts and operators.  Unknown commands also survive as uppercase
    tokens, so OCR hallucinations such as ``\\sharp`` are still penalized.
    """

    formula = unicodedata.normalize("NFKC", html.unescape(formula))
    formula = re.sub(r"(?<!\\)%.*?$", "", formula, flags=re.M)
    formula = re.sub(
        r"\\begin\s*\{(?:aligned\*?|align\*?|gathered|gather\*?|split|cases|matrix|pmatrix|bmatrix|vmatrix|Vmatrix)\}",
        "",
        formula,
        flags=re.I,
    )
    formula = re.sub(
        r"\\begin\s*\{array\}\s*\{[^{}]*\}",
        "",
        formula,
        flags=re.I,
    )
    formula = re.sub(r"\\end\s*\{[^{}]+\}", "", formula, flags=re.I)
    formula = _unwrap_formula_style_commands(formula)

    # Layout-only commands and TeX spacing have no mathematical meaning.
    formula = re.sub(
        r"\\(?:left|right|displaystyle|textstyle|scriptstyle|scriptscriptstyle|limits|nolimits|phantom|hphantom|vphantom)\b",
        "",
        formula,
    )
    formula = re.sub(r"\\(?:quad|qquad|enspace|thinspace|medspace|thickspace)\b", "", formula)
    formula = re.sub(r"\\[!,:; ]", "", formula)
    formula = formula.replace("\\%", "%").replace("\\&", "&")
    formula = formula.replace("\\{", "{").replace("\\}", "}")
    formula = formula.replace("\\\\", "")
    formula = formula.replace("&", "")

    unicode_ops = str.maketrans(
        {
            "×": "MUL",
            "·": "MUL",
            "÷": "DIV",
            "≈": "APPROX",
            "≃": "APPROX",
            "≠": "NEQ",
            "≤": "LE",
            "≥": "GE",
            "∞": "INF",
            "−": "-",
            "–": "-",
        }
    )
    formula = formula.translate(unicode_ops)

    def replace_command(match: re.Match[str]) -> str:
        command = match.group(1)
        return _FORMULA_COMMAND_MAP.get(command, command.upper())

    formula = re.sub(r"\\([A-Za-z]+)", replace_command, formula)
    # Preserve scripts explicitly even though generic Markdown normalization
    # later removes underscores.
    formula = re.sub(r"_\s*\{([^{}]*)\}", r"SUB(\1)", formula)
    formula = re.sub(r"\^\s*\{([^{}]*)\}", r"SUP(\1)", formula)
    formula = re.sub(r"_\s*([A-Za-z0-9]+)", r"SUB(\1)", formula)
    formula = re.sub(r"\^\s*([A-Za-z0-9]+)", r"SUP(\1)", formula)
    formula = formula.replace("{", "(").replace("}", ")")
    formula = re.sub(r"\s+", "", formula)
    return formula.strip()


def normalize_formula_markup(text: str) -> str:
    """Canonicalize Markdown/LaTeX math spans using one shared rule set."""

    if not CURRENT_CONFIG.normalize_formulas:
        return text

    marker_prefix = "⟦FORMULA:"

    def replace_formula(match: re.Match[str]) -> str:
        payload = next(group for group in match.groups() if group is not None)
        canonical = _canonicalize_formula_payload(payload)
        # A parser may wrap an ordinary percentage, number, short variable or
        # financial abbreviation in inline math even though another parser
        # emits the identical token as plain text.  The math boundary is only
        # presentation in these atomic cases, so do not add a FORMULA marker.
        if re.fullmatch(
            r"(?:[+-]?(?:\d+(?:\.\d+)?|\.\d+)(?:%|[xX])?|[A-Za-z]{1,12})",
            canonical,
        ):
            return canonical
        return f"{marker_prefix}{canonical}⟧" if canonical else ""

    # Process display math first so its dollar signs cannot be consumed by the
    # inline pattern.  Inline dollar math is deliberately restricted to one
    # physical line to avoid treating currency passages as formula blocks.
    patterns = (
        re.compile(r"\$\$(.*?)\$\$", flags=re.S),
        re.compile(r"\\\[(.*?)\\\]", flags=re.S),
        re.compile(r"\\\((.*?)\\\)", flags=re.S),
        re.compile(r"(?<!\\)\$(?!\$)([^\n$]+?)(?<!\\)\$(?!\$)"),
    )
    for pattern in patterns:
        text = pattern.sub(replace_formula, text)
    return text


def _collapse_image_markers(text: str) -> str:
    """Collapse adjacent normalized image markers to a single marker."""

    text = re.sub(r"(?:!\[\]){2,}", "![]", text)
    collapsed: List[str] = []
    pending_image = False
    pending_blank = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped == "![]":
            if not pending_image:
                if pending_blank and collapsed:
                    collapsed.append("")
                collapsed.append("![]")
            pending_image = True
            pending_blank = False
            continue
        if stripped == "":
            if pending_image:
                pending_blank = True
                continue
            collapsed.append(line)
            continue
        pending_image = False
        pending_blank = False
        collapsed.append(line)
    return re.sub(r"(?:!\[\]){2,}", "![]", "\n".join(collapsed))


def normalize_image_markers(text: str) -> str:
    """Normalize common Markdown/HTML image markers to a single `![]` token."""

    if not CURRENT_CONFIG.normalize_images:
        return text
    # Some parsers serialize a visual element as an XML-like container whose
    # children only describe its page and bounding box, for example:
    # <image><page>8</page><x>13</x><y>12</y><w>02</w><h>01</h></image>
    # Normalize the complete container before generic HTML stripping; otherwise
    # its coordinate values survive as a spurious number such as 813120201.
    text = re.sub(r"<image\b[^>]*>.*?</image\s*>", "\n![]\n", text, flags=re.I | re.S)
    text = re.sub(r"<img\b[^>]*>", "\n![]\n", text, flags=re.I | re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "![]", text)
    text = re.sub(r"!\[[^\]]*\]\[[^\]]*\]", "![]", text)
    text = re.sub(
        r"(?im)^\s*(?:\[image\]|\[图片\]|\[圖像\]|\[figure\]|\[fig\]|<image\s*/?>|<pic\s*/?>|<picture\s*/?>)\s*$",
        "![]",
        text,
    )
    text = re.sub(r"(?im)^\s*!\[\]\s*$", "![]", text)
    return _collapse_image_markers(text)


def normalize_markdown_text_preserve_newlines(text: str) -> str:
    """Normalize generic Markdown text while preserving newline characters."""

    text = html.unescape(text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = normalize_formula_markup(text)
    text = normalize_footnote_markers(text)
    text = normalize_details_blocks(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = normalize_image_markers(text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = normalize_image_markers(text)
    text = re.sub(r"[*_`~]+", "", text)
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t\f\v]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = _collapse_image_markers(text)
    return text.strip(" \t\n")


def normalize_semantic_text_preserve_newlines(text: str) -> str:
    """Apply the shared semantic normalization used by body and table text."""

    text = normalize_markdown_text_preserve_newlines(text)
    text = unicodedata.normalize("NFKC", text)
    text = normalize_chinese_variants(text)
    text = normalize_footnote_markers(text)
    text = normalize_punctuation_variants(text)
    return text


def normalize_details_blocks(text: str) -> str:
    """Remove details/summary wrappers while preserving useful inner content."""

    pattern = re.compile(
        r"<details>\s*<summary>\s*(.*?)\s*</summary>(.*?)</details>",
        flags=re.I | re.S,
    )

    def replace(match: re.Match[str]) -> str:
        summary = re.sub(r"\s+", "_", html.unescape(match.group(1)).strip().lower())
        summary = summary.replace("-", "_")
        body = match.group(2).strip()
        visual_summaries = {
            "natural_image",
            "flowchart",
            "figure",
            "image",
            "picture",
            "diagram",
            "visual",
        }
        has_mermaid = bool(re.search(r"```+\s*mermaid\b|^\s*(?:graph|flowchart)\s+(?:td|lr|rl|bt)\b", body, flags=re.I | re.M))
        if CURRENT_CONFIG.normalize_images and (summary in visual_summaries or has_mermaid):
            return "\n![]\n"
        if summary == "natural_image":
            return "\n"
        return f"\n{body}\n"

    previous = None
    current = text
    while previous != current:
        previous = current
        current = pattern.sub(replace, current)
    return current


CHART_DETAIL_SUMMARIES = {
    "area",
    "area_stacked",
    "bar",
    "bar_chart",
    "bar_line",
    "bar_stacked",
    "bubble",
    "chart",
    "diagram",
    "donut",
    "flow_chart",
    "flowchart",
    "graph",
    "line",
    "line_chart",
    "org_chart",
    "organization_chart",
    "pie",
    "radar",
    "relation",
    "relationship",
    "sankey",
    "scatter",
    "timeline",
    "tree",
    "treemap",
}


def _normalized_details_summary(summary: str) -> str:
    """Return a stable key for a details/summary visual type."""

    key = re.sub(r"\s+", "_", html.unescape(summary).strip().lower())
    return key.replace("-", "_")


def _is_chart_transcription_heading(line: str) -> bool:
    """Detect the heading immediately following the custom `?[]` marker."""

    compact = re.sub(r"\s+", "", line)
    return bool(re.match(r"^(?:图中|图例)", compact))


def _is_chart_transcription_payload_line(line: str) -> bool:
    """Detect a line belonging to a `?[]` chart transcription block."""

    stripped = line.strip()
    if not stripped:
        return True
    if _is_chart_transcription_heading(stripped):
        return True
    if re.match(r"^(?:[-*+]\s+|\d+[.)、]\s*)", stripped):
        return True
    if re.match(r"^(?:数据来源|资料来源|来源|注)\s*[:：]", stripped, flags=re.I):
        return True
    if re.fullmatch(r"(?:数据来源|资料来源|来源|注)", stripped, flags=re.I):
        return True
    # Short colon-terminated labels such as “出口西药类拆分：” introduce
    # another subsection inside the same chart transcription.
    if len(stripped) <= 120 and re.search(r"[:：]\s*$", stripped):
        return True
    if re.match(r"^</?(?:table|thead|tbody|tfoot|tr|t[dh])\b", stripped, flags=re.I):
        return True
    if is_pipe_row(stripped) or is_pipe_separator(stripped):
        return True
    return False


def _chart_table_records(table: TableItem) -> List[str]:
    """Convert one chart table to representation-neutral key/value records."""

    matrix = [[normalize_text(cell) for cell in row] for row in table.matrix]
    if not matrix:
        return []
    width = max((len(row) for row in matrix), default=0)
    if width <= 0:
        return []
    rows = [row + [""] * (width - len(row)) for row in matrix]
    headers = rows[0]
    if len(rows) == 1:
        return ["|".join(cell for cell in headers if cell)]

    records: List[str] = []
    for row in rows[1:]:
        fields: List[str] = []
        for index, value in enumerate(row):
            if not value:
                continue
            header = headers[index] if index < len(headers) else ""
            fields.append(f"{header}:{value}" if header else value)
        if fields:
            records.append("|".join(fields))
    return records


def _canonicalize_chart_payload(payload: str) -> str:
    """Flatten list/table chart transcriptions without losing their content.

    Gold charts commonly use repeated ``key:value`` list rows while MinerU
    emits the same values as a Markdown table.  This conversion makes those
    representations comparable. Chart tables stay outside the ordinary table
    denominator unless a marked chart-table Gold object explicitly accepts
    that alternate representation.
    """

    tables, spans = extract_tables(payload)
    remainder = remove_tables(payload, spans)
    lines: List[str] = []
    for line in remainder.splitlines():
        stripped = line.strip()
        if not stripped or stripped == "?[]" or _is_chart_transcription_heading(stripped):
            continue
        stripped = re.sub(r"^#{1,6}\s+", "", stripped)
        stripped = re.sub(r"^(?:[-*+]\s+|\d+[.)、]\s*)", "", stripped)
        if stripped:
            lines.append(stripped)
    for table in tables:
        lines.extend(_chart_table_records(table))
    if not lines:
        return "?[]"
    return "?[]\n" + "\n".join(lines)


def prepare_chart_content_for_scoring(md: str, include_charts: bool) -> Tuple[str, int]:
    """Canonicalize or remove informative chart blocks before core scoring.

    Both modes exclude unmarked chart tables from the ordinary table module.
    With ``include_charts`` enabled, the chart payload is converted to plain
    key/value records and retained in body-text scoring. Otherwise the entire
    block is removed symmetrically. Marked chart-table routing is handled by
    the table evaluator before chart scoring.
    """

    text = md.replace("\r\n", "\n").replace("\r", "\n")
    chart_count = 0
    protected_marker = "[[[REPRESENTATION_NEUTRAL_CHART]]]"

    def protected_payload(payload: str) -> str:
        canonical = _canonicalize_chart_payload(payload)
        return canonical.replace("?[]", protected_marker, 1)

    details_pattern = re.compile(
        r"<details\b[^>]*>\s*<summary\b[^>]*>\s*(.*?)\s*</summary>(.*?)</details\s*>",
        flags=re.I | re.S,
    )

    def replace_chart_details(match: re.Match[str]) -> str:
        nonlocal chart_count
        summary = _normalized_details_summary(match.group(1))
        if summary in CHART_DETAIL_SUMMARIES:
            chart_count += 1
            if not include_charts:
                return "\n"
            return "\n" + protected_payload(match.group(2)) + "\n"
        return match.group(0)

    previous = None
    while previous != text:
        previous = text
        text = details_pattern.sub(replace_chart_details, text)

    def replace_explicit_chart(match: re.Match[str]) -> str:
        nonlocal chart_count
        chart_count += 1
        if not include_charts:
            return "\n"
        return "\n" + protected_payload(match.group(1)) + "\n"

    text = re.sub(
        r"<(?:chart|diagram|flowchart)\b[^>]*>(.*?)</(?:chart|diagram|flowchart)\s*>",
        replace_explicit_chart,
        text,
        flags=re.I | re.S,
    )
    if not include_charts:
        def remove_mermaid(match: re.Match[str]) -> str:
            nonlocal chart_count
            chart_count += 1
            return "\n"

        text = re.sub(
            r"```+\s*mermaid\b.*?```+",
            remove_mermaid,
            text,
            flags=re.I | re.S,
        )

    lines = text.split("\n")
    kept: List[str] = []
    index = 0
    while index < len(lines):
        if lines[index].strip() != "?[]":
            kept.append(lines[index])
            index += 1
            continue

        chart_count += 1
        index += 1
        while index < len(lines) and not lines[index].strip():
            index += 1

        if index >= len(lines) or not _is_chart_transcription_heading(lines[index]):
            if include_charts:
                kept.extend(["", "?[]", ""])
            continue

        payload: List[str] = [lines[index]]
        index += 1
        while index < len(lines) and _is_chart_transcription_payload_line(lines[index]):
            payload.append(lines[index])
            index += 1

        while kept and not kept[-1].strip():
            kept.pop()
        kept.append("")
        if include_charts:
            kept.extend(_canonicalize_chart_payload("\n".join(payload)).splitlines())
            kept.append("")

    return "\n".join(kept).replace(protected_marker, "?[]"), chart_count


def strip_chart_content_for_scoring(md: str) -> Tuple[str, int]:
    """Backward-compatible wrapper for callers that exclude charts."""

    return prepare_chart_content_for_scoring(md, include_charts=False)


def extract_chart_payloads(md: str) -> List[str]:
    """Return informative chart payloads using prediction-local boundaries."""

    text = md.replace("\r\n", "\n").replace("\r", "\n")
    payloads: List[str] = []

    details_pattern = re.compile(
        r"<details\b[^>]*>\s*<summary\b[^>]*>\s*(.*?)\s*</summary>(.*?)</details\s*>",
        flags=re.I | re.S,
    )

    def collect_details(match: re.Match[str]) -> str:
        if _normalized_details_summary(match.group(1)) in CHART_DETAIL_SUMMARIES:
            payloads.append(match.group(2))
            return "\n"
        return match.group(0)

    previous = None
    while previous != text:
        previous = text
        text = details_pattern.sub(collect_details, text)

    def collect_explicit(match: re.Match[str]) -> str:
        payloads.append(match.group(1))
        return "\n"

    text = re.sub(
        r"<(?:chart|diagram|flowchart)\b[^>]*>(.*?)</(?:chart|diagram|flowchart)\s*>",
        collect_explicit,
        text,
        flags=re.I | re.S,
    )

    lines = text.split("\n")
    index = 0
    while index < len(lines):
        if lines[index].strip() != "?[]":
            index += 1
            continue
        index += 1
        while index < len(lines) and not lines[index].strip():
            index += 1
        block: List[str] = []
        if index < len(lines) and _is_chart_transcription_heading(lines[index]):
            block.append(lines[index])
            index += 1
            while index < len(lines) and _is_chart_transcription_payload_line(lines[index]):
                block.append(lines[index])
                index += 1
        payloads.append("\n".join(block))
    return payloads


def extract_chart_embedded_tables(
    chart_payloads: Sequence[str], index_offset: int
) -> List[TableItem]:
    """Extract optional table candidates contained inside chart payloads."""

    tables: List[TableItem] = []
    for payload_index, payload in enumerate(chart_payloads):
        payload_tables, _ = extract_tables(payload)
        for chart_table_index, table in enumerate(payload_tables):
            table.index = index_offset + len(tables)
            table.kind = f"chart_{table.kind}"
            table.from_chart_block = True
            table.chart_payload_index = payload_index
            table.chart_table_index = chart_table_index
            tables.append(table)
    return tables


def _chart_payload_has_information(payload: str) -> bool:
    """Return whether a routed chart payload still contains real chart data."""

    cleaned_lines: List[str] = []
    for line in payload.splitlines():
        stripped = line.strip()
        if not stripped or stripped in {"?[]", "![]"}:
            continue
        if re.fullmatch(r"!\[[^]]*]\([^)]*\)", stripped):
            continue
        if re.match(r"^(?:数据|资料|图表)?来源\s*[：:]", stripped):
            continue
        if re.match(r"^注\s*[：:]", stripped):
            continue
        cleaned_lines.append(stripped)
    if not cleaned_lines:
        return False
    canonical = _canonicalize_chart_payload("\n".join(cleaned_lines))
    return bool(_chart_tokens(canonical.replace("?[]", "")))


def remove_routed_chart_tables(
    chart_payloads: Sequence[str],
    auxiliary_tables: Sequence[TableItem],
    table_score: Dict[str, Any],
) -> Tuple[List[str], int]:
    """Remove chart-embedded tables already credited by the table module."""

    auxiliary_by_index = {table.index: table for table in auxiliary_tables}
    routed: Dict[int, List[Tuple[int, int]]] = {}
    for match in table_score.get("matches", []):
        if not match.get("pred_from_chart_block"):
            continue
        table = auxiliary_by_index.get(match.get("pred_index"))
        if table is None or table.chart_payload_index is None:
            continue
        routed.setdefault(table.chart_payload_index, []).append((table.start, table.end))

    kept_payloads: List[str] = []
    routed_table_count = 0
    for payload_index, payload in enumerate(chart_payloads):
        spans = sorted(routed.get(payload_index, []))
        routed_table_count += len(spans)
        if not spans:
            kept_payloads.append(payload)
            continue
        remainder = remove_tables(payload, spans)
        if _chart_payload_has_information(remainder):
            kept_payloads.append(remainder)
    return kept_payloads, routed_table_count


_CHART_TOKEN_RE = re.compile(
    r"[+-]?\d+(?:[.,]\d+)*(?:%|％|倍|亿元|万元|元|年|月|日)?"
    r"|[A-Za-z]+(?:[-_][A-Za-z0-9]+)*"
    r"|[\u3400-\u9fff]"
)


def _chart_tokens(text: str) -> List[str]:
    """Tokenize chart/body content without depending on a language model."""

    normalized = normalize_semantic_text_preserve_newlines(text).lower()
    return _CHART_TOKEN_RE.findall(normalized)


def _counter_f1(left: Counter[str], right: Counter[str]) -> float:
    left_count = sum(left.values())
    right_count = sum(right.values())
    if left_count == 0 and right_count == 0:
        return 1.0
    if left_count == 0 or right_count == 0:
        return 0.0
    overlap = sum((left & right).values())
    return 2.0 * overlap / (left_count + right_count)


def _chart_features(payload: str) -> Tuple[Counter[str], Counter[str]]:
    tokens = _chart_tokens(_canonicalize_chart_payload(payload))
    numbers = Counter(token for token in tokens if token[:1].isdigit() or token[:1] in "+-")
    words = Counter(token for token in tokens if not (token[:1].isdigit() or token[:1] in "+-"))
    return numbers, words


def _score_chart_feature_pair(
    gt_features: Tuple[Counter[str], Counter[str]],
    pred_features: Tuple[Counter[str], Counter[str]],
) -> Dict[str, float]:
    gt_numbers, gt_words = gt_features
    pred_numbers, pred_words = pred_features
    numeric_f1 = _counter_f1(gt_numbers, pred_numbers)
    lexical_f1 = _counter_f1(gt_words, pred_words)
    if not gt_numbers and not pred_numbers:
        pair_score = lexical_f1
    else:
        pair_score = numeric_f1 * 0.65 + lexical_f1 * 0.35
    return {
        "pair_score": clamp_score(pair_score * 100.0),
        "numeric_f1": clamp_score(numeric_f1 * 100.0),
        "lexical_f1": clamp_score(lexical_f1 * 100.0),
    }


def score_chart_payloads(gt_payloads: Sequence[str], pred_payloads: Sequence[str]) -> Dict[str, Any]:
    """Order-aware one-to-one chart matching with numeric-first token F1."""

    gt_count = len(gt_payloads)
    pred_count = len(pred_payloads)
    if gt_count == 0 and pred_count == 0:
        return {
            "chart_score": 100.0,
            "gt_chart_count": 0,
            "pred_chart_count": 0,
            "matched_chart_count": 0,
            "missing_chart_count": 0,
            "extra_chart_count": 0,
            "matches": [],
        }

    pair_cache: Dict[Tuple[int, int], Dict[str, float]] = {}
    gt_features = [_chart_features(payload) for payload in gt_payloads]
    pred_features = [_chart_features(payload) for payload in pred_payloads]
    dp = [[0.0] * (pred_count + 1) for _ in range(gt_count + 1)]
    choice = [[""] * (pred_count + 1) for _ in range(gt_count + 1)]
    for i in range(1, gt_count + 1):
        choice[i][0] = "skip_gt"
    for j in range(1, pred_count + 1):
        choice[0][j] = "skip_pred"
    for i in range(1, gt_count + 1):
        for j in range(1, pred_count + 1):
            pair = _score_chart_feature_pair(gt_features[i - 1], pred_features[j - 1])
            pair_cache[(i - 1, j - 1)] = pair
            candidates = (
                (dp[i - 1][j], "skip_gt"),
                (dp[i][j - 1], "skip_pred"),
                (dp[i - 1][j - 1] + pair["pair_score"], "match"),
            )
            dp[i][j], choice[i][j] = max(candidates, key=lambda item: item[0])

    matches: List[Dict[str, Any]] = []
    i, j = gt_count, pred_count
    while i > 0 or j > 0:
        action = choice[i][j]
        if action == "match":
            pair = pair_cache[(i - 1, j - 1)]
            matches.append(
                {
                    "gt_index": i - 1,
                    "pred_index": j - 1,
                    "pair_score": round_float(pair["pair_score"]),
                    "numeric_f1": round_float(pair["numeric_f1"]),
                    "lexical_f1": round_float(pair["lexical_f1"]),
                }
            )
            i -= 1
            j -= 1
        elif action == "skip_gt":
            i -= 1
        elif action == "skip_pred":
            j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1
    matches.reverse()
    denominator = max(gt_count, pred_count, 1)
    chart_score = sum(item["pair_score"] for item in matches) / denominator
    return {
        "chart_score": round_float(clamp_score(chart_score)),
        "gt_chart_count": gt_count,
        "pred_chart_count": pred_count,
        "matched_chart_count": len(matches),
        "missing_chart_count": max(gt_count - len(matches), 0),
        "extra_chart_count": max(pred_count - len(matches), 0),
        "matches": matches,
    }


def _compact_body_line(line: str) -> str:
    """Return a line without ignorable horizontal whitespace."""

    return re.sub(r"[ \t\f\v]+", "", line.strip())


def _normalize_body_line_content(line: str) -> str:
    """Normalize low-value line-level Markdown/list artifacts."""

    compact = _compact_body_line(line)
    compact = re.sub(r"^[>\u25cf\u2022\u00b7*+\-]+", "", compact)
    compact = re.sub(r"^[\[{](.*?)[\]}]$", r"\1", compact)
    return compact


def _has_toc_dot_leader(line: str) -> bool:
    """Detect table-of-contents dot leader lines ending in a page number."""

    return bool(
        re.search(r"(?:\.|\u2026|\u22ef|\u00b7|_|-){3,}\s*\d{1,4}\s*$", line)
        or re.search(r"(?:\.|\u2026|\u22ef|\u00b7|_|-){3,}\d{1,4}$", _compact_body_line(line))
    )


def _is_standalone_page_number(line: str) -> bool:
    """Detect isolated page numbers and common page footer forms."""

    compact = _compact_body_line(line)
    stripped = line.strip()
    if re.fullmatch(r"-?\d{1,4}-?", compact):
        return True
    if re.fullmatch(r"(?:page)?\d{1,4}(?:of|/)\d{1,4}", compact, flags=re.I):
        return True
    if re.fullmatch(r"\u7b2c\d{1,4}\u9875(?:/\u5171?\d{1,4}\u9875?)?", compact):
        return True
    if re.fullmatch(r"page\s+\d{1,4}(?:\s+of\s+\d{1,4})?", stripped, flags=re.I):
        return True
    return False


def _is_image_caption_noise(line: str) -> bool:
    """Detect generated natural-image captions that are not document text."""

    stripped = line.strip()
    lower = stripped.lower()
    if len(stripped) > 260:
        return False
    if re.search(r"[\u3400-\u9fff]", stripped):
        return False
    caption_starts = (
        "illustration of ",
        "an illustration of ",
        "image of ",
        "an image of ",
        "a photo of ",
        "the image shows ",
        "watercolor-style ",
    )
    caption_markers = (
        "no text or symbols",
        "no text or symbols visible",
        "cartoon character",
        "rendered in warm yellow tones",
        "rendered in monochromatic yellow tones",
    )
    return lower.startswith(caption_starts) and any(marker in lower for marker in caption_markers)


def _strip_heading_marker_for_cleanup(line: str) -> str:
    """Remove Markdown heading markers for cleanup detection only."""

    match = re.match(r"^ {0,3}#{1,6}\s+(.*?)\s*#*\s*$", line.strip())
    return match.group(1).strip() if match else line.strip()


def _looks_like_repeated_header_footer(line: str) -> bool:
    """Conservatively detect repeated report header/footer text."""

    compact = _compact_body_line(line)
    lower = compact.lower()
    if len(compact) > 80:
        return False
    if "report" in lower:
        return True
    report_terms = (
        "\u5e74\u5ea6\u62a5\u544a",
        "\u534a\u5e74\u5ea6\u62a5\u544a",
        "\u4e2d\u671f\u62a5\u544a",
        "\u5b63\u5ea6\u62a5\u544a",
    )
    return any(term in compact for term in report_terms)


def _looks_like_pred_page_artifact(line: str) -> bool:
    """Detect no-value repeated header/footer lines in prediction Markdown."""

    stripped = line.strip()
    if not stripped:
        return False
    if "<table" in stripped.lower() or "</table" in stripped.lower():
        return False
    if is_pipe_row(stripped):
        return False

    content = _strip_heading_marker_for_cleanup(stripped)
    compact = _compact_body_line(unicodedata.normalize("NFKC", content))
    if not compact or len(compact) > 90:
        return False
    if _is_standalone_page_number(content) or _has_toc_dot_leader(content):
        return True
    if _looks_like_repeated_header_footer(content):
        return True

    report_terms = (
        "\u5e74\u5ea6\u62a5\u544a",
        "\u5e74\u62a5",
        "\u4e2d\u671f\u62a5\u544a",
        "\u534a\u5e74\u5ea6\u62a5\u544a",
        "\u5b63\u5ea6\u62a5\u544a",
        "\u5e74\u5ea6\u5831\u544a",
        "\u5e74\u5831",
        "\u4e2d\u671f\u5831\u544a",
        "\u4e2d\u5831",
        "annualreport",
        "interimreport",
    )
    company_terms = (
        "\u6709\u9650\u516c\u53f8",
        "\u80a1\u4efd",
        "\u96c6\u5718",
        "\u96c6\u56e2",
        "\u63a7\u80a1",
        "\u516c\u53f8",
        "limited",
        "holdings",
        "group",
        "inc.",
        "corporation",
    )
    if any(term in compact.lower() for term in report_terms):
        return True
    lower_compact = compact.lower()
    has_company_term = any(term in lower_compact for term in company_terms)
    has_sentence_marker = any(
        marker in compact
        for marker in (
            "\uff1a",
            ":",
            "\uff0c",
            ",",
            "\u3002",
            "\uff1b",
            ";",
            "\u3001",
            "\u300a",
            "\u300b",
            "\u7684",
            "\u88ab",
            "\u4e8e",
            "\u81f4",
        )
    )
    company_name_endings = (
        "\u6709\u9650\u516c\u53f8",
        "\u80a1\u4efd\u6709\u9650\u516c\u53f8",
        "\u63a7\u80a1\u6709\u9650\u516c\u53f8",
        "limited",
        "holdingslimited",
        "corporation",
    )
    if (
        has_company_term
        and len(compact) <= 55
        and not has_sentence_marker
        and any(lower_compact.endswith(ending) for ending in company_name_endings)
    ):
        return True
    if stripped.startswith("#") and len(compact) <= 35:
        low_value_heading_terms = {
            "\u4e3b\u5e2d\u5831\u544a",
            "\u8463\u4e8b\u6703",
            "\u4f01\u696d\u7ba1\u6cbb\u5831\u544a",
            "\u74b0\u5883\u3001\u793e\u6703\u53ca\u7ba1\u6cbb\u5831\u544a",
            "\u6536\u5165",
            "\u6210\u672c\u53ca\u958b\u652f",
        }
        return compact in low_value_heading_terms
    return False


def _cleanup_line_key(line: str) -> str:
    """Return the compact key used by prediction cleanup."""

    content = _strip_heading_marker_for_cleanup(line)
    return _compact_body_line(unicodedata.normalize("NFKC", content))


def cleanup_prediction_header_footer(md: str, reference_md: Optional[str] = None) -> PredCleanupResult:
    """Remove no-value repeated headers/footers from prediction Markdown only.

    Candidate lines are only removed when prediction has more occurrences than
    the GT reference. This keeps GT-vs-GT validation at 100 while still removing
    extra page-running noise from model output.
    """

    normalized = md.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.splitlines()
    reference_counts: Counter[str] = Counter()
    if reference_md is not None:
        for ref_line in reference_md.replace("\r\n", "\n").replace("\r", "\n").splitlines():
            ref_key = _cleanup_line_key(ref_line)
            if ref_key and _looks_like_pred_page_artifact(ref_line):
                reference_counts[ref_key] += 1

    keys: List[str] = []
    counts: Counter[str] = Counter()
    for line in lines:
        key = _cleanup_line_key(line)
        keys.append(key)
        if key and _looks_like_pred_page_artifact(line):
            counts[key] += 1

    seen: Counter[str] = Counter()
    kept: List[str] = []
    removed_examples: List[str] = []
    removed_count = 0
    for line, key in zip(lines, keys):
        remove_line = False
        if key and _looks_like_pred_page_artifact(line):
            seen[key] += 1
            allowed_count = reference_counts.get(key, 0)
            if counts[key] >= 2 or _is_standalone_page_number(line) or _has_toc_dot_leader(line):
                remove_line = seen[key] > allowed_count
        if remove_line:
            removed_count += 1
            if line.strip() and len(removed_examples) < 20:
                removed_examples.append(line.strip())
            continue
        kept.append(line)

    return PredCleanupResult(
        markdown="\n".join(kept),
        removed_line_count=removed_count,
        removed_line_examples=removed_examples,
    )


def _repeated_header_footer_lines(lines: Sequence[str]) -> set[str]:
    """Return compact repeated lines that look like page headers or footers."""

    compact_lines = [_compact_body_line(line) for line in lines if _compact_body_line(line)]
    counts = Counter(compact_lines)
    return {
        line
        for line, count in counts.items()
        if count >= 3 and _looks_like_repeated_header_footer(line)
    }


def normalize_body_text_preserve_newlines(text: str, remove_repeated_noise: bool = False) -> str:
    """Normalize body text while preserving each newline as one character."""

    text = normalize_semantic_text_preserve_newlines(text)

    raw_lines = text.split("\n")
    repeated_noise = _repeated_header_footer_lines(raw_lines) if remove_repeated_noise else set()
    kept_lines: List[str] = []
    for line in raw_lines:
        compact = _compact_body_line(line)
        if _has_toc_dot_leader(line):
            continue
        if _is_standalone_page_number(line):
            continue
        if _is_image_caption_noise(line):
            continue
        if compact and compact in repeated_noise:
            continue
        kept_lines.append(_normalize_body_line_content(line) if compact else "")

    collapsed_lines: List[str] = []
    previous_blank = False
    for line in kept_lines:
        is_blank = line == ""
        if is_blank and previous_blank:
            continue
        collapsed_lines.append(line)
        previous_blank = is_blank

    return "\n".join(collapsed_lines).strip("\n")


def normalized_edit_distance_preserve_newlines(a: str, b: str) -> float:
    """Compute normalized edit distance with newlines preserved as characters."""

    a_norm = normalize_body_text_preserve_newlines(a)
    b_norm = normalize_body_text_preserve_newlines(b)
    denom = max(len(a_norm), len(b_norm), 1)
    # Always compute the exact document-level distance.  The native
    # python-Levenshtein backend is strongly recommended for speed; the
    # pure-Python path is slower but must produce the same score.  A segmented
    # approximation can change alignment when paragraph boundaries differ.
    return min(1.0, levenshtein_distance(a_norm, b_norm) / denom)


def _preview(text: str, limit: int = 140) -> str:
    """Return a compact preview string for reports."""

    text = normalize_body_text_preserve_newlines(text).replace("\n", r"\n")
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def score_text(gt_text: str, pred_text: str) -> Dict[str, Any]:
    """Score body text as one strict character sequence with newlines kept."""

    gt_body = normalize_body_text_preserve_newlines(gt_text)
    pred_body = normalize_body_text_preserve_newlines(pred_text)

    if not gt_body and not pred_body:
        return {
            "text_mode": "normalized_full_text_preserve_newlines",
            "text_score": 100.0,
            "matched_block_count": 0,
            "missing_block_count": 0,
            "extra_block_count": 0,
            "average_edit_distance": 0.0,
            "gt_block_count": 0,
            "pred_block_count": 0,
            "worst_matches": [],
        }

    average_distance = normalized_edit_distance_preserve_newlines(gt_body, pred_body)
    score = clamp_score((1.0 - average_distance) * 100.0)

    if gt_body and pred_body:
        op = "match"
        matched = 1
        missing = 0
        extra = 0
    elif gt_body:
        op = "missing"
        matched = 0
        missing = 1
        extra = 0
    else:
        op = "extra"
        matched = 0
        missing = 0
        extra = 1

    worst_matches = [
        {
            "op": op,
            "distance": round_float(average_distance),
            "gt_start": 0,
            "gt_count": 1 if gt_body else 0,
            "pred_start": 0,
            "pred_count": 1 if pred_body else 0,
            "gt_preview": _preview(gt_body),
            "pred_preview": _preview(pred_body),
        }
    ]

    return {
        "text_mode": "normalized_full_text_preserve_newlines",
        "text_score": round_float(score),
        "matched_block_count": matched,
        "missing_block_count": missing,
        "extra_block_count": extra,
        "average_edit_distance": round_float(average_distance),
        "gt_block_count": 1 if gt_body else 0,
        "pred_block_count": 1 if pred_body else 0,
        "worst_matches": worst_matches,
    }


def _matrix_shape(matrix: Sequence[Sequence[str]]) -> Tuple[int, int]:
    """Return row and max-column count for a table matrix."""

    rows = len(matrix)
    cols = max((len(row) for row in matrix), default=0)
    return rows, cols


def flatten_table_matrix_for_text(matrix: Sequence[Sequence[str]]) -> str:
    """Flatten a table matrix into row-major text for edit-distance scoring."""

    if not matrix:
        return ""
    rows = []
    for row in matrix:
        rows.append("\t".join(normalize_semantic_text_preserve_newlines(cell) for cell in row))
    return "\n".join(rows)


def normalized_table_content_distance(a: str, b: str) -> float:
    """Compute normalized edit distance for flattened table text."""

    a_norm = normalize_semantic_text_preserve_newlines(a)
    b_norm = normalize_semantic_text_preserve_newlines(b)
    denom = max(len(a_norm), len(b_norm), 1)
    return min(1.0, levenshtein_distance(a_norm, b_norm) / denom)


def table_structure_score_from_shapes(
    gt_matrix: Sequence[Sequence[str]],
    pred_matrix: Sequence[Sequence[str]],
) -> float:
    """Score table structure from row, column, and total cell-count similarity."""

    gt_rows, gt_cols = _matrix_shape(gt_matrix)
    pred_rows, pred_cols = _matrix_shape(pred_matrix)
    if gt_rows == 0 and pred_rows == 0:
        return 100.0
    row_score = 1.0 - abs(gt_rows - pred_rows) / max(gt_rows, pred_rows, 1)
    col_score = 1.0 - abs(gt_cols - pred_cols) / max(gt_cols, pred_cols, 1)
    gt_cells = gt_rows * gt_cols
    pred_cells = pred_rows * pred_cols
    cell_count_score = 1.0 - abs(gt_cells - pred_cells) / max(gt_cells, pred_cells, 1)
    return clamp_score((row_score + col_score + cell_count_score) / 3.0 * 100.0)


def score_table_pair(gt_table: TableItem, pred_table: TableItem) -> Dict[str, Any]:
    """Score one table pair from structure distance and content edit distance."""

    gt_matrix = gt_table.matrix
    pred_matrix = pred_table.matrix
    gt_rows, gt_cols = _matrix_shape(gt_matrix)
    pred_rows, pred_cols = _matrix_shape(pred_matrix)

    if gt_rows == 0 and pred_rows == 0:
        structure_score = 100.0
        content_score = 100.0
    else:
        structure_score = table_structure_score_from_shapes(gt_matrix, pred_matrix)
        gt_table_text = flatten_table_matrix_for_text(gt_matrix)
        pred_table_text = flatten_table_matrix_for_text(pred_matrix)
        if not gt_table_text and not pred_table_text:
            content_score = 100.0
        elif not gt_table_text or not pred_table_text:
            content_score = 0.0
        else:
            content_score = clamp_score(
                (1.0 - normalized_table_content_distance(gt_table_text, pred_table_text)) * 100.0
            )

    weight_sum = max(CURRENT_CONFIG.table_structure_weight + CURRENT_CONFIG.table_content_weight, 1e-9)
    structure_weight = CURRENT_CONFIG.table_structure_weight / weight_sum
    content_weight = CURRENT_CONFIG.table_content_weight / weight_sum
    final_score = clamp_score(structure_score * structure_weight + content_score * content_weight)
    return {
        "gt_index": gt_table.index,
        "pred_index": pred_table.index,
        "gt_kind": gt_table.kind,
        "pred_kind": pred_table.kind,
        "gt_accepts_chart_representation": gt_table.accept_chart_representation,
        "pred_from_chart_block": pred_table.from_chart_block,
        "pred_chart_payload_index": pred_table.chart_payload_index,
        "pred_chart_table_index": pred_table.chart_table_index,
        "gt_span_pages": list(gt_table.span_pages) if gt_table.span_pages else None,
        "pred_span_pages": list(pred_table.span_pages) if pred_table.span_pages else None,
        "gt_is_cross_page": gt_table.span_pages is not None,
        "pred_is_cross_page": pred_table.span_pages is not None,
        "gt_shape": {"rows": gt_rows, "cols": gt_cols},
        "pred_shape": {"rows": pred_rows, "cols": pred_cols},
        "table_structure_score": round_float(structure_score),
        "table_content_score": round_float(content_score),
        "table_pair_score": round_float(final_score),
    }


def match_tables(
    gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """For each GT table, choose one best unused Pred table with order-aware ties."""

    matches: List[Dict[str, Any]] = []
    used_pred: set[int] = set()
    cache = pair_cache if pair_cache is not None else {}
    candidate_limit = 5

    def pair(gt_idx: int, pred_idx: int) -> Dict[str, Any]:
        key = (gt_idx, pred_idx)
        if key not in cache:
            cache[key] = score_table_pair(gt_tables[gt_idx], pred_tables[pred_idx])
        return cache[key]

    for gt_idx in range(len(gt_tables)):
        best: Optional[Dict[str, Any]] = None
        best_pred_idx: Optional[int] = None
        candidates = [
            (
                table_structure_score_from_shapes(
                    gt_tables[gt_idx].matrix,
                    pred_tables[pred_idx].matrix,
                ),
                pred_idx,
            )
            for pred_idx in range(len(pred_tables))
            if pred_idx not in used_pred
        ]
        candidates.sort(key=lambda item: (-item[0], abs(item[1] - gt_idx), item[1]))
        for structure_score, pred_idx in candidates[:candidate_limit]:
            weight_sum = max(CURRENT_CONFIG.table_structure_weight + CURRENT_CONFIG.table_content_weight, 1e-9)
            structure_weight = CURRENT_CONFIG.table_structure_weight / weight_sum
            content_weight = CURRENT_CONFIG.table_content_weight / weight_sum
            if best is not None and structure_score * structure_weight + 100.0 * content_weight <= best["table_pair_score"]:
                break
            candidate = pair(gt_idx, pred_idx)
            if (
                best is None
                or candidate["table_pair_score"] > best["table_pair_score"]
                or (
                    candidate["table_pair_score"] == best["table_pair_score"]
                    and best_pred_idx is not None
                    and abs(pred_idx - gt_idx) < abs(best_pred_idx - gt_idx)
                )
            ):
                best = candidate
                best_pred_idx = pred_idx
        if best is None or best_pred_idx is None:
            break
        used_pred.add(best_pred_idx)
        matches.append(best)

    matches.sort(key=lambda item: item["gt_index"])
    return matches


def score_tables(
    gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Score all extracted GT and prediction tables."""

    if not gt_tables and not pred_tables:
        return {
            "table_content_score": 100.0,
            "table_structure_score": 100.0,
            "table_matrix_score": 100.0,
            "matched_table_count": 0,
            "missing_table_count": 0,
            "extra_table_count": 0,
            "gt_table_count": 0,
            "pred_table_count": 0,
            "final_table_score": 100.0,
            "matches": [],
        }

    matches = match_tables(gt_tables, pred_tables, pair_cache)
    matched_gt = {item["gt_index"] for item in matches}
    matched_pred = {item["pred_index"] for item in matches}
    missing = len(gt_tables) - len(matched_gt)
    extra = len(pred_tables) - len(matched_pred)
    denom = max(len(gt_tables), len(pred_tables), 1)

    content_score = sum(item["table_content_score"] for item in matches) / denom
    structure_score = sum(item["table_structure_score"] for item in matches) / denom
    matrix_score = sum(item["table_pair_score"] for item in matches) / denom
    final_score = matrix_score

    return {
        "table_content_score": round_float(clamp_score(content_score)),
        "table_structure_score": round_float(clamp_score(structure_score)),
        "table_matrix_score": round_float(clamp_score(matrix_score)),
        "table_alignment_strategy": "gt_best_unused_pred_one_to_one_order_aware",
        "matched_table_count": len(matches),
        "missing_table_count": missing,
        "extra_table_count": extra,
        "gt_table_count": len(gt_tables),
        "pred_table_count": len(pred_tables),
        "final_table_score": round_float(clamp_score(final_score)),
        "matches": matches,
    }


_TABLE_ANCHOR_STOPWORDS = {
    "截至",
    "年度",
    "本集团",
    "本公司",
    "人民币",
    "千元",
    "总计",
    "合计",
    "附注",
    "项目",
    "2023年",
    "2024年",
}


def table_anchor_text(matrix: Sequence[Sequence[str]]) -> str:
    """Build a compact semantic anchor from headers and row labels.

    Headers and the first column identify a financial table much more reliably
    than its numeric body.  Numbers, dates and generic report words are removed
    so similarly shaped but unrelated tables do not look artificially close.
    """

    anchor_cells: List[str] = []
    for row in matrix[:3]:
        anchor_cells.extend(str(cell) for cell in row)
    for row in matrix[3:]:
        if row:
            anchor_cells.append(str(row[0]))
    text = normalize_text(" ".join(anchor_cells))
    text = normalize_chinese_variants(text)
    text = re.sub(r"\d+(?:[.,:/%-]\d+)*", " ", text)
    for stopword in _TABLE_ANCHOR_STOPWORDS:
        text = text.replace(stopword, " ")
    text = re.sub(r"[^\w\u3400-\u9fff]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip().lower()[:6000]


def _table_anchor_features(text: str) -> Tuple[set[str], set[str]]:
    """Return word and CJK-bigram features for keyword retrieval."""

    words = {
        token
        for token in re.findall(r"[a-z][a-z0-9]{2,}|[\u3400-\u9fff]{2,}", text)
        if token not in _TABLE_ANCHOR_STOPWORDS
    }
    compact_cjk = "".join(re.findall(r"[\u3400-\u9fff]", text))
    bigrams = {
        compact_cjk[index : index + 2]
        for index in range(max(len(compact_cjk) - 1, 0))
    }
    return words, bigrams


def table_keyword_score(
    left_features: Tuple[set[str], set[str]],
    right_features: Tuple[set[str], set[str]],
) -> float:
    """Score table-header/row-label keyword overlap on a 0-100 scale."""

    left_words, left_bigrams = left_features
    right_words, right_bigrams = right_features

    def dice(left: set[str], right: set[str]) -> float:
        if not left or not right:
            return 0.0
        return 2.0 * len(left & right) / (len(left) + len(right))

    def containment(left: set[str], right: set[str]) -> float:
        if not left or not right:
            return 0.0
        return len(left & right) / max(min(len(left), len(right)), 1)

    word_score = max(dice(left_words, right_words), containment(left_words, right_words))
    bigram_score = max(
        dice(left_bigrams, right_bigrams),
        containment(left_bigrams, right_bigrams),
    )
    return round_float(100.0 * (0.35 * word_score + 0.65 * bigram_score))


def match_pred_tables(
    gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
) -> List[Dict[str, Any]]:
    """Match Pred tables to GT tables using semantic anchors plus structure.

    Candidate retrieval is deliberately independent of table order.  A global
    greedy assignment then enforces one-to-one use, which prevents a split or
    missing table near the front of a report from shifting every later match.
    """

    cache = pair_cache if pair_cache is not None else {}
    # Keyword+structure retrieval is cheap across all GT tables; only the best
    # few candidates need the much more expensive full-table edit distance.
    candidate_limit = 6
    gt_features = [
        _table_anchor_features(table_anchor_text(table.matrix)) for table in gt_tables
    ]
    pred_features = [
        _table_anchor_features(table_anchor_text(table.matrix)) for table in pred_tables
    ]

    def pair(pred_idx: int, gt_idx: int) -> Dict[str, Any]:
        key = (pred_idx, gt_idx)
        if key not in cache:
            cache[key] = score_table_pair(gt_tables[gt_idx], pred_tables[pred_idx])
        return cache[key]

    edges: List[Tuple[float, float, float, int, int, Dict[str, Any]]] = []
    for pred_idx, pred_table in enumerate(pred_tables):
        retrieval: List[Tuple[float, float, int]] = []
        for gt_idx, gt_table in enumerate(gt_tables):
            if pred_table.from_chart_block and not gt_table.accept_chart_representation:
                continue
            keyword_score = table_keyword_score(
                pred_features[pred_idx], gt_features[gt_idx]
            )
            structure_score = table_structure_score_from_shapes(
                gt_table.matrix, pred_table.matrix
            )
            retrieval_score = 0.70 * keyword_score + 0.30 * structure_score
            retrieval.append((retrieval_score, keyword_score, gt_idx))
        retrieval.sort(key=lambda item: (-item[0], item[2]))
        for _, keyword_score, gt_idx in retrieval[:candidate_limit]:
            candidate = dict(pair(pred_idx, gt_idx))
            structure_score = candidate["table_structure_score"]
            match_score = (
                0.50 * keyword_score
                + 0.30 * candidate["table_pair_score"]
                + 0.20 * structure_score
            )
            # Prefer leaving an extraction unmatched over pairing unrelated
            # tables solely because their row/column counts happen to agree.
            if match_score < 32.0:
                continue
            if keyword_score < 8.0 and candidate["table_pair_score"] < 75.0:
                continue
            candidate["table_keyword_score"] = round_float(keyword_score)
            candidate["table_match_score"] = round_float(match_score)
            edges.append(
                (
                    match_score,
                    keyword_score,
                    candidate["table_pair_score"],
                    pred_idx,
                    gt_idx,
                    candidate,
                )
            )

    edges.sort(key=lambda item: (-item[0], -item[1], -item[2], item[3], item[4]))
    used_pred: set[int] = set()
    used_gt: set[int] = set()
    matches: List[Dict[str, Any]] = []
    for _, _, _, pred_idx, gt_idx, candidate in edges:
        if pred_idx in used_pred or gt_idx in used_gt:
            continue
        used_pred.add(pred_idx)
        used_gt.add(gt_idx)
        candidate["pred_position"] = pred_idx
        candidate["gt_position"] = gt_idx
        matches.append(candidate)

    matches.sort(key=lambda item: item["pred_index"])
    return matches


def table_footprint(table: TableItem) -> Dict[str, float | int]:
    """Estimate a table's document footprint from its parser-neutral matrix.

    Equal-per-table macro averaging lets a tiny two-row table contribute as
    much as a dense multi-page table.  Pixel area is unavailable in a Gold
    Markdown file and would make scoring depend on PDF rendering details, so
    the scorer uses a reproducible proxy: the geometric mean of expanded grid
    slots and normalized cell characters.  The geometric mean prevents either
    a mostly empty large grid or one exceptionally verbose cell from dominating
    by itself.  Expanded rowspan/colspan cells intentionally contribute to the
    estimate because they occupy visual grid area in the source table.
    """

    rows = len(table.matrix)
    cols = max((len(row) for row in table.matrix), default=0)
    grid_slots = max(rows * cols, 1)
    normalized_characters = sum(
        len(normalize_text(cell)) for row in table.matrix for cell in row
    )
    character_units = max(normalized_characters, grid_slots, 1)
    units = math.sqrt(float(grid_slots) * float(character_units))
    return {
        "rows": rows,
        "cols": cols,
        "grid_slots": grid_slots,
        "normalized_characters": normalized_characters,
        "footprint_units": units,
    }


def _table_source_cells(table: TableItem) -> List[str]:
    """Return source cells once, without duplicating rowspan/colspan text."""

    if table.kind == "html":
        parser = SimpleTableHTMLParser()
        parser.feed(table.raw)
        parser.close()
        return [str(cell["text"]) for row in parser.rows for cell in row]
    return [cell for row in table.matrix for cell in row]


def table_information_units(tables: Sequence[TableItem]) -> Dict[str, int]:
    """Count semantic table tokens plus one structural unit per grid slot."""

    semantic_tokens = 0
    grid_slots = 0
    for table in tables:
        semantic_tokens += sum(
            len(_chart_tokens(cell)) for cell in _table_source_cells(table)
        )
        rows = len(table.matrix)
        cols = max((len(row) for row in table.matrix), default=0)
        grid_slots += rows * cols
    return {
        "semantic_tokens": semantic_tokens,
        "grid_slots": grid_slots,
        "information_units": semantic_tokens + grid_slots,
    }


def calculate_module_weights(
    gt_tables: Sequence[TableItem],
    gt_body_token_count: int,
    gt_chart_token_count: int,
    score_charts: bool,
) -> Tuple[Dict[str, float], Dict[str, Any]]:
    """Split the non-heading score budget by Gold content information share."""

    title_weight = clamp_score(CURRENT_CONFIG.title_layout_weight * 100.0) / 100.0
    content_budget = max(0.0, 1.0 - title_weight)
    table_stats = table_information_units(gt_tables)
    active_chart_tokens = gt_chart_token_count if score_charts else 0
    text_units = gt_body_token_count + active_chart_tokens
    table_units = int(table_stats["information_units"])
    total_units = table_units + text_units
    if total_units:
        table_share = table_units / total_units
    else:
        table_share = 0.0
    weights = {
        "table": content_budget * table_share,
        "title_layout": title_weight,
        "text": content_budget * (1.0 - table_share),
    }
    details = {
        "mode": "gt_content_information_share",
        "title_layout_reserve": title_weight,
        "content_budget": content_budget,
        "table_semantic_tokens": table_stats["semantic_tokens"],
        "table_grid_slots": table_stats["grid_slots"],
        "table_information_units": table_units,
        "body_information_units": gt_body_token_count,
        "chart_information_units": active_chart_tokens,
        "text_information_units": text_units,
        "total_content_information_units": total_units,
        "table_content_share": table_share,
    }
    return weights, details


def _apply_footprint_aggregation(
    gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    matches: Sequence[Dict[str, Any]],
) -> Tuple[float, float, float, List[Dict[str, Any]], List[Dict[str, Any]], float, float]:
    """Aggregate matched table scores by GT footprint and penalize extra Pred area."""

    gt_stats = [table_footprint(table) for table in gt_tables]
    pred_stats = [table_footprint(table) for table in pred_tables]
    gt_total = sum(float(item["footprint_units"]) for item in gt_stats)
    matched_regular_pred = {
        item["pred_index"]
        for item in matches
        if item["pred_index"] < len(pred_tables)
    }
    extra_pred_indices = [
        index for index in range(len(pred_tables)) if index not in matched_regular_pred
    ]
    extra_pred_total = sum(
        float(pred_stats[index]["footprint_units"]) for index in extra_pred_indices
    )
    denominator = max(gt_total + extra_pred_total, 1.0)

    weighted_matches: List[Dict[str, Any]] = []
    content_numerator = 0.0
    structure_numerator = 0.0
    pair_numerator = 0.0
    for item in matches:
        gt_index = int(item["gt_index"])
        gt_units = float(gt_stats[gt_index]["footprint_units"])
        enriched = dict(item)
        enriched["gt_footprint"] = {
            **gt_stats[gt_index],
            "document_weight": gt_units / gt_total if gt_total else 0.0,
        }
        if item["pred_index"] < len(pred_stats):
            enriched["pred_footprint"] = pred_stats[item["pred_index"]]
        content_numerator += float(item["table_content_score"]) * gt_units
        structure_numerator += float(item["table_structure_score"]) * gt_units
        pair_numerator += float(item["table_pair_score"]) * gt_units
        weighted_matches.append(enriched)

    gt_footprints = [
        {
            "gt_index": index,
            **stats,
            "document_weight": (
                float(stats["footprint_units"]) / gt_total if gt_total else 0.0
            ),
        }
        for index, stats in enumerate(gt_stats)
    ]
    extra_pred_footprints = [
        {"pred_index": index, **pred_stats[index]} for index in extra_pred_indices
    ]
    return (
        content_numerator / denominator,
        structure_numerator / denominator,
        pair_numerator / denominator,
        weighted_matches,
        gt_footprints,
        gt_total,
        extra_pred_total,
    )


def score_tables_pred_driven(
    gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
    auxiliary_chart_tables: Sequence[TableItem] = (),
) -> Dict[str, Any]:
    """Score one GT variant with pred-driven semantic one-to-one matching.

    Each prediction table searches the complete GT table set using keyword
    anchors plus structure.  Unrelated tables may remain unmatched, so a
    missing table near the front cannot shift all later matches.
    """

    if not gt_tables and not pred_tables:
        return {
            "table_content_score": 100.0,
            "table_structure_score": 100.0,
            "table_matrix_score": 100.0,
            "table_alignment_strategy": "pred_semantic_best_one_to_one_gt_footprint_weighted",
            "table_aggregation": CURRENT_CONFIG.table_aggregation,
            "matched_table_count": 0,
            "missing_table_count": 0,
            "extra_table_count": 0,
            "gt_table_count": 0,
            "pred_table_count": 0,
            "auxiliary_chart_table_count": len(auxiliary_chart_tables),
            "auxiliary_chart_table_matched_count": 0,
            "gt_chart_table_eligible_count": 0,
            "gt_table_footprints": [],
            "gt_footprint_total": 0.0,
            "extra_pred_footprint_total": 0.0,
            "final_table_score": 100.0,
            "matches": [],
        }

    combined_pred_tables = list(pred_tables) + list(auxiliary_chart_tables)
    matches = match_pred_tables(gt_tables, combined_pred_tables, pair_cache)
    matched_gt = {item["gt_index"] for item in matches}
    matched_regular_pred = {
        item["pred_index"]
        for item in matches
        if item["pred_index"] < len(pred_tables)
    }
    matched_auxiliary = sum(
        1 for item in matches if item.get("pred_from_chart_block")
    )
    gt_footprints: List[Dict[str, Any]] = []
    gt_footprint_total = 0.0
    extra_pred_footprint_total = 0.0
    if CURRENT_CONFIG.table_aggregation == "footprint":
        (
            content_score,
            structure_score,
            matrix_score,
            matches,
            gt_footprints,
            gt_footprint_total,
            extra_pred_footprint_total,
        ) = _apply_footprint_aggregation(gt_tables, pred_tables, matches)
        alignment_strategy = "pred_semantic_best_one_to_one_gt_footprint_weighted"
    else:
        denominator = max(len(gt_tables), len(pred_tables), 1)
        content_score = sum(item["table_content_score"] for item in matches) / denominator
        structure_score = sum(item["table_structure_score"] for item in matches) / denominator
        matrix_score = sum(item["table_pair_score"] for item in matches) / denominator
        alignment_strategy = "pred_semantic_best_one_to_one_uniform"

    return {
        "table_content_score": round_float(clamp_score(content_score)),
        "table_structure_score": round_float(clamp_score(structure_score)),
        "table_matrix_score": round_float(clamp_score(matrix_score)),
        "table_alignment_strategy": alignment_strategy,
        "table_aggregation": CURRENT_CONFIG.table_aggregation,
        "matched_table_count": len(matches),
        "missing_table_count": len(gt_tables) - len(matched_gt),
        "extra_table_count": len(pred_tables) - len(matched_regular_pred),
        "gt_table_count": len(gt_tables),
        "pred_table_count": len(pred_tables),
        "auxiliary_chart_table_count": len(auxiliary_chart_tables),
        "auxiliary_chart_table_matched_count": matched_auxiliary,
        "gt_chart_table_eligible_count": sum(
            table.accept_chart_representation for table in gt_tables
        ),
        "gt_table_footprints": gt_footprints,
        "gt_footprint_total": round_float(gt_footprint_total),
        "extra_pred_footprint_total": round_float(extra_pred_footprint_total),
        "final_table_score": round_float(clamp_score(matrix_score)),
        "matches": matches,
    }


def score_tables_per_pred_max(
    primary_gt_tables: Sequence[TableItem],
    alt_gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    primary_pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
    alt_pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
    auxiliary_chart_tables: Sequence[TableItem] = (),
) -> Dict[str, Any]:
    """Score each Pred table against both GT variants and retain its better pair.

    One-to-one matching is enforced independently inside the primary and alt GT
    variants. A prediction table can therefore use the representation that best
    matches its page-merge behavior, while unmatched prediction tables still
    receive zero through the final denominator.
    """

    if not primary_gt_tables and not alt_gt_tables and not pred_tables:
        return {
            "table_content_score": 100.0,
            "table_structure_score": 100.0,
            "table_matrix_score": 100.0,
            "matched_table_count": 0,
            "missing_table_count": 0,
            "extra_table_count": 0,
            "gt_table_count": 0,
            "pred_table_count": 0,
            "auxiliary_chart_table_count": len(auxiliary_chart_tables),
            "auxiliary_chart_table_matched_count": 0,
            "reference_table_count": 0,
            "table_alignment_strategy": "per_table_best_of_primary_alt_gt_footprint_weighted",
            "table_aggregation": CURRENT_CONFIG.table_aggregation,
            "gt_table_footprints": {},
            "gt_footprint_total": 0.0,
            "extra_pred_footprint_total": 0.0,
            "final_table_score": 100.0,
            "matches": [],
        }

    combined_pred_tables = list(pred_tables) + list(auxiliary_chart_tables)
    primary_matches = {
        item["pred_position"]: item
        for item in match_pred_tables(
            primary_gt_tables, combined_pred_tables, primary_pair_cache
        )
    }
    alt_matches = {
        item["pred_position"]: item
        for item in match_pred_tables(
            alt_gt_tables, combined_pred_tables, alt_pair_cache
        )
    }
    matches: List[Dict[str, Any]] = []
    primary_selected_count = 0
    alt_selected_count = 0

    for pred_idx in range(len(combined_pred_tables)):
        primary_match = primary_matches.get(pred_idx)
        alt_match = alt_matches.get(pred_idx)
        if primary_match is None and alt_match is None:
            continue
        if alt_match is not None and (
            primary_match is None
            or alt_match["table_pair_score"] > primary_match["table_pair_score"]
        ):
            selected = dict(alt_match)
            selected["selected_gt_variant"] = "alt"
            alt_selected_count += 1
        else:
            selected = dict(primary_match) if primary_match is not None else dict(alt_match)
            selected["selected_gt_variant"] = "primary"
            primary_selected_count += 1
        selected["primary_pair_score"] = (
            primary_match["table_pair_score"] if primary_match is not None else None
        )
        selected["alt_pair_score"] = alt_match["table_pair_score"] if alt_match is not None else None
        matches.append(selected)

    reference_table_count = min(len(primary_gt_tables), len(alt_gt_tables))
    matched_count = len(matches)
    matched_regular_pred = {
        item["pred_index"]
        for item in matches
        if item["pred_index"] < len(pred_tables)
    }
    matched_auxiliary = sum(
        1 for item in matches if item.get("pred_from_chart_block")
    )
    gt_footprints: Dict[str, List[Dict[str, Any]]] = {}
    gt_footprint_total = 0.0
    extra_pred_footprint_total = 0.0
    if CURRENT_CONFIG.table_aggregation == "footprint":
        variant_tables = {
            "primary": primary_gt_tables,
            "alt": alt_gt_tables,
        }
        variant_stats = {
            name: [table_footprint(table) for table in tables]
            for name, tables in variant_tables.items()
        }
        variant_totals = {
            name: sum(float(item["footprint_units"]) for item in stats)
            for name, stats in variant_stats.items()
        }
        positive_totals = [value for value in variant_totals.values() if value > 0]
        reference_footprint = min(positive_totals) if positive_totals else 1.0
        gt_footprint_total = reference_footprint
        pred_stats = [table_footprint(table) for table in pred_tables]
        extra_pred_indices = [
            index for index in range(len(pred_tables)) if index not in matched_regular_pred
        ]
        extra_pred_footprint_total = sum(
            float(pred_stats[index]["footprint_units"])
            for index in extra_pred_indices
        )

        enriched_matches: List[Dict[str, Any]] = []
        selected_weight_total = 0.0
        content_numerator = 0.0
        structure_numerator = 0.0
        pair_numerator = 0.0
        for item in matches:
            variant = str(item.get("selected_gt_variant", "primary"))
            raw_stats = variant_stats[variant][int(item["gt_index"])]
            variant_total = max(variant_totals[variant], 1.0)
            scaled_units = (
                float(raw_stats["footprint_units"])
                * reference_footprint
                / variant_total
            )
            enriched = dict(item)
            enriched["gt_footprint"] = {
                **raw_stats,
                "variant": variant,
                "variant_document_weight": (
                    float(raw_stats["footprint_units"]) / variant_total
                ),
                "scaled_footprint_units": scaled_units,
            }
            if item["pred_index"] < len(pred_stats):
                enriched["pred_footprint"] = pred_stats[item["pred_index"]]
            selected_weight_total += scaled_units
            content_numerator += float(item["table_content_score"]) * scaled_units
            structure_numerator += float(item["table_structure_score"]) * scaled_units
            pair_numerator += float(item["table_pair_score"]) * scaled_units
            enriched_matches.append(enriched)

        denominator = max(reference_footprint, selected_weight_total, 1.0)
        denominator += extra_pred_footprint_total
        content_score = content_numerator / denominator
        structure_score = structure_numerator / denominator
        matrix_score = pair_numerator / denominator
        matches = enriched_matches
        for name, stats in variant_stats.items():
            variant_total = max(variant_totals[name], 1.0)
            gt_footprints[name] = [
                {
                    "gt_index": index,
                    **item,
                    "document_weight": float(item["footprint_units"]) / variant_total,
                }
                for index, item in enumerate(stats)
            ]
        alignment_strategy = "per_table_best_of_primary_alt_gt_footprint_weighted"
    else:
        denominator = max(len(pred_tables), reference_table_count, 1)
        content_score = sum(item["table_content_score"] for item in matches) / denominator
        structure_score = sum(item["table_structure_score"] for item in matches) / denominator
        matrix_score = sum(item["table_pair_score"] for item in matches) / denominator
        alignment_strategy = "per_table_best_of_primary_alt_one_to_one_uniform"

    return {
        "table_content_score": round_float(clamp_score(content_score)),
        "table_structure_score": round_float(clamp_score(structure_score)),
        "table_matrix_score": round_float(clamp_score(matrix_score)),
        "table_alignment_strategy": alignment_strategy,
        "table_aggregation": CURRENT_CONFIG.table_aggregation,
        "matched_table_count": matched_count,
        "missing_table_count": max(reference_table_count - matched_count, 0),
        "extra_table_count": len(pred_tables) - len(matched_regular_pred),
        "gt_table_count": reference_table_count,
        "pred_table_count": len(pred_tables),
        "auxiliary_chart_table_count": len(auxiliary_chart_tables),
        "auxiliary_chart_table_matched_count": matched_auxiliary,
        "primary_gt_table_count": len(primary_gt_tables),
        "alt_gt_table_count": len(alt_gt_tables),
        "reference_table_count": reference_table_count,
        "primary_selected_pair_count": primary_selected_count,
        "alt_selected_pair_count": alt_selected_count,
        "gt_table_footprints": gt_footprints,
        "gt_footprint_total": round_float(gt_footprint_total),
        "extra_pred_footprint_total": round_float(extra_pred_footprint_total),
        "final_table_score": round_float(clamp_score(matrix_score)),
        "matches": matches,
    }


def select_table_score(
    primary_score: Dict[str, Any],
    alt_score: Optional[Dict[str, Any]],
    strategy: str,
) -> Tuple[str, Dict[str, Any]]:
    """Select the table score according to primary/alt/max strategy."""

    if strategy == "primary" or alt_score is None:
        selected_name = "primary"
        if strategy == "alt" and alt_score is None:
            selected_name = "primary (alt unavailable)"
        return selected_name, primary_score
    if strategy == "alt":
        return "alt", alt_score
    if alt_score["final_table_score"] > primary_score["final_table_score"]:
        return "alt", alt_score
    return "primary", primary_score


def evaluate(
    gt_path: str | Path,
    pred_path: str | Path,
    gt_table_alt_path: Optional[str | Path] = None,
    table_gt_strategy: str = "max",
    config: Optional[ScoringConfig] = None,
) -> Dict[str, Any]:
    """Run the full scoring pipeline and return a JSON-serializable result."""

    global CURRENT_CONFIG
    CURRENT_CONFIG = config or ScoringConfig()
    gt_md = read_markdown(gt_path)
    pred_md = read_markdown(pred_path)
    if CURRENT_CONFIG.remove_pred_header_footer:
        pred_cleanup = cleanup_prediction_header_footer(pred_md, reference_md=gt_md)
        pred_md = pred_cleanup.markdown
    else:
        pred_cleanup = PredCleanupResult(markdown=pred_md, removed_line_count=0, removed_line_examples=[])

    gt_chart_payloads = extract_chart_payloads(gt_md)
    pred_chart_payloads = extract_chart_payloads(pred_md)
    # Chart content does not enter the ordinary business-table denominator;
    # only tables matched to explicit chart-table Gold objects are routed once.
    # The chart-aware mode blends a separate representation-neutral chart
    # score into the text module below; chart-off uses the same chart-free body.
    gt_scoring_md, gt_chart_count = prepare_chart_content_for_scoring(
        gt_md, include_charts=False
    )
    pred_scoring_md, pred_chart_count = prepare_chart_content_for_scoring(
        pred_md, include_charts=False
    )

    gt_tables, gt_table_spans = extract_tables(gt_scoring_md)
    pred_tables, pred_table_spans = extract_tables(pred_scoring_md)
    auxiliary_chart_tables = extract_chart_embedded_tables(
        pred_chart_payloads, len(pred_tables)
    )

    alt_tables: Optional[List[TableItem]] = None
    alt_score: Optional[Dict[str, Any]] = None
    alt_chart_count = 0
    if gt_table_alt_path:
        alt_md = read_markdown(gt_table_alt_path)
        alt_md, alt_chart_count = prepare_chart_content_for_scoring(
            alt_md, include_charts=False
        )
        alt_tables, _ = extract_tables(alt_md)

    primary_pair_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
    alt_pair_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
    primary_table_score = score_tables_pred_driven(
        gt_tables,
        pred_tables,
        primary_pair_cache,
        auxiliary_chart_tables,
    )
    if alt_tables is not None:
        alt_score = score_tables_pred_driven(
            alt_tables,
            pred_tables,
            alt_pair_cache,
            auxiliary_chart_tables,
        )
    if table_gt_strategy == "max" and alt_tables is not None:
        selected_table_name = "per_table_max"
        selected_table_score = score_tables_per_pred_max(
            gt_tables,
            alt_tables,
            pred_tables,
            primary_pair_cache,
            alt_pair_cache,
            auxiliary_chart_tables,
        )
    else:
        selected_table_name, selected_table_score = select_table_score(
            primary_table_score, alt_score, table_gt_strategy
        )

    routed_pred_chart_payloads, routed_chart_table_count = remove_routed_chart_tables(
        pred_chart_payloads,
        auxiliary_chart_tables,
        selected_table_score,
    )
    chart_score = score_chart_payloads(
        gt_chart_payloads, routed_pred_chart_payloads
    )

    gt_without_tables = remove_chart_table_markers(
        remove_tables(gt_scoring_md, gt_table_spans)
    )
    pred_without_tables = remove_chart_table_markers(
        remove_tables(pred_scoring_md, pred_table_spans)
    )
    gt_heading_items = extract_heading_items(gt_without_tables)
    pred_heading_items = extract_heading_items(pred_without_tables)
    gt_heading_levels = [item.level for item in gt_heading_items]
    pred_heading_levels = [item.level for item in pred_heading_items]
    title_score = score_title_layout(
        gt_heading_levels,
        pred_heading_levels,
        gt_heading_items,
        pred_heading_items,
    )

    gt_text_for_scoring = strip_heading_markers_keep_text(gt_without_tables)
    pred_text_for_scoring = strip_heading_markers_keep_text(pred_without_tables)
    base_text_score = score_text(gt_text_for_scoring, pred_text_for_scoring)
    text_score = dict(base_text_score)
    gt_body_token_count = len(_chart_tokens(gt_text_for_scoring))
    gt_chart_token_count = sum(
        len(_chart_tokens(_canonicalize_chart_payload(payload)))
        for payload in gt_chart_payloads
    )
    total_reference_tokens = gt_body_token_count + gt_chart_token_count
    chart_token_share = (
        gt_chart_token_count / total_reference_tokens if total_reference_tokens else 0.0
    )
    if CURRENT_CONFIG.score_charts:
        combined_text_score = (
            base_text_score["text_score"] * (1.0 - chart_token_share)
            + chart_score["chart_score"] * chart_token_share
        )
        text_score["text_score"] = round_float(clamp_score(combined_text_score))
        text_score["text_mode"] = "body_edit_distance_plus_representation_neutral_chart_tokens"
    text_score["body_only_text_score"] = base_text_score["text_score"]
    text_score["chart_score"] = chart_score["chart_score"]
    text_score["gt_body_token_count"] = gt_body_token_count
    text_score["gt_chart_token_count"] = gt_chart_token_count
    text_score["chart_token_share"] = round_float(chart_token_share)

    content_weights, content_weighting_details = calculate_module_weights(
        gt_tables,
        gt_body_token_count,
        gt_chart_token_count,
        CURRENT_CONFIG.score_charts,
    )
    if CURRENT_CONFIG.module_weighting == "content":
        effective_weights = content_weights
        weighting_details = content_weighting_details
    else:
        effective_weights = dict(WEIGHTS)
        weighting_details = {
            **content_weighting_details,
            "mode": "fixed_40_20_40",
        }

    final_score = (
        selected_table_score["final_table_score"] * effective_weights["table"]
        + title_score["title_layout_score"] * effective_weights["title_layout"]
        + text_score["text_score"] * effective_weights["text"]
    )

    return {
        "inputs": {
            "gt": str(gt_path),
            "pred": str(pred_path),
            "gt_table_alt": str(gt_table_alt_path) if gt_table_alt_path else None,
            "table_gt_strategy": table_gt_strategy,
        },
        "pred_cleanup": {
            "mode": "prediction_only_header_footer_cleanup",
            "removed_line_count": pred_cleanup.removed_line_count,
            "removed_line_examples": pred_cleanup.removed_line_examples,
        },
        "chart_evaluation": {
            "score_charts": CURRENT_CONFIG.score_charts,
            "mode": (
                "included_as_order_aware_numeric_first_token_score"
                if CURRENT_CONFIG.score_charts
                else "excluded_from_scoring"
            ),
            "gt_chart_block_count": gt_chart_count,
            "alt_gt_chart_block_count": alt_chart_count,
            "pred_chart_block_count": pred_chart_count,
            "pred_chart_payload_count_after_chart_table_routing": len(
                routed_pred_chart_payloads
            ),
            "routed_chart_table_count": routed_chart_table_count,
            "gt_removed_block_count": 0 if CURRENT_CONFIG.score_charts else gt_chart_count,
            "alt_gt_removed_block_count": 0 if CURRENT_CONFIG.score_charts else alt_chart_count,
            "pred_removed_block_count": 0 if CURRENT_CONFIG.score_charts else pred_chart_count,
            "chart_score": chart_score,
            "gt_body_token_count": gt_body_token_count,
            "gt_chart_token_count": gt_chart_token_count,
            "chart_token_share": round_float(chart_token_share),
        },
        "weights": effective_weights,
        "weighting_evaluation": weighting_details,
        "config": asdict(CURRENT_CONFIG),
        "scores": {
            "final_score": round_float(clamp_score(final_score)),
            "table_score": selected_table_score["final_table_score"],
            "title_layout_score": title_score["title_layout_score"],
            "text_score": text_score["text_score"],
        },
        "table_evaluation": {
            "selected_gt": selected_table_name,
            "selected_table_score": selected_table_score,
            "primary_table_score": primary_table_score,
            "alt_table_score": alt_score,
        },
        "title_layout_evaluation": title_score,
        "text_evaluation": text_score,
    }


def _format_level_list(levels: Sequence[int], limit: int = 120) -> str:
    """Format heading levels without making huge reports."""

    values = list(levels)
    if len(values) <= limit:
        return str(values)
    return f"{values[:limit]} ... ({len(values)} total)"


def generate_markdown_report(result: Dict[str, Any]) -> str:
    """Generate a human-readable Markdown report."""

    scores = result["scores"]
    table_eval = result["table_evaluation"]
    selected_name = table_eval["selected_gt"]
    selected_table = table_eval.get("selected_table_score") or (
        table_eval["alt_table_score"]
        if selected_name == "alt"
        else table_eval["primary_table_score"]
    )
    primary_table = table_eval["primary_table_score"]
    alt_table = table_eval["alt_table_score"]
    title_eval = result["title_layout_evaluation"]
    text_eval = result["text_evaluation"]
    pred_cleanup = result.get("pred_cleanup", {})
    chart_eval = result.get("chart_evaluation", {})
    config = result.get("config", {})
    effective_weights = result.get("weights", WEIGHTS)
    weighting_eval = result.get("weighting_evaluation", {})

    lines = [
        "# Financial Markdown Scoring Report",
        "",
        "## Overall",
        f"- Final Score: {scores['final_score']:.4f}",
        f"- Table Score: {scores['table_score']:.4f}",
        f"- Title Layout Score: {scores['title_layout_score']:.4f}",
        f"- Text Score: {scores['text_score']:.4f}",
        "",
        "## Prediction Cleanup",
        f"- Mode: {pred_cleanup.get('mode', 'none')}",
        f"- Removed pred header/footer lines: {pred_cleanup.get('removed_line_count', 0)}",
        "- Removed examples:",
    ]
    examples = pred_cleanup.get("removed_line_examples") or []
    if examples:
        for example in examples[:10]:
            lines.append(f"  - {example}")
    else:
        lines.append("  - None")
    lines.extend(
        [
            "",
            "## Weights",
            f"- Mode: {weighting_eval.get('mode', 'fixed_40_20_40')}",
            f"- Table: {100.0 * float(effective_weights.get('table', 0.40)):.2f}%",
            f"- Title Layout: {100.0 * float(effective_weights.get('title_layout', 0.20)):.2f}%",
            f"- Text: {100.0 * float(effective_weights.get('text', 0.40)):.2f}%",
            f"- GT table semantic tokens / grid slots / information units: "
            f"{weighting_eval.get('table_semantic_tokens', 0)} / "
            f"{weighting_eval.get('table_grid_slots', 0)} / "
            f"{weighting_eval.get('table_information_units', 0)}",
            f"- GT body / active chart / text information units: "
            f"{weighting_eval.get('body_information_units', 0)} / "
            f"{weighting_eval.get('chart_information_units', 0)} / "
            f"{weighting_eval.get('text_information_units', 0)}",
            "",
            "## Configuration",
            f"- Remove pred header/footer: {config.get('remove_pred_header_footer', True)}",
            f"- Normalize images: {config.get('normalize_images', True)}",
            f"- Score informative charts: {config.get('score_charts', True)}",
            f"- Normalize Chinese variants: {config.get('normalize_zh', 't2s')}",
            f"- Normalize footnotes: {config.get('normalize_footnotes', True)}",
            f"- Normalize punctuation: {config.get('normalize_punctuation', True)}",
            f"- Table pair weights: structure={config.get('table_structure_weight', 0.60)}, "
            f"content={config.get('table_content_weight', 0.40)}",
            f"- Table aggregation: {config.get('table_aggregation', 'footprint')}",
            f"- Module weighting: {config.get('module_weighting', 'content')}",
            f"- Title layout reserve: {config.get('title_layout_weight', 0.20)}",
            f"- Chart scoring mode: {chart_eval.get('mode', 'included_in_scoring')}",
            f"- Detected primary GT / Pred chart blocks: "
            f"{chart_eval.get('gt_chart_block_count', 0)} / "
            f"{chart_eval.get('pred_chart_block_count', 0)}",
            f"- Representation-neutral chart score: "
            f"{chart_eval.get('chart_score', {}).get('chart_score', 0.0):.4f}",
            f"- GT chart token share inside text module: "
            f"{chart_eval.get('chart_token_share', 0.0):.4f}",
            f"- Removed primary GT / alt GT / Pred chart blocks: "
            f"{chart_eval.get('gt_removed_block_count', 0)} / "
            f"{chart_eval.get('alt_gt_removed_block_count', 0)} / "
            f"{chart_eval.get('pred_removed_block_count', 0)}",
            "",
            "## Table Evaluation",
            f"- Table GT strategy result: {selected_name}",
            f"- Primary table score: {primary_table['final_table_score']:.4f}",
        ]
    )
    if alt_table is not None:
        lines.append(f"- Alt table score: {alt_table['final_table_score']:.4f}")
    if selected_name == "per_table_max":
        lines.extend(
            [
                "- Per-table rule: each predicted table keeps its higher one-to-one pair score from primary or alt GT.",
                f"- Per-table selected primary / alt pairs: "
                f"{selected_table.get('primary_selected_pair_count', 0)} / "
                f"{selected_table.get('alt_selected_pair_count', 0)}",
                f"- Per-table reference table count: "
                f"{selected_table.get('reference_table_count', 0)}",
            ]
        )
    lines.extend(
        [
            f"- Matched / missing / extra tables: {selected_table['matched_table_count']} / "
            f"{selected_table['missing_table_count']} / {selected_table['extra_table_count']}",
            f"- Table content score: {selected_table['table_content_score']:.4f}",
            f"- Table structure score: {selected_table['table_structure_score']:.4f}",
            f"- Table matrix score: {selected_table.get('table_matrix_score', selected_table['final_table_score']):.4f}",
            f"- Table alignment strategy: {selected_table.get('table_alignment_strategy', 'unknown')}",
            f"- GT footprint total / extra Pred footprint: "
            f"{selected_table.get('gt_footprint_total', 0.0):.4f} / "
            f"{selected_table.get('extra_pred_footprint_total', 0.0):.4f}",
            f"- Chart-table eligible / auxiliary / matched: "
            f"{selected_table.get('gt_chart_table_eligible_count', 0)} / "
            f"{selected_table.get('auxiliary_chart_table_count', 0)} / "
            f"{selected_table.get('auxiliary_chart_table_matched_count', 0)}",
        ]
    )
    footprint_rows = selected_table.get("gt_table_footprints") or []
    if isinstance(footprint_rows, list) and footprint_rows:
        lines.extend(["", "### GT Table Footprint Weights"])
        for item in footprint_rows[:50]:
            lines.append(
                "- GT table {index}: weight={weight:.2f}%, grid={rows}x{cols}, "
                "characters={characters}, footprint={footprint:.4f}".format(
                    index=item.get("gt_index", 0),
                    weight=100.0 * float(item.get("document_weight", 0.0)),
                    rows=item.get("rows", 0),
                    cols=item.get("cols", 0),
                    characters=item.get("normalized_characters", 0),
                    footprint=float(item.get("footprint_units", 0.0)),
                )
            )
        if len(footprint_rows) > 50:
            lines.append(f"- ... {len(footprint_rows) - 50} more tables in JSON report.")
    lines.extend(["", "### Table Matches"])
    if selected_table["matches"]:
        for match in selected_table["matches"][:30]:
            gt_weight = match.get("gt_footprint", {}).get("document_weight")
            weight_text = f", GT weight={100.0 * float(gt_weight):.2f}%" if gt_weight is not None else ""
            lines.append(
                "- {variant} GT table {gt_index} -> Pred table {pred_index}: pair={pair:.4f}, "
                "structure={structure:.4f}, content={content:.4f}, "
                "keywords={keywords:.4f}, match={match_score:.4f}, "
                "GT shape={gt_shape}, Pred shape={pred_shape}{weight_text}".format(
                    variant=match.get("selected_gt_variant", selected_name),
                    gt_index=match["gt_index"],
                    pred_index=match["pred_index"],
                    pair=match["table_pair_score"],
                    structure=match["table_structure_score"],
                    content=match["table_content_score"],
                    keywords=match.get("table_keyword_score", 0.0),
                    match_score=match.get("table_match_score", match["table_pair_score"]),
                    gt_shape=match["gt_shape"],
                    pred_shape=match["pred_shape"],
                    weight_text=weight_text,
                )
            )
    else:
        lines.append("- No matched tables.")

    lines.extend(
        [
            "",
            "## Title Layout Evaluation",
            f"- GT raw heading levels: `{_format_level_list(title_eval['gt_raw_heading_levels'])}`",
            f"- Pred raw heading levels: `{_format_level_list(title_eval['pred_raw_heading_levels'])}`",
            f"- GT relative heading levels: `{_format_level_list(title_eval['gt_relative_heading_levels'])}`",
            f"- Pred relative heading levels: `{_format_level_list(title_eval['pred_relative_heading_levels'])}`",
            f"- Title layout score: {title_eval['title_layout_score']:.4f}",
            f"- Heading F1 score: {title_eval.get('heading_f1_score', 0.0):.4f}",
            f"- Level accuracy score: {title_eval.get('level_accuracy_score', 0.0):.4f}",
            f"- Order score: {title_eval.get('order_score', 0.0):.4f}",
            "- Main penalties:",
        ]
    )
    for issue in title_eval["issues"]:
        lines.append(f"  - {issue}")

    lines.extend(
        [
            "",
            "## Text Evaluation",
            f"- Text mode: {text_eval.get('text_mode', 'unknown')}",
            f"- Text score: {text_eval['text_score']:.4f}",
            f"- Body-only text score: {text_eval.get('body_only_text_score', text_eval['text_score']):.4f}",
            f"- Chart score used by text module: {text_eval.get('chart_score', 0.0):.4f}",
            f"- Average edit distance: {text_eval['average_edit_distance']:.4f}",
            f"- Matched / missing / extra blocks: {text_eval['matched_block_count']} / "
            f"{text_eval['missing_block_count']} / {text_eval['extra_block_count']}",
            f"- GT / Pred block counts: {text_eval['gt_block_count']} / {text_eval['pred_block_count']}",
            "",
            "### Worst Match Samples",
        ]
    )
    if text_eval["worst_matches"]:
        for idx, item in enumerate(text_eval["worst_matches"], start=1):
            lines.extend(
                [
                    f"{idx}. op={item['op']}, distance={item['distance']:.4f}, "
                    f"GT blocks {item['gt_start']}+{item['gt_count']}, "
                    f"Pred blocks {item['pred_start']}+{item['pred_count']}",
                    f"   - GT: {item['gt_preview'] or '(empty)'}",
                    f"   - Pred: {item['pred_preview'] or '(empty)'}",
                ]
            )
    else:
        lines.append("- No text mismatches.")

    lines.extend(
        [
            "",
            "## Notes",
            "- Table score compares extracted HTML and Markdown pipe tables after conversion to cell matrices.",
            "- Table matching is Pred-driven semantic one-to-one: structure and header/row-label keywords select the highest-confidence unused GT candidate.",
            "- Footprint aggregation weights each GT table by sqrt(expanded grid slots x normalized cell characters); unmatched GT footprint receives zero and unmatched Pred footprint enlarges the denominator.",
            "- Content-aware module weighting reserves the configured title-layout share, then splits the remaining score budget between tables and text using Gold semantic tokens plus one structural unit per logical table grid slot.",
            "- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.",
            "- A chart-embedded table may match only a Gold table marked as chart-table; once routed, that payload is removed from chart scoring to prevent duplicate credit.",
            "- Table pair score is 60% structure score and 40% content score; table content score uses exact normalized Levenshtein distance on complete flattened table text.",
            "- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.",
            "- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.",
            "- With score_charts=off, marked chart transcriptions are removed symmetrically before table extraction, heading layout, and body scoring.",
            "- No-value page headers and footers are removed from prediction Markdown only; GT Markdown is kept as the reference answer.",
            "- Current limitations: complex nested tables, heavily malformed HTML, and table semantic equivalence beyond cell text are only approximated.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse CLI arguments."""

    parser = argparse.ArgumentParser(description="Score financial Markdown parsing results.")
    parser.add_argument("--gt", required=True, help="Primary GT Markdown path.")
    parser.add_argument("--pred", required=True, help="Prediction Markdown path.")
    parser.add_argument("--gt-table-alt", help="Optional second table GT Markdown path.")
    parser.add_argument(
        "--table-gt-strategy",
        choices=["primary", "alt", "max"],
        default="max",
        help="primary/alt use one GT; max keeps the better GT pair for each Pred table.",
    )
    parser.add_argument("--md-out", help="Optional Markdown report output path.")
    parser.add_argument("--json-out", help="Optional JSON report output path.")
    parser.add_argument(
        "--remove-pred-header-footer",
        choices=["on", "off"],
        default="on",
        help="Remove no-value header/footer lines from prediction Markdown.",
    )
    parser.add_argument(
        "--normalize-images",
        choices=["on", "off"],
        default="on",
        help="Normalize image/flowchart/mermaid markers to ![].",
    )
    parser.add_argument(
        "--score-charts",
        choices=["on", "off"],
        default="on",
        help="Include informative chart transcriptions in body-text scoring.",
    )
    parser.add_argument(
        "--normalize-zh",
        choices=["t2s", "none"],
        default="t2s",
        help="Normalize Traditional Chinese to Simplified Chinese when OpenCC is available.",
    )
    parser.add_argument(
        "--normalize-footnotes",
        choices=["on", "off"],
        default="on",
        help="Remove common inline superscript/footnote markers from body text.",
    )
    parser.add_argument(
        "--normalize-punctuation",
        choices=["on", "off"],
        default="on",
        help="Normalize low-value punctuation variants in body text.",
    )
    parser.add_argument(
        "--normalize-formulas",
        choices=["on", "off"],
        default="on",
        help="Canonicalize presentation-only Markdown/LaTeX formula syntax while preserving mathematical tokens.",
    )
    parser.add_argument(
        "--table-structure-weight",
        type=float,
        default=0.60,
        help="Structure weight inside single table pair scoring.",
    )
    parser.add_argument(
        "--table-content-weight",
        type=float,
        default=0.40,
        help="Content weight inside single table pair scoring.",
    )
    parser.add_argument(
        "--table-aggregation",
        choices=["footprint", "uniform"],
        default="footprint",
        help=(
            "Aggregate per-table scores by parser-neutral GT footprint "
            "(default) or give every table equal weight."
        ),
    )
    parser.add_argument(
        "--module-weighting",
        choices=["content", "fixed"],
        default="content",
        help=(
            "Split the non-heading score budget by GT table/text information "
            "share (default) or use the legacy fixed 40/20/40 weights."
        ),
    )
    parser.add_argument(
        "--title-layout-weight",
        type=float,
        default=0.20,
        help="Reserved title-layout weight used by content-aware module weighting.",
    )
    return parser.parse_args(argv)


def _flag_on(value: str) -> bool:
    """Convert on/off CLI values to bool."""

    return value == "on"


def main(argv: Optional[Sequence[str]] = None) -> int:
    """CLI entry point."""

    args = parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if args.table_structure_weight < 0 or args.table_content_weight < 0:
        raise ValueError("Table weights must be non-negative.")
    if args.table_structure_weight + args.table_content_weight <= 0:
        raise ValueError("At least one table weight must be positive.")
    if not 0.0 <= args.title_layout_weight < 1.0:
        raise ValueError("Title layout weight must be in [0, 1).")

    config = ScoringConfig(
        remove_pred_header_footer=_flag_on(args.remove_pred_header_footer),
        normalize_images=_flag_on(args.normalize_images),
        score_charts=_flag_on(args.score_charts),
        normalize_zh=args.normalize_zh,
        normalize_footnotes=_flag_on(args.normalize_footnotes),
        normalize_punctuation=_flag_on(args.normalize_punctuation),
        normalize_formulas=_flag_on(args.normalize_formulas),
        table_structure_weight=args.table_structure_weight,
        table_content_weight=args.table_content_weight,
        table_aggregation=args.table_aggregation,
        module_weighting=args.module_weighting,
        title_layout_weight=args.title_layout_weight,
    )

    result = evaluate(
        gt_path=args.gt,
        pred_path=args.pred,
        gt_table_alt_path=args.gt_table_alt,
        table_gt_strategy=args.table_gt_strategy,
        config=config,
    )
    markdown_report = generate_markdown_report(result)

    if args.md_out:
        Path(args.md_out).write_text(markdown_report, encoding="utf-8")
    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(result, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    if not args.md_out and not args.json_out:
        print(markdown_report)
    else:
        print(
            "Final Score: {final:.4f} | Table: {table:.4f} | Title: {title:.4f} | Text: {text:.4f}".format(
                final=result["scores"]["final_score"],
                table=result["scores"]["table_score"],
                title=result["scores"]["title_layout_score"],
                text=result["scores"]["text_score"],
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
