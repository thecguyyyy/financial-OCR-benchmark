#!/usr/bin/env python3
"""Shared, GT-independent utilities for parser-specific output adapters.

The helpers in this module deliberately know nothing about the PDF, document
identifier, ground truth, or benchmark score.  They only remove stable output
protocol artifacts while preserving document text, heading order, and table
boundaries.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmark_scorer import extract_heading_items, extract_tables  # noqa: E402


Adapter = Callable[[str, Counter[str]], str]

CHART_KINDS = {
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

DETAILS_RE = re.compile(
    r"<details\b[^>]*>\s*<summary\b[^>]*>(?P<summary>.*?)</summary>"
    r"(?P<body>.*?)</details>",
    re.IGNORECASE | re.DOTALL,
)
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^\n)]*\)")
REFERENCE_IMAGE_RE = re.compile(r"!\[[^\]]*\]\[[^\]]*\]")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*?/?>", re.IGNORECASE | re.DOTALL)
COORDINATE_IMAGE_RE = re.compile(r"<image\b[^>]*>.*?</image\s*>", re.IGNORECASE | re.DOTALL)
MERMAID_RE = re.compile(r"```+\s*mermaid\b.*?```+", re.IGNORECASE | re.DOTALL)
PAGEBREAK_RE = re.compile(r"^[ \t]*<pagebreak\b[^>]*/?>[ \t]*$", re.IGNORECASE | re.MULTILINE)
COMMENTED_COORDINATE_IMAGE_RE = re.compile(
    r"<!--\s*(?P<image><image\b[^>]*>.*?</image\s*>)\s*-->",
    re.IGNORECASE | re.DOTALL,
)
HTML_TABLE_BLOCK_RE = re.compile(r"<table\b.*?</table\s*>", re.IGNORECASE | re.DOTALL)
COMMENTED_COORDINATE_IMAGE_TABLE_RE = re.compile(
    r"(?P<image><!--\s*<image\b[^>]*>.*?</image\s*>\s*-->)"
    r"\s*(?P<table><table\b.*?</table\s*>)",
    re.IGNORECASE | re.DOTALL,
)
_SELF_DIRECTORY_LABEL_RE = re.compile(
    r"^\s*(?:#{1,6}\s*)?(?:图表目录|插图目录|图目录|表格目录)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
_SELF_DIRECTORY_FIRST_CELL_RE = re.compile(
    r"^\s*(?:图(?:表)?|表)\s*(?:\d+|[一二三四五六七八九十百]+)\s*[:：、.]?",
    re.IGNORECASE,
)
_SELF_HTML_ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr\s*>", re.IGNORECASE | re.DOTALL)
_SELF_HTML_CELL_RE = re.compile(
    r"<t[dh]\b[^>]*>(.*?)</t[dh]\s*>", re.IGNORECASE | re.DOTALL
)
_SELF_HTML_TAG_RE = re.compile(r"<[^>]+>", re.DOTALL)
_SELF_PROTECTED_TEXT_RE = re.compile(
    r"(<table\b.*?</table\s*>|\\\[.*?\\\]|\$\$.*?\$\$|\\\(.*?\\\)|`+.*?`+)",
    re.IGNORECASE | re.DOTALL,
)
_SELF_CJK_HIGHLIGHT_BRACE_RE = re.compile(
    r"\{([^{}\n]*[\u3400-\u9fff][^{}\n]*)\}"
)
_SELF_VISUAL_LIST_BULLET_RE = re.compile(
    r"^(?P<indent>\s*)[■□☑☐✓✔◆◇●○▪▫]\s*", re.MULTILINE
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")


def unwrap_commented_coordinate_images(text: str, stats: Counter[str]) -> str:
    """Retain self-developed-parser image objects hidden in HTML comments."""

    text, count = COMMENTED_COORDINATE_IMAGE_RE.subn(
        lambda match: f"\n{match.group('image')}\n", text
    )
    stats["commented_coordinate_images_unwrapped"] += count
    return text


def wrap_commented_coordinate_image_tables(text: str, stats: Counter[str]) -> str:
    """Mark a commented coordinate image plus its adjacent table as one chart.

    The self-developed parser uses HTML comments for raster regions in its
    industry-report output. When such an image is immediately followed by a
    table, both objects are two representations of the same figure rather than
    an ordinary business table. The wrapper retains the image object and table
    while exposing that relationship to the chart-aware scorer. Direct
    coordinate images are ignored because annual-report pages often place
    decorative icons before unrelated business tables.
    """

    def replace(match: re.Match[str]) -> str:
        stats["commented_image_table_charts_wrapped"] += 1
        return (
            '\n<chart data-type="image_table">\n'
            f"{match.group('image')}\n{match.group('table')}\n"
            "</chart>\n"
        )

    return COMMENTED_COORDINATE_IMAGE_TABLE_RE.sub(replace, text)


def _self_directory_table_rows(table: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for row_html in _SELF_HTML_ROW_RE.findall(table):
        cells: list[str] = []
        for cell_html in _SELF_HTML_CELL_RE.findall(row_html):
            cell_html = re.sub(r"<br\b[^>]*?/?>", " ", cell_html, flags=re.IGNORECASE)
            cell = html.unescape(_SELF_HTML_TAG_RE.sub("", cell_html))
            cells.append(re.sub(r"\s+", " ", cell).strip())
        if cells:
            rows.append(cells)
    return rows


def unwrap_self_directory_tables(text: str, stats: Counter[str]) -> str:
    """Convert layout tables inside an explicit figure directory to text.

    A table qualifies only when it follows an explicit figure/table-directory
    label, occurs before the next Markdown section heading, and at least 80%
    of its rows begin with a figure/table number. This keeps the directory text
    but prevents a presentational two-column list from entering the business-
    table denominator.
    """

    replacements: list[tuple[int, int, str, int]] = []
    for table_match in HTML_TABLE_BLOCK_RE.finditer(text):
        labels = list(_SELF_DIRECTORY_LABEL_RE.finditer(text, 0, table_match.start()))
        if not labels:
            continue
        label = labels[-1]
        between = text[label.end() : table_match.start()]
        if re.search(r"(?m)^\s*#{1,6}\s+\S", between):
            continue
        rows = _self_directory_table_rows(table_match.group(0))
        if not rows:
            continue
        directory_rows = sum(
            bool(row and _SELF_DIRECTORY_FIRST_CELL_RE.match(row[0])) for row in rows
        )
        if directory_rows / len(rows) < 0.80:
            continue
        rendered: list[str] = []
        for row in rows:
            if len(row) == 1:
                rendered.append(row[0])
            else:
                separator = "" if re.search(r"[:：、.]\s*$", row[0]) else " "
                rendered.append(row[0] + separator + " ".join(row[1:]))
        replacements.append(
            (table_match.start(), table_match.end(), "\n\n".join(rendered), len(rows))
        )

    for start, end, rendered, row_count in reversed(replacements):
        text = text[:start] + rendered + text[end:]
        stats["directory_layout_tables_unwrapped"] += 1
        stats["directory_layout_rows_preserved"] += row_count
    return text


def unwrap_self_highlight_braces(text: str, stats: Counter[str]) -> str:
    """Remove presentation-only braces around CJK emphasis outside math/tables."""

    def replace(match: re.Match[str]) -> str:
        prefix = match.string[: match.start()]
        # Preserve arguments of malformed or only partially delimited LaTeX,
        # such as ``\text{保险服务费用}``, as well as sub/superscripts.
        if re.search(r"\\[A-Za-z]+\s*$", prefix) or prefix.endswith(("_", "^")):
            return match.group(0)
        stats["cjk_highlight_braces_unwrapped"] += 1
        return match.group(1)

    parts = _SELF_PROTECTED_TEXT_RE.split(text)
    for index in range(0, len(parts), 2):
        parts[index] = _SELF_CJK_HIGHLIGHT_BRACE_RE.sub(replace, parts[index])
    return "".join(parts)


def normalize_self_visual_list_bullets(text: str, stats: Counter[str]) -> str:
    """Convert visual checkbox/square bullets at line start to Markdown lists."""

    # This convention belongs to the industry-report variant that also emits
    # coordinate images inside comments. In annual reports, square marks often
    # encode selected/unselected form values and must remain distinct.
    if not COMMENTED_COORDINATE_IMAGE_RE.search(text):
        return text
    text, count = _SELF_VISUAL_LIST_BULLET_RE.subn(r"\g<indent>- ", text)
    stats["visual_list_bullets_normalized"] += count
    return text


def normalize_serialized_table_linebreaks(text: str, stats: Counter[str]) -> str:
    """Turn the API's literal ``\\n`` cell separator into a real line break."""

    def replace_table(match: re.Match[str]) -> str:
        table = match.group(0)
        normalized, count = re.subn(r"\\n", "\n", table)
        stats["serialized_table_linebreaks_normalized"] += count
        return normalized

    return HTML_TABLE_BLOCK_RE.sub(replace_table, text)


