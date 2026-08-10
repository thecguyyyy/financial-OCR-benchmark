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


DOCUMENT_IDS = ("005", "006", "007", "008", "009", "010")
Adapter = Callable[[str, Counter[str]], str]

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


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")


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
    """Unwrap MinerU visual containers without interpreting their content."""

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
    """Ignore whitespace introduced only around the canonical image marker."""

    return re.sub(r"\s*!\[\]\s*", "![]", cell).strip()


def _canonical_validation_heading(item: object) -> tuple[int, str]:
    level = int(getattr(item, "level"))
    text = str(getattr(item, "text"))
    text = _validation_image_only(text)
    text = re.sub(r"</?(?:sup|sub)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return level, text


def validate_transformation(source: str, normalized: str, adapter: Adapter) -> dict[str, object]:
    """Check table boundaries/content, heading sequence, and idempotence."""

    source_tables, _ = extract_tables(_validation_image_only(source))
    output_tables, _ = extract_tables(_validation_image_only(normalized))
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
    for source_heading in source_headings:
        if output_index < len(output_headings) and source_heading == output_headings[output_index]:
            output_index += 1
            continue
        if _looks_like_running_header(f"# {source_heading[1]}"):
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

    for doc_id in DOCUMENT_IDS:
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
