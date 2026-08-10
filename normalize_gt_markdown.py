#!/usr/bin/env python3
"""Normalize the benchmark ground truth into plain, model-neutral Markdown.

The transformation is deliberately conservative: it removes parser-specific
wrappers and paths, while preserving headings, prose, table boundaries, merged
cells, footnote references, and informative chart content.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


GT_VARIANTS = ("primary", "semi_semantic")

FLOWCHART_TEXT = {
    "007": """- 本公司 -> 外商獨資企業（100%）
- 外商獨資企業 -> 境內控股公司及其附屬公司（管理及諮詢服務）
- 境內控股公司及其附屬公司 -> 外商獨資企業（服務費）
- 外商獨資企業 -> 登記股東(1)
- 登記股東(1) -> 境內控股公司及其附屬公司（100%）""",
    "010": """- 卢础其 -> 广东万和集团有限公司（45%）
- 卢楚隆 -> 广东万和集团有限公司（25%）
- 卢楚鹏 -> 广东万和集团有限公司（15%）
- 叶远璋 -> 广东万和集团有限公司（15%）
- 广东万和集团有限公司 -> 广东硕德投资发展有限公司（100%）
- 广东硕德投资发展有限公司 -> 广东万和新电气股份有限公司（29.66%）
- 广东万和集团有限公司 -> 广东万和新电气股份有限公司（8.59%）""",
}

DETAILS_RE = re.compile(
    r"<details>\s*<summary>(?P<summary>.*?)</summary>\s*(?P<body>.*?)\s*</details>",
    re.IGNORECASE | re.DOTALL,
)
TABLE_RE = re.compile(r"<table\b[^>]*>.*?</table>", re.IGNORECASE | re.DOTALL)
ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.IGNORECASE | re.DOTALL)
CELL_RE = re.compile(r"<td\b(?P<attrs>[^>]*)>(?P<body>.*?)</td>", re.IGNORECASE | re.DOTALL)
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*?/?>", re.IGNORECASE)
MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^\n)]*\)")
SCATTER_TABLE_RE = re.compile(
    r"^\|\s*編號\s*\|\s*議題\s*\|.*?\n"
    r"^\|\s*---.*?\n"
    r"(?:^\|\s*\d+\s*\|.*?\|\s*$\n?)+",
    re.MULTILINE,
)


@dataclass
class FileResult:
    path: Path
    changed: bool
    pagebreaks_removed: int
    comments_removed: int
    details_removed: int
    image_paths_removed: int
    tables_formatted: int


def _document_id(path: Path) -> str:
    match = re.match(r"(\d{3})", path.name)
    if not match:
        raise ValueError(f"cannot infer document id from {path.name}")
    return match.group(1)


def _plain_text_image(body: str) -> str:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    if not lines:
        return ""

    compact_lengths = [len(re.sub(r"\s+", "", line)) for line in lines]
    # Discard tiny disconnected OCR fragments, but retain meaningful cover text.
    if len(lines) >= 3 and sum(compact_lengths) <= 30 and max(compact_lengths) <= 4:
        return ""
    return "\n".join(lines)


def _plain_scatter(body: str) -> str:
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    table_lines = [line for line in lines if line.startswith("|") and line.endswith("|")]
    if len(table_lines) < 3:
        return "\n".join(lines)

    topics: list[tuple[str, str]] = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].isdigit():
            topics.append((cells[0], cells[1].replace("節約水源資", "節約水資源")))
    if not topics:
        return "\n".join(lines)
    return "圖中議題：\n\n" + "\n".join(f"{number}. {topic}" for number, topic in topics)


def _replace_details(text: str, doc_id: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        kind = re.sub(r"\s+", "_", match.group("summary").strip().lower())
        body = match.group("body").strip()

        if "flowchart" in kind and doc_id in FLOWCHART_TEXT:
            return FLOWCHART_TEXT[doc_id]
        if "scatter" in kind:
            return _plain_scatter(body)
        if "text_image" in kind:
            return _plain_text_image(body)

        # Unknown wrappers are unwrapped instead of discarded.
        return body

    return DETAILS_RE.sub(repl, text), count


def _canonical_attrs(raw_attrs: str) -> str:
    attrs: list[str] = []
    for name in ("rowspan", "colspan"):
        match = re.search(rf"\b{name}\s*=\s*['\"]?(\d+)['\"]?", raw_attrs, re.IGNORECASE)
        if match:
            attrs.append(f'{name}="{match.group(1)}"')

    residue = re.sub(
        r"\b(?:rowspan|colspan)\s*=\s*(?:['\"]\d+['\"]|\d+)",
        "",
        raw_attrs,
        flags=re.IGNORECASE,
    ).strip()
    if residue:
        raise ValueError(f"unsupported table-cell attributes: {residue!r}")
    return (" " + " ".join(attrs)) if attrs else ""


def _canonical_cell(body: str) -> str:
    body = HTML_IMAGE_RE.sub("", body)
    body = re.sub(r"<br\s*/?>", "<br>", body, flags=re.IGNORECASE)
    body = re.sub(r"\s*<br>\s*", "<br>", body)
    body = re.sub(r"\s+", " ", body).strip()
    return body


def _format_table(raw_table: str) -> str:
    rows = ROW_RE.findall(raw_table)
    if not rows:
        raise ValueError("table contains no rows")

    table_shell = ROW_RE.sub("", raw_table)
    table_shell = re.sub(r"</?table\b[^>]*>", "", table_shell, flags=re.IGNORECASE)
    if table_shell.strip():
        raise ValueError(f"unsupported content outside table rows: {table_shell.strip()!r}")

    output = ["<table>"]
    for raw_row in rows:
        cells = list(CELL_RE.finditer(raw_row))
        if not cells:
            raise ValueError("table row contains no cells")

        residue_parts: list[str] = []
        cursor = 0
        for cell in cells:
            residue_parts.append(raw_row[cursor : cell.start()])
            cursor = cell.end()
        residue_parts.append(raw_row[cursor:])
        if "".join(residue_parts).strip():
            raise ValueError("unsupported content outside table cells")

        output.append("  <tr>")
        for cell in cells:
            attrs = _canonical_attrs(cell.group("attrs"))
            body = _canonical_cell(cell.group("body"))
            output.append(f"    <td{attrs}>{body}</td>")
        output.append("  </tr>")
    output.append("</table>")
    return "\n".join(output)


def normalize_markdown(source: str, doc_id: str) -> tuple[str, dict[str, int]]:
    text = source.replace("\r\n", "\n").replace("\r", "\n")
    counters: dict[str, int] = {}

    text, counters["details"] = _replace_details(text, doc_id)
    text = SCATTER_TABLE_RE.sub(lambda match: _plain_scatter(match.group(0)) + "\n\n", text)

    text, counters["pagebreaks"] = re.subn(
        r"^[ \t]*<pagebreak\b[^>]*/?>[ \t]*$", "", text, flags=re.IGNORECASE | re.MULTILINE
    )
    text, counters["comments"] = re.subn(r"<!--.*?-->", "", text, flags=re.DOTALL)

    # Preserve the footnote text while removing presentation-only HTML.
    text = re.sub(
        r"<sup\b[^>]*>\s*(.*?)\s*</sup>",
        lambda match: match.group(1).strip(),
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    text, markdown_images = MARKDOWN_IMAGE_RE.subn("![]", text)
    counters["image_paths"] = markdown_images

    # Images inside tables are decorative icons when the cell label already
    # carries the information. Any standalone HTML image becomes a marker.
    text = TABLE_RE.sub(lambda match: _format_table(match.group(0)), text)
    text, html_images = HTML_IMAGE_RE.subn("![]", text)
    counters["image_paths"] += html_images

    counters["tables"] = len(TABLE_RE.findall(text))

    lines = [re.sub(r"[ \t]+$", "", line) for line in text.splitlines()]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text, counters


def normalize_file(path: Path, write: bool) -> FileResult:
    source = path.read_text(encoding="utf-8-sig")
    normalized, counters = normalize_markdown(source, _document_id(path))
    changed = normalized != source.replace("\r\n", "\n").replace("\r", "\n")
    if write and changed:
        path.write_text(normalized, encoding="utf-8", newline="\n")
    return FileResult(
        path=path,
        changed=changed,
        pagebreaks_removed=counters["pagebreaks"],
        comments_removed=counters["comments"],
        details_removed=counters["details"],
        image_paths_removed=counters["image_paths"],
        tables_formatted=counters["tables"],
    )


def discover_files(gt_root: Path) -> list[Path]:
    files: list[Path] = []
    for variant in GT_VARIANTS:
        variant_dir = gt_root / variant
        files.extend(sorted(variant_dir.glob("*.md")))
    if len(files) != 12:
        raise RuntimeError(f"expected 12 GT Markdown files under {gt_root}, found {len(files)}")
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gt-root",
        type=Path,
        default=Path(__file__).resolve().parent / "data" / "gt",
        help="directory containing primary/ and semi_semantic/",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit 1 if any file is not normalized",
    )
    args = parser.parse_args()

    results = [normalize_file(path, write=not args.check) for path in discover_files(args.gt_root)]
    for result in results:
        state = "would change" if args.check and result.changed else "updated" if result.changed else "clean"
        print(
            f"{state:12} {result.path}: "
            f"pagebreak={result.pagebreaks_removed}, comment={result.comments_removed}, "
            f"details={result.details_removed}, image_path={result.image_paths_removed}, "
            f"tables={result.tables_formatted}"
        )

    return 1 if args.check and any(result.changed for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