def strip_comments(text: str, stats: Counter[str]) -> str:
    text, count = re.subn(r"<!--.*?-->", "", text, flags=re.DOTALL)
    stats["comments_removed"] += count
    return text


def unwrap_inline_tags(text: str, stats: Counter[str], tags: Iterable[str] = ("sup", "sub")) -> str:
    for tag in tags:
        pattern = re.compile(
            rf"<{tag}\b[^>]*>\s*(.*?)\s*</{tag}>", re.IGNORECASE | re.DOTALL
        )
        text, count = pattern.subn(lambda match: match.group(1).strip(), text)
        stats[f"{tag}_wrappers_removed"] += count
    return text


def normalize_images(text: str, stats: Counter[str], coordinate_xml: bool = False) -> str:
    if coordinate_xml:
        text, count = COORDINATE_IMAGE_RE.subn("\n![]\n", text)
        stats["coordinate_images_normalized"] += count
    text, md_count = MARKDOWN_IMAGE_RE.subn("![]", text)
    text, ref_count = REFERENCE_IMAGE_RE.subn("![]", text)
    text, html_count = HTML_IMAGE_RE.subn("\n![]\n", text)
    stats["markdown_images_normalized"] += md_count + ref_count
    stats["html_images_normalized"] += html_count
    return text


