#!/usr/bin/env python
"""Score financial announcement Markdown parsing results.

The scorer compares a prediction Markdown file with a ground-truth Markdown
file. It evaluates three modules only: tables, heading layout, and text.
Formula scoring is intentionally out of scope.
"""

from __future__ import annotations

import argparse
import difflib
import html
import json
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

    remove_pred_header_footer: bool = False
    normalize_images: bool = True
    normalize_zh: str = "t2s"
    normalize_footnotes: bool = True
    normalize_punctuation: bool = True
    table_structure_weight: float = 0.60
    table_content_weight: float = 0.40


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
    if len(a_norm) * len(b_norm) <= 4_000_000:
        return min(1.0, levenshtein_distance(a_norm, b_norm) / denom)
    return min(1.0, segmented_edit_distance_preserve_newlines(a_norm, b_norm) / denom)


def _diff_opcode_cost(a_text: str, b_text: str) -> int:
    """Estimate edit cost for a large changed block without dropping newlines."""

    if not a_text:
        return len(b_text)
    if not b_text:
        return len(a_text)
    if len(a_text) * len(b_text) <= 4_000_000:
        return levenshtein_distance(a_text, b_text)

    cost = 0
    matcher = difflib.SequenceMatcher(None, a_text, b_text, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if tag == "delete":
            cost += i2 - i1
        elif tag == "insert":
            cost += j2 - j1
        else:
            cost += max(i2 - i1, j2 - j1)
    return cost


def segmented_edit_distance_preserve_newlines(a_norm: str, b_norm: str) -> int:
    """Compute edit cost for large body text using line opcodes plus char costs."""

    a_lines = a_norm.splitlines(keepends=True)
    b_lines = b_norm.splitlines(keepends=True)
    matcher = difflib.SequenceMatcher(None, a_lines, b_lines, autojunk=False)
    distance = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        a_chunk = "".join(a_lines[i1:i2])
        b_chunk = "".join(b_lines[j1:j2])
        if tag == "delete":
            distance += len(a_chunk)
        elif tag == "insert":
            distance += len(b_chunk)
        else:
            distance += _diff_opcode_cost(a_chunk, b_chunk)
    return distance


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
    if len(a_norm) * len(b_norm) <= 200_000:
        return min(1.0, levenshtein_distance(a_norm, b_norm) / denom)
    return min(1.0, segmented_edit_distance_preserve_newlines(a_norm, b_norm) / denom)


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


def score_tables_per_pred_max(
    primary_gt_tables: Sequence[TableItem],
    alt_gt_tables: Sequence[TableItem],
    pred_tables: Sequence[TableItem],
    primary_pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
    alt_pair_cache: Optional[Dict[Tuple[int, int], Dict[str, Any]]] = None,
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
            "reference_table_count": 0,
            "final_table_score": 100.0,
            "matches": [],
        }

    primary_matches = {
        item["pred_position"]: item
        for item in match_pred_tables(primary_gt_tables, pred_tables, primary_pair_cache)
    }
    alt_matches = {
        item["pred_position"]: item
        for item in match_pred_tables(alt_gt_tables, pred_tables, alt_pair_cache)
    }
    matches: List[Dict[str, Any]] = []
    primary_selected_count = 0
    alt_selected_count = 0

    for pred_idx in range(len(pred_tables)):
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
    denominator = max(len(pred_tables), reference_table_count, 1)
    matched_count = len(matches)
    content_score = sum(item["table_content_score"] for item in matches) / denominator
    structure_score = sum(item["table_structure_score"] for item in matches) / denominator
    matrix_score = sum(item["table_pair_score"] for item in matches) / denominator

    return {
        "table_content_score": round_float(clamp_score(content_score)),
        "table_structure_score": round_float(clamp_score(structure_score)),
        "table_matrix_score": round_float(clamp_score(matrix_score)),
        "table_alignment_strategy": "per_table_best_of_primary_alt_one_to_one",
        "matched_table_count": matched_count,
        "missing_table_count": max(reference_table_count - matched_count, 0),
        "extra_table_count": len(pred_tables) - matched_count,
        "gt_table_count": reference_table_count,
        "pred_table_count": len(pred_tables),
        "primary_gt_table_count": len(primary_gt_tables),
        "alt_gt_table_count": len(alt_gt_tables),
        "reference_table_count": reference_table_count,
        "primary_selected_pair_count": primary_selected_count,
        "alt_selected_pair_count": alt_selected_count,
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
    gt_tables, gt_table_spans = extract_tables(gt_md)
    pred_tables, pred_table_spans = extract_tables(pred_md)

    alt_tables: Optional[List[TableItem]] = None
    alt_score: Optional[Dict[str, Any]] = None
    if gt_table_alt_path:
        alt_md = read_markdown(gt_table_alt_path)
        alt_tables, _ = extract_tables(alt_md)

    primary_pair_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
    alt_pair_cache: Dict[Tuple[int, int], Dict[str, Any]] = {}
    primary_table_score = score_tables(gt_tables, pred_tables, primary_pair_cache)
    if alt_tables is not None:
        alt_score = score_tables(alt_tables, pred_tables, alt_pair_cache)
    if table_gt_strategy == "max" and alt_tables is not None:
        selected_table_name = "per_table_max"
        selected_table_score = score_tables_per_pred_max(
            gt_tables,
            alt_tables,
            pred_tables,
            # score_tables() caches pairs as (gt_index, pred_index), while the
            # pred-centric matcher caches them as (pred_index, gt_index).
            # Never share those caches: the tuple shapes are identical and
            # would silently return a score for the reversed table pair.
            {},
            {},
        )
    else:
        selected_table_name, selected_table_score = select_table_score(
            primary_table_score, alt_score, table_gt_strategy
        )

    gt_without_tables = remove_tables(gt_md, gt_table_spans)
    pred_without_tables = remove_tables(pred_md, pred_table_spans)
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
    text_score = score_text(gt_text_for_scoring, pred_text_for_scoring)

    final_score = (
        selected_table_score["final_table_score"] * WEIGHTS["table"]
        + title_score["title_layout_score"] * WEIGHTS["title_layout"]
        + text_score["text_score"] * WEIGHTS["text"]
    )

    return {
        "inputs": {
            "gt": str(gt_path),
            "pred": str(pred_path),
            "gt_table_alt": str(gt_table_alt_path) if gt_table_alt_path else None,
            "table_gt_strategy": table_gt_strategy,
        },
        "pred_cleanup": {
            "mode": (
                "prediction_only_header_footer_cleanup"
                if CURRENT_CONFIG.remove_pred_header_footer
                else "disabled_after_explicit_adapter"
            ),
            "removed_line_count": pred_cleanup.removed_line_count,
            "removed_line_examples": pred_cleanup.removed_line_examples,
        },
        "weights": WEIGHTS,
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
    config = result.get("config", {})

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
            "- Table: 40%",
            "- Title Layout: 20%",
            "- Text: 40%",
            "",
            "## Configuration",
            f"- Remove pred header/footer: {config.get('remove_pred_header_footer', True)}",
            f"- Normalize images: {config.get('normalize_images', True)}",
            f"- Normalize Chinese variants: {config.get('normalize_zh', 't2s')}",
            f"- Normalize footnotes: {config.get('normalize_footnotes', True)}",
            f"- Normalize punctuation: {config.get('normalize_punctuation', True)}",
            f"- Table pair weights: structure={config.get('table_structure_weight', 0.60)}, "
            f"content={config.get('table_content_weight', 0.40)}",
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
            "",
            "### Table Matches",
        ]
    )
    if selected_table["matches"]:
        for match in selected_table["matches"][:30]:
            lines.append(
                "- {variant} GT table {gt_index} -> Pred table {pred_index}: pair={pair:.4f}, "
                "structure={structure:.4f}, content={content:.4f}, "
                "keywords={keywords:.4f}, match={match_score:.4f}, "
                "GT shape={gt_shape}, Pred shape={pred_shape}".format(
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
            "- With primary or alt strategy, table matching is GT-driven one-to-one: each GT table chooses one best unused Pred table.",
            "- With max and two GT files, each predicted table keeps the higher pair score from the two independently one-to-one-matched GT variants.",
            "- Table pair score is 60% structure score and 40% content score; table content score uses normalized edit distance on flattened table text.",
            "- Title layout score uses heading text only for anchor alignment, then combines heading F1, relative-level accuracy, and order coverage.",
            "- Text score removes tables, keeps heading words, preserves newlines, and scores the full body as one character sequence.",
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
        default="off",
        help="Legacy/debug option; standard scoring keeps this off after the explicit adapter.",
    )
    parser.add_argument(
        "--normalize-images",
        choices=["on", "off"],
        default="on",
        help="Normalize image/flowchart/mermaid markers to ![].",
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

    config = ScoringConfig(
        remove_pred_header_footer=_flag_on(args.remove_pred_header_footer),
        normalize_images=_flag_on(args.normalize_images),
        normalize_zh=args.normalize_zh,
        normalize_footnotes=_flag_on(args.normalize_footnotes),
        normalize_punctuation=_flag_on(args.normalize_punctuation),
        table_structure_weight=args.table_structure_weight,
        table_content_weight=args.table_content_weight,
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
