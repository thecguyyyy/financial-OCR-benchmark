#!/usr/bin/env python3
"""Adapter for the published self-developed parser outputs."""

from __future__ import annotations

from collections import Counter

from common import (
    normalize_images,
    normalize_newlines,
    remove_pagebreaks,
    remove_repeated_page_noise,
    run_adapter_cli,
    strip_comments,
    unwrap_inline_tags,
)

SYSTEM_ID = "self-developed-parser"
ADAPTER_NAME = "normalize_self_developed.py"
RULES = [
    "remove pagebreak control tags",
    "replace image coordinate XML with ![] so page/x/y/w/h values cannot enter text scoring",
    "unwrap presentation-only sup/sub tags while retaining their text",
    "remove parser comments, duplicate running headers, and isolated page numbers",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = remove_pagebreaks(text, stats)
    text = normalize_images(text, stats, coordinate_xml=True)
    text = unwrap_inline_tags(text, stats)
    text = strip_comments(text, stats)
    return remove_repeated_page_noise(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
