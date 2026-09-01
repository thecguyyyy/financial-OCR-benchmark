#!/usr/bin/env python3
"""Adapter for PaddleOCR-VL-1.6 page-wise outputs."""

from __future__ import annotations

from collections import Counter

from common import (
    normalize_images,
    normalize_newlines,
    remove_image_only_chart_peripherals,
    remove_repeated_page_noise,
    run_adapter_cli,
    strip_comments,
    unwrap_inline_tags,
    unwrap_paddle_divs,
)

SYSTEM_ID = "paddleocr-vl-1.6-pagewise"
ADAPTER_NAME = "normalize_paddleocr_pagewise.py"
RULES = [
    "unwrap PaddleOCR alignment divs while retaining text",
    "replace image paths with ![]",
    "keep figure titles while removing adjacent image-only markers, sources, and notes",
    "unwrap presentation-only sup/sub tags and remove parser comments",
    "remove duplicate running headers and isolated page numbers; do not merge page-wise tables",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = unwrap_paddle_divs(text, stats)
    text = normalize_images(text, stats)
    text = remove_image_only_chart_peripherals(text, stats)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