def remove_pagebreaks(text: str, stats: Counter[str]) -> str:
    text, count = PAGEBREAK_RE.subn("", text)
    stats["pagebreaks_removed"] += count
    return text


def normalize_mermaid(text: str, stats: Counter[str]) -> str:
    text, count = MERMAID_RE.subn("\n![]\n", text)
    stats["mermaid_blocks_normalized"] += count
    return text


def normalize_mineru_details(text: str, stats: Counter[str]) -> str:
    """Normalize MinerU containers while preserving informative chart boundaries.

    The ``chart`` wrapper is representation-only metadata derived exclusively
    from MinerU's own ``summary`` value.  Its body and every table matrix remain
    unchanged.  Keeping this boundary lets the shared scorer either compare or
    exclude charts without consulting a PDF, GT, document identifier, or score.
    """

    visual_kinds = {"natural_image", "flowchart", "figure", "image", "picture", "diagram", "visual"}

    def replace(match: re.Match[str]) -> str:
        summary = re.sub(r"[\s-]+", "_", html.unescape(match.group("summary")).strip().lower())
        body = match.group("body").strip()
        stats["details_wrappers_removed"] += 1
        has_mermaid = bool(
            re.search(
                r"```+\s*mermaid\b|^\s*(?:graph|flowchart)\s+(?:td|lr|rl|bt)\b",
                body,
                flags=re.IGNORECASE | re.MULTILINE,
            )
        )
        has_table = bool(
            re.search(r"<table\b", body, flags=re.IGNORECASE)
            or re.search(r"(?m)^\s*\|.*\|\s*$", body)
        )
        if summary in CHART_KINDS and (has_table or body):
            stats["informative_chart_boundaries_preserved"] += 1
            return f'\n<chart data-type="{summary}">\n{body}\n</chart>\n'
        if (summary in visual_kinds or has_mermaid) and not has_table:
            stats["visual_details_to_image_marker"] += 1
            return "\n![]\n"
        # text_image, chart and scatter blocks contain scoreable text/table data.
        stats["text_details_unwrapped"] += 1
        return f"\n{body}\n"

    previous = None
    while previous != text:
        previous = text
        text = DETAILS_RE.sub(replace, text)
    return text


_MINERU_CHART_TITLE_RE = re.compile(
    r"^\s*(?:#{1,6}\s*)?"
    r"(?:图(?:表)?\s*(?:\d+|[一二三四五六七八九十百]+)|figure\s*\d+|chart\s*\d+)"
    r"(?:\s*[:：、.\-]\s*|\s+).+\s*$",
    re.IGNORECASE,
)
_MINERU_CHART_SOURCE_RE = re.compile(
    r"^\s*(?:数据来源|资料来源|数据源|来源|source)\s*[:：]",
    re.IGNORECASE,
)
_MINERU_CHART_NOTE_RE = re.compile(
    r"^\s*(?:注|备注|说明)\s*[:：]",
    re.IGNORECASE,
)
_MINERU_CHART_NOTE_ITEM_RE = re.compile(
    r"^\s*(?:\d{1,2}|[①-⑳])\s*[)）.、:]",
    re.IGNORECASE,
)

_MINERU_DIRECTORY_HEADING_RE = re.compile(
    r"^\s*(?P<marks>#{1,6})\s*(?P<kind>内容目录|图表目录|插图目录|图目录|表格目录)\s*$",
    re.IGNORECASE,
)


