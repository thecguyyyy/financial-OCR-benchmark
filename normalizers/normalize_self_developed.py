#!/usr/bin/env python3
"""Adapter for the published self-developed parser outputs."""

from __future__ import annotations

from collections import Counter

from common import (
    normalize_images,
    normalize_newlines,
    normalize_serialized_table_linebreaks,
    normalize_self_visual_list_bullets,
    remove_image_only_chart_peripherals,
    remove_pagebreaks,
    remove_repeated_page_boundary_headings,
    remove_repeated_page_noise,
    run_adapter_cli,
    strip_comments,
    unwrap_commented_coordinate_images,
    unwrap_self_directory_tables,
    unwrap_self_highlight_braces,
    unwrap_inline_tags,
    wrap_commented_coordinate_image_tables,
)

SYSTEM_ID = "self-developed-parser"
ADAPTER_NAME = "normalize_self_developed.py"
RULES = [
    "mark a commented coordinate image immediately followed by a table as one chart object while retaining both representations",
    "unwrap coordinate-image objects hidden inside HTML comments before normalizing their coordinates",
    "remove pagebreak control tags",
    "replace image coordinate XML with ![] so page/x/y/w/h values cannot enter text scoring",
    "convert literal \\n separators inside HTML table cells to real line breaks",
    "keep the first copy and remove repeated Markdown headings emitted at the start of at least three pages",
    "remove image/source/note protocol residue only when a numbered figure title is immediately followed by an image marker",
    "convert figure-directory layout tables back to text while retaining every directory row",
    "unwrap presentation-only braces around CJK emphasis outside formulas and tables",
    "convert visual checkbox/square bullets at line start to Markdown list markers",
    "unwrap presentation-only sup/sub tags while retaining their text",
    "remove parser comments, duplicate running headers, and isolated page numbers",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = normalize_self_visual_list_bullets(text, stats)
    text = wrap_commented_coordinate_image_tables(text, stats)
    text = unwrap_commented_coordinate_images(text, stats)
    text = normalize_serialized_table_linebreaks(text, stats)
    text = remove_repeated_page_boundary_headings(text, stats)
    text = remove_pagebreaks(text, stats)
    text = normalize_images(text, stats, coordinate_xml=True)
    text = remove_image_only_chart_peripherals(text, stats)
    text = unwrap_self_directory_tables(text, stats)
    text = unwrap_self_highlight_braces(text, stats)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
