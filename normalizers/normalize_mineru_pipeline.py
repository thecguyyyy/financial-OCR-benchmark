#!/usr/bin/env python3
"""Adapter for the published MinerU 3.4.0 pipeline outputs."""

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
)

SYSTEM_ID = "mineru-3.4.0-pipeline"
ADAPTER_NAME = "normalize_mineru_pipeline.py"
RULES = [
    "replace Markdown/HTML image paths with ![]",
    "keep figure titles while removing their immediately adjacent image-only marker, source, and note residue",
    "unwrap presentation-only sup/sub tags while retaining their text",
    "remove parser comments, duplicate running headers, and isolated page numbers",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = normalize_images(text, stats)
    text = remove_image_only_chart_peripherals(text, stats)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