def remove_mineru_directory_payloads(text: str, stats: Counter[str]) -> str:
    """Remove directory entries while retaining the directory headings.

    MinerU sometimes omits the terminal page number or promotes an entry to a
    Markdown heading.  Such partial entries evade the scorer's generic
    dot-leader filter and are then counted as body or heading errors.  This
    pass relies only on explicit ``内容目录``/``图表目录`` section headings:

    * a content directory ends at the following figure/table directory;
    * a figure/table directory ends at the next Markdown heading.

    The directory headings themselves are retained.  No entry text, page
    number, document identifier, PDF, or GT content is consulted.
    """

    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        match = _MINERU_DIRECTORY_HEADING_RE.match(lines[index])
        if not match:
            output.append(lines[index])
            index += 1
            continue

        output.append(lines[index])
        kind = match.group("kind")
        cursor = index + 1
        if kind == "内容目录":
            while cursor < len(lines):
                next_match = _MINERU_DIRECTORY_HEADING_RE.match(lines[cursor])
                if next_match and next_match.group("kind") != "内容目录":
                    break
                cursor += 1
        else:
            while cursor < len(lines) and not re.match(r"^\s*#{1,6}\s+", lines[cursor]):
                cursor += 1

        removed = lines[index + 1 : cursor]
        stats["directory_payload_lines_removed"] += sum(bool(line.strip()) for line in removed)
        stats["directory_sections_cleaned"] += 1
        output.append("")
        index = cursor
    return "\n".join(output)


_MINERU_MARKDOWN_ESCAPE_RE = re.compile(r"\\([~*+_$])")
_MINERU_TABLE_TAG_PREFIX_RE = re.compile(
    r"^\[(?:table|tale)_[A-Za-z]+\]?\s*", re.IGNORECASE
)
_MINERU_TABLE_TAG_SUFFIX_RE = re.compile(
    r"^\[([^\[\]\n]*?)(?:[:：])?(?:table|tale)_[A-Za-z]+\]?\s*$", re.IGNORECASE
)


def unescape_mineru_markdown_punctuation(text: str, stats: Counter[str]) -> str:
    """Undo MinerU escapes for literal Markdown punctuation outside tables.

    MinerU emits ranges and literal symbols with a backslash before ``~``,
    ``*``, ``+`` or ``$``.  The shared Markdown normalizer removes the symbol
    but would otherwise leave the backslash as false OCR content.  LaTeX
    commands and delimiters (such as escaped percent signs and parenthesis or
    bracket delimiters) are deliberately untouched, and table rows are skipped so table matrices remain byte-for-
    byte stable under adapter validation.
    """

    output: list[str] = []
    table_depth = 0
    for line in text.splitlines():
        lowered = line.lower()
        inside_html_table = table_depth > 0 or bool(re.search(r"<table\b", lowered))
        is_pipe_table_row = bool(re.match(r"^\s*\|.*\|\s*$", line))
        if not inside_html_table and not is_pipe_table_row:
            line, count = _MINERU_MARKDOWN_ESCAPE_RE.subn(r"\1", line)
            stats["markdown_punctuation_escapes_removed"] += count
        output.append(line)
        table_depth += len(re.findall(r"<table\b", lowered))
        table_depth -= len(re.findall(r"</table\s*>", lowered))
    return "\n".join(output)


def remove_mineru_table_classification_tags(text: str, stats: Counter[str]) -> str:
    """Remove MinerU ``Table_*`` classification fragments outside tables.

    Hybrid output can fuse an internal class label into visible text, for
    example ``[投资要点Table_S`` or ``[Table_Rep相关研究``.  The rule removes
    only the ASCII ``Table_``/``Tale_`` fragment at a line boundary and keeps
    every surrounding Chinese character.  Actual HTML and pipe-table rows are
    skipped so cell matrices cannot change.
    """

    output: list[str] = []
    table_depth = 0
    for line in text.splitlines():
        lowered = line.lower()
        inside_html_table = table_depth > 0 or bool(re.search(r"<table\b", lowered))
        is_pipe_table_row = bool(re.match(r"^\s*\|.*\|\s*$", line))
        if not inside_html_table and not is_pipe_table_row:
            heading = re.match(r"^(?P<prefix>\s*#{1,6}\s+)(?P<body>.*)$", line)
            prefix = heading.group("prefix") if heading else ""
            body = heading.group("body") if heading else line
            updated, prefix_count = _MINERU_TABLE_TAG_PREFIX_RE.subn("", body)
            if prefix_count == 0:
                updated, suffix_count = _MINERU_TABLE_TAG_SUFFIX_RE.subn(r"\1", body)
            else:
                suffix_count = 0
            if prefix_count or suffix_count:
                line = prefix + updated.rstrip("：:")
                stats["table_classification_tags_removed"] += prefix_count + suffix_count
        output.append(line)
        table_depth += len(re.findall(r"<table\b", lowered))
        table_depth -= len(re.findall(r"</table\s*>", lowered))
    return "\n".join(output)


