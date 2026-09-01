#!/usr/bin/env python3
"""Adapter for the published MinerU 3.4.0 hybrid effort=high outputs."""

from __future__ import annotations

from collections import Counter

from common import (
    attach_mineru_chart_peripherals,
    normalize_images,
    normalize_mermaid,
    normalize_mineru_details,
    normalize_newlines,
    remove_generated_image_captions,
    remove_mineru_directory_payloads,
    remove_mineru_table_classification_tags,
    remove_repeated_page_noise,
    run_adapter_cli,
    strip_comments,
    unescape_mineru_markdown_punctuation,
    unwrap_inline_tags,
)

SYSTEM_ID = "mineru-3.4.0-hybrid-high"
ADAPTER_NAME = "normalize_mineru_hybrid.py"
RULES = [
    "unwrap MinerU details/summary containers while retaining text_image content and marking chart boundaries from MinerU summary types",
    "keep the figure title as text while attaching its adjacent image marker, source, and note lines to the MinerU-derived chart boundary",
    "retain explicit contents/list-of-figures headings but remove their directory entries, including partial entries and entries mis-promoted to headings",
    "undo MinerU backslash escapes for literal range, multiplication, list, underscore, and currency symbols outside tables while retaining LaTeX commands",
    "remove line-boundary Table_ or Tale_ classification fragments while retaining surrounding visible text and all table cells",
    "replace natural images, flowcharts, Mermaid blocks, and image paths with ![]",
    "remove generated decorative-image captions and presentation-only sup/sub wrappers",
    "remove duplicate running headers and isolated page numbers using prediction-only repetition",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = remove_mineru_directory_payloads(text, stats)
    text = normalize_mineru_details(text, stats)
    text = unescape_mineru_markdown_punctuation(text, stats)
    text = remove_mineru_table_classification_tags(text, stats)
    text = normalize_mermaid(text, stats)
    text = normalize_images(text, stats)
    text = attach_mineru_chart_peripherals(text, stats)
    text = remove_generated_image_captions(text, stats)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
