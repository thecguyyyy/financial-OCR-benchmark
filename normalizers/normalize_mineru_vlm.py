#!/usr/bin/env python3
"""Adapter for the published MinerU 3.4.4 VLM outputs."""

from __future__ import annotations

from collections import Counter

from common import (
    normalize_images,
    normalize_mermaid,
    normalize_mineru_details,
    normalize_newlines,
    remove_generated_image_captions,
    remove_repeated_page_noise,
    run_adapter_cli,
    strip_comments,
    unwrap_inline_tags,
)

SYSTEM_ID = "mineru-3.4.4-vlm"
ADAPTER_NAME = "normalize_mineru_vlm.py"
RULES = [
    "unwrap MinerU details/summary containers while retaining text_image and chart text",
    "replace natural images, flowcharts, Mermaid blocks, and image paths with ![]",
    "remove generated decorative-image captions and presentation-only sup/sub wrappers",
    "remove duplicate running headers and isolated page numbers using prediction-only repetition",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = normalize_mineru_details(text, stats)
    text = normalize_mermaid(text, stats)
    text = normalize_images(text, stats)
    text = remove_generated_image_captions(text, stats)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