def attach_mineru_chart_peripherals(text: str, stats: Counter[str]) -> str:
    """Move stable MinerU chart peripherals inside their ``chart`` block.

    MinerU serializes an informative visual as four adjacent pieces: a figure
    title, an image marker, a ``details/summary`` transcription, and source or
    note lines.  ``normalize_mineru_details`` already converts the transcription
    to ``<chart>``.  This prediction-only pass keeps the human-readable figure
    title in normal text, while attaching the immediately adjacent image marker,
    source, and note lines to the chart boundary.  Chart-off scoring can then
    remove the complete visual payload without dropping its title.

    Only syntax next to an existing MinerU-derived ``<chart>`` is considered;
    ordinary paragraphs, standalone images, and document-specific words are
    never used as signals.
    """

    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        if not re.match(r"^\s*<chart\b[^>]*>\s*$", lines[index], flags=re.IGNORECASE):
            output.append(lines[index])
            index += 1
            continue

        close_index = index + 1
        while close_index < len(lines) and not re.match(
            r"^\s*</chart\s*>\s*$", lines[close_index], flags=re.IGNORECASE
        ):
            close_index += 1
        if close_index >= len(lines):
            output.extend(lines[index:])
            break

        # Inspect only the immediately adjacent nonblank prefix.  An image
        # marker directly adjacent to a MinerU-derived chart is the raster
        # representation of that same chart, even when a cover chart uses an
        # unnumbered title such as "行业走势".  A title is recognized only so
        # it can be kept outside the chart boundary.
        prefix_start = len(output)
        cursor = len(output) - 1
        while cursor >= 0 and not output[cursor].strip():
            cursor -= 1
        image_index: int | None = None
        if cursor >= 0 and output[cursor].strip() == "![]":
            image_index = cursor
            cursor -= 1
            while cursor >= 0 and not output[cursor].strip():
                cursor -= 1
        title_index: int | None = None
        if cursor >= 0 and _MINERU_CHART_TITLE_RE.match(output[cursor]):
            title_index = cursor
        if image_index is not None:
            prefix_start = image_index

        prefix = output[prefix_start:]
        if prefix:
            del output[prefix_start:]
            if title_index is not None:
                stats["chart_titles_recognized"] += 1
            if image_index is not None:
                stats["chart_image_markers_attached"] += 1

        suffix: list[str] = []
        suffix_cursor = close_index + 1
        pending_blanks: list[str] = []
        saw_note = False
        while suffix_cursor < len(lines):
            candidate = lines[suffix_cursor]
            if not candidate.strip():
                pending_blanks.append(candidate)
                suffix_cursor += 1
                continue
            is_source = bool(_MINERU_CHART_SOURCE_RE.match(candidate))
            is_note = bool(_MINERU_CHART_NOTE_RE.match(candidate))
            # Numbered note continuations must be physically contiguous with
            # the note header.  A blank line terminates the note block; this
            # prevents a following numbered body paragraph from being absorbed.
            is_note_item = (
                saw_note
                and not pending_blanks
                and bool(_MINERU_CHART_NOTE_ITEM_RE.match(candidate))
            )
            if not (is_source or is_note or is_note_item):
                break
            suffix.extend(pending_blanks)
            pending_blanks = []
            suffix.append(candidate)
            suffix_cursor += 1
            saw_note = saw_note or is_note
            if is_source:
                stats["chart_source_lines_attached"] += 1
            else:
                stats["chart_note_lines_attached"] += 1

        opening = lines[index]
        body = lines[index + 1 : close_index]
        closing = lines[close_index]
        output.append(opening)
        output.extend(prefix)
        output.extend(body)
        output.extend(suffix)
        output.append(closing)
        index = suffix_cursor if suffix else close_index + 1

    return "\n".join(output)


def remove_image_only_chart_peripherals(text: str, stats: Counter[str]) -> str:
    """Remove image/source protocol residue for figures without a data block.

    Pipeline output has no ``details/summary`` transcription to establish a
    scoreable chart payload.  The only safe local signature is therefore a
    figure-title line immediately followed by the normalized ``![]`` marker.
    The title is retained; only that marker and its adjacent source/note lines
    are removed.  No figure number, document id, PDF, or GT content is used.
    """

    lines = text.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        title = lines[index]
        if not _MINERU_CHART_TITLE_RE.match(title):
            output.append(title)
            index += 1
            continue

        marker_index = index + 1
        while marker_index < len(lines) and not lines[marker_index].strip():
            marker_index += 1
        if marker_index >= len(lines) or lines[marker_index].strip() != "![]":
            output.append(title)
            index += 1
            continue

        output.append(title)
        cursor = marker_index
        # A single caption can precede two side-by-side figures.  Consume every
        # immediately adjacent image/source group in the same pass so the
        # transformation remains idempotent.
        while cursor < len(lines) and lines[cursor].strip() == "![]":
            stats["image_only_chart_markers_removed"] += 1
            cursor += 1
            pending_blanks: list[str] = []
            saw_note = False
            while cursor < len(lines):
                candidate = lines[cursor]
                if not candidate.strip():
                    pending_blanks.append(candidate)
                    cursor += 1
                    continue
                is_source = bool(_MINERU_CHART_SOURCE_RE.match(candidate))
                is_note = bool(_MINERU_CHART_NOTE_RE.match(candidate))
                is_note_item = (
                    saw_note
                    and not pending_blanks
                    and bool(_MINERU_CHART_NOTE_ITEM_RE.match(candidate))
                )
                if not (is_source or is_note or is_note_item):
                    break
                pending_blanks = []
                cursor += 1
                saw_note = saw_note or is_note
                if is_source:
                    stats["image_only_chart_source_lines_removed"] += 1
                else:
                    stats["image_only_chart_note_lines_removed"] += 1

        output.append("")
        index = cursor
    return "\n".join(output)


