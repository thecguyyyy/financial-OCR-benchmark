#!/usr/bin/env python3
"""Template for a new parser-specific, GT-independent output adapter.

Copy this file, change SYSTEM_ID and the explicit rules, then commit the copied
script with the parser results.  Never inspect GT/PDF files or branch on a
document identifier inside an adapter.
"""

from __future__ import annotations

from collections import Counter

from common import normalize_images, normalize_newlines, run_adapter_cli, strip_comments

SYSTEM_ID = "replace-with-parser-id"
ADAPTER_NAME = "normalize_replace_with_parser_id.py"
RULES = [
    "replace parser image paths with ![]",
    "remove parser metadata comments",
]


def normalize(text: str, stats: Counter[str]) -> str:
    text = normalize_newlines(text)
    text = normalize_images(text, stats)
    return strip_comments(text, stats)


if __name__ == "__main__":
    raise SystemExit(run_adapter_cli(normalize, ADAPTER_NAME, SYSTEM_ID, RULES))