def unwrap_paddle_divs(text: str, stats: Counter[str]) -> str:
    """Remove presentation-only PaddleOCR div wrappers and retain their body."""

    pattern = re.compile(r"<div\b[^>]*>(.*?)</div>", re.IGNORECASE | re.DOTALL)
    previous = None
    while previous != text:
        previous = text

        def replace(match: re.Match[str]) -> str:
            stats["div_wrappers_removed"] += 1
            return f"\n{match.group(1).strip()}\n"

        text = pattern.sub(replace, text)
    return text


def remove_generated_image_captions(text: str, stats: Counter[str]) -> str:
    """Remove VLM-authored English descriptions of decorative natural images."""

    starts = (
        "illustration of ",
        "an illustration of ",
        "image of ",
        "an image of ",
        "a photo of ",
        "the image shows ",
        "watercolor-style ",
    )
    markers = (
        "no text or symbols",
        "cartoon character",
        "rendered in warm yellow tones",
        "rendered in monochromatic yellow tones",
    )
    kept: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        lowered = stripped.lower()
        is_caption = (
            len(stripped) <= 260
            and not re.search(r"[\u3400-\u9fff]", stripped)
            and lowered.startswith(starts)
            and any(marker in lowered for marker in markers)
        )
        if is_caption:
            stats["generated_image_captions_removed"] += 1
        else:
            kept.append(line)
    return "\n".join(kept)


def _line_key(line: str) -> str:
    content = re.sub(r"^\s*#{1,6}\s+", "", line.strip())
    return re.sub(r"\s+", "", content).lower()


def _is_standalone_page_number(line: str) -> bool:
    compact = re.sub(r"\s+", "", line.strip()).lower()
    return bool(
        re.fullmatch(r"-?\d{1,4}-?", compact)
        or re.fullmatch(r"(?:page)?\d{1,4}(?:of|/)\d{1,4}", compact)
        or re.fullmatch(r"第\d{1,4}页(?:/共?\d{1,4}页?)?", compact)
    )


def _looks_like_running_header(line: str) -> bool:
    key = _line_key(line)
    if not key or len(key) > 90:
        return False
    report_terms = (
        "年度报告", "半年度报告", "中期报告", "季度报告", "年度報告", "中期報告",
        "annualreport", "interimreport",
    )
    company_endings = (
        "股份有限公司", "控股有限公司", "有限公司", "limited", "holdingslimited", "corporation",
    )
    return any(term in key for term in report_terms) or any(key.endswith(term) for term in company_endings)


def _page_boundary_heading_counter(text: str) -> Counter[tuple[int, str]]:
    """Find exact headings repeatedly emitted at the start of PDF pages.

    A candidate must occur within the first five visible lines of at least
    three page segments. Coordinate-image protocol lines and one-line HTML
    tables do not consume the five-line window. One occurrence is retained,
    so a genuine section heading is never erased completely.
    """

    pages = PAGEBREAK_RE.split(normalize_newlines(text))
    page_hits: dict[tuple[int, str], set[int]] = {}
    total_counts: Counter[tuple[int, str]] = Counter()
    for page_index, page in enumerate(pages):
        visible = 0
        seen_on_page: set[tuple[int, str]] = set()
        for line in page.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if (
                stripped == "![]"
                or COORDINATE_IMAGE_RE.fullmatch(stripped)
                or COMMENTED_COORDINATE_IMAGE_RE.fullmatch(stripped)
                or re.match(r"^</?(?:table|tr|td|th)\b", stripped, flags=re.IGNORECASE)
            ):
                continue
            visible += 1
            heading = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
            if heading and visible <= 5:
                item = (
                    len(heading.group(1)),
                    re.sub(r"\s+", " ", html.unescape(heading.group(2))).strip(),
                )
                seen_on_page.add(item)
                total_counts[item] += 1
            if visible >= 5:
                break
        for item in seen_on_page:
            page_hits.setdefault(item, set()).add(page_index)

    return Counter(
        {
            item: total_counts[item] - 1
            for item, hit_pages in page_hits.items()
            if len(hit_pages) >= 3 and total_counts[item] >= 3
        }
    )


def remove_repeated_page_boundary_headings(text: str, stats: Counter[str]) -> str:
    """Keep the first copy of repeated page-start headings and drop the rest."""

    removable = _page_boundary_heading_counter(text)
    if not removable:
        return text
    seen: Counter[tuple[int, str]] = Counter()
    output: list[str] = []
    for line in text.splitlines():
        heading = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
        if not heading:
            output.append(line)
            continue
        item = (
            len(heading.group(1)),
            re.sub(r"\s+", " ", html.unescape(heading.group(2))).strip(),
        )
        if item in removable:
            seen[item] += 1
            if seen[item] > 1 and removable[item] > 0:
                removable[item] -= 1
                stats["duplicate_page_boundary_headings_removed"] += 1
                continue
        output.append(line)
    return "\n".join(output)


def remove_repeated_page_noise(text: str, stats: Counter[str]) -> str:
    """Remove page numbers and duplicate running headers using prediction only.

    One occurrence of a repeated report/company line is retained so a genuine
    cover title is never erased.  No GT text or document identifier is used.
    """

    lines = text.splitlines()
    eligible: list[bool] = []
    keys: list[str] = []
    table_depth = 0
    counts: Counter[str] = Counter()
    for line in lines:
        lowered = line.lower()
        inside_table = table_depth > 0 or "<table" in lowered
        table_depth += len(re.findall(r"<table\b", lowered))
        table_depth -= len(re.findall(r"</table\s*>", lowered))
        candidate = not inside_table and _looks_like_running_header(line)
        key = _line_key(line)
        eligible.append(candidate)
        keys.append(key)
        if candidate:
            counts[key] += 1

    seen: Counter[str] = Counter()
    kept: list[str] = []
    for line, candidate, key in zip(lines, eligible, keys):
        if _is_standalone_page_number(line):
            stats["standalone_page_numbers_removed"] += 1
            continue
        if candidate and counts[key] >= 2:
            seen[key] += 1
            if seen[key] > 1:
                stats["duplicate_running_headers_removed"] += 1
                continue
        kept.append(line)
    return "\n".join(kept)


def finalize_markdown(text: str) -> str:
    text = normalize_newlines(text)
    lines = [re.sub(r"[ \t]+$", "", line) for line in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"(?:^|\n)[ \t]*!\[\][ \t]*(?:\n[ \t]*)+(?=!\[\][ \t]*(?:\n|$))", "\n", text)
    text = re.sub(r"(?:!\[\]\s*){2,}", "![]\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def _validation_image_only(text: str) -> str:
    text = COORDINATE_IMAGE_RE.sub("![]", text)
    text = MARKDOWN_IMAGE_RE.sub("![]", text)
    text = REFERENCE_IMAGE_RE.sub("![]", text)
    text = HTML_IMAGE_RE.sub("![]", text)
    return text


def _canonical_validation_cell(cell: str) -> str:
    """Ignore presentation-only cell whitespace and canonical image spacing."""

    cell = cell.replace(r"\n", "\n")
    cell = re.sub(r"\s*!\[\]\s*", "![]", cell)
    return re.sub(r"\s+", "", cell).strip()


def _canonical_validation_heading(item: object) -> tuple[int, str]:
    level = int(getattr(item, "level"))
    text = str(getattr(item, "text"))
    text = _validation_image_only(text)
    text = re.sub(r"</?(?:sup|sub)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = _MINERU_MARKDOWN_ESCAPE_RE.sub(r"\1", text)
    text = _MINERU_TABLE_TAG_PREFIX_RE.sub("", text)
    text = _MINERU_TABLE_TAG_SUFFIX_RE.sub(r"\1", text).rstrip("：:")
    text = _SELF_CJK_HIGHLIGHT_BRACE_RE.sub(r"\1", text)
    text = re.sub(r"^[■□☑☐✓✔◆◇●○▪▫]\s*", "", text)
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return level, text


def _directory_payload_heading_counter(text: str) -> Counter[tuple[int, str]]:
    """Return headings that occur inside explicit MinerU directory payloads."""

    cleaned = remove_mineru_directory_payloads(text, Counter())
    original = Counter(_canonical_validation_heading(item) for item in extract_heading_items(text))
    retained = Counter(_canonical_validation_heading(item) for item in extract_heading_items(cleaned))
    original.subtract(retained)
    return Counter({item: count for item, count in original.items() if count > 0})


def validate_transformation(source: str, normalized: str, adapter: Adapter) -> dict[str, object]:
    """Check table boundaries/content, heading sequence, and idempotence."""

    source_for_tables = unwrap_self_directory_tables(source, Counter())
    output_for_tables = unwrap_self_directory_tables(normalized, Counter())
    source_tables, _ = extract_tables(_validation_image_only(source_for_tables))
    output_tables, _ = extract_tables(_validation_image_only(output_for_tables))
    if len(source_tables) != len(output_tables):
        raise ValueError(f"table count changed: {len(source_tables)} -> {len(output_tables)}")
    for index, (before, after) in enumerate(zip(source_tables, output_tables)):
        before_matrix = [
            [_canonical_validation_cell(cell) for cell in row] for row in before.matrix
        ]
        after_matrix = [
            [_canonical_validation_cell(cell) for cell in row] for row in after.matrix
        ]
        if before_matrix != after_matrix:
            raise ValueError(f"table matrix changed at index {index}")

    source_headings = [
        _canonical_validation_heading(item) for item in extract_heading_items(source)
    ]
    output_headings = [
        _canonical_validation_heading(item) for item in extract_heading_items(normalized)
    ]
    output_index = 0
    removed_artifact_headings = 0
    directory_artifact_headings = _directory_payload_heading_counter(source)
    page_boundary_artifact_headings = _page_boundary_heading_counter(source)
    for source_heading in source_headings:
        if output_index < len(output_headings) and source_heading == output_headings[output_index]:
            output_index += 1
            continue
        if _looks_like_running_header(f"# {source_heading[1]}"):
            removed_artifact_headings += 1
            continue
        if directory_artifact_headings[source_heading] > 0:
            directory_artifact_headings[source_heading] -= 1
            removed_artifact_headings += 1
            continue
        if page_boundary_artifact_headings[source_heading] > 0:
            page_boundary_artifact_headings[source_heading] -= 1
            removed_artifact_headings += 1
            continue
        raise ValueError(f"non-artifact heading changed or removed: {source_heading!r}")
    if output_index != len(output_headings):
        raise ValueError("adapter added or altered a heading")

    second_pass = finalize_markdown(adapter(normalized, Counter()))
    if second_pass != normalized:
        raise ValueError("adapter is not idempotent")
    return {
        "table_count": len(output_tables),
        "heading_count": len(output_headings),
        "artifact_headings_removed": removed_artifact_headings,
        "table_matrices_preserved": True,
        "heading_sequence_preserved": True,
        "idempotent": True,
    }


def normalize_directory(
    input_dir: Path,
    output_dir: Path,
    adapter: Adapter,
    adapter_name: str,
    system_id: str,
    rules: list[str],
) -> dict[str, object]:
    input_dir = input_dir.resolve()
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    files: list[dict[str, object]] = []
    totals: Counter[str] = Counter()

    document_ids = tuple(
        sorted(
            path.stem
            for path in input_dir.glob("*.md")
            if re.fullmatch(r"\d{3}", path.stem)
        )
    )
    if not document_ids:
        raise FileNotFoundError(f"no canonical NNN.md predictions found in: {input_dir}")

    for doc_id in document_ids:
        source_path = input_dir / f"{doc_id}.md"
        if not source_path.is_file():
            raise FileNotFoundError(f"missing canonical prediction: {source_path}")
        source = normalize_newlines(source_path.read_text(encoding="utf-8-sig"))
        stats: Counter[str] = Counter()
        normalized = finalize_markdown(adapter(source, stats))
        validation = validate_transformation(source, normalized, adapter)
        output_path = output_dir / f"{doc_id}.md"
        output_path.write_text(normalized, encoding="utf-8", newline="\n")
        totals.update(stats)
        files.append(
            {
                "id": doc_id,
                "source": f"predictions/{system_id}/{doc_id}.md",
                "output": f"normalized_predictions/{system_id}/{doc_id}.md",
                "source_sha256": sha256_text(source),
                "output_sha256": sha256_text(normalized),
                "changes": dict(sorted(stats.items())),
                "validation": validation,
            }
        )
        print(
            f"NORMALIZED {system_id}/{doc_id}.md "
            f"tables={validation['table_count']} headings={validation['heading_count']}",
            flush=True,
        )

    manifest: dict[str, object] = {
        "system": system_id,
        "adapter": adapter_name,
        "document_ids": list(document_ids),
        "constraints": {
            "uses_ground_truth": False,
            "uses_pdf": False,
            "uses_document_id_rules": False,
            "merges_or_splits_tables": False,
            "reorders_content": False,
        },
        "rules": rules,
        "totals": dict(sorted(totals.items())),
        "files": files,
    }
    (output_dir / "normalization_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    return manifest


def run_adapter_cli(
    adapter: Adapter,
    adapter_name: str,
    system_id: str,
    rules: list[str],
) -> int:
    parser = argparse.ArgumentParser(
        description=f"Normalize {system_id} output without reading GT or PDF files."
    )
    parser.add_argument(
        "--input-dir", type=Path, default=ROOT / "predictions" / system_id
    )
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "normalized_predictions" / system_id
    )
    args = parser.parse_args()
    normalize_directory(args.input_dir, args.output_dir, adapter, adapter_name, system_id, rules)
    return 0
