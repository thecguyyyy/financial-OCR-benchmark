#!/usr/bin/env python
"""Score one external parser's six Markdown outputs against this benchmark.

Expected prediction identifiers are 005 through 010. The preferred file names
are 005.md, ..., 010.md; longer names beginning with the same identifier are
also accepted when the match is unique.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCORER = ROOT / "benchmark_scorer.py"
DOCUMENTS = [
    ("005", "中国平安"),
    ("006", "阿里巴巴"),
    ("007", "美团"),
    ("008", "先锋新材"),
    ("009", "紫天科技"),
    ("010", "万和电气"),
]
ALIASES = {
    "005": ("pingan", "平安"),
    "006": ("alibaba", "阿里"),
    "007": ("meituan", "美团"),
    "008": ("xianfeng", "先锋"),
    "009": ("zitian", "紫天"),
    "010": ("wanhe", "万和"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Score another parser's six Markdown outputs with the benchmark protocol."
    )
    parser.add_argument(
        "--pred-dir",
        type=Path,
        required=True,
        help="Directory containing the parser outputs for documents 005 through 010.",
    )
    parser.add_argument(
        "--system-name",
        required=True,
        help="Display name written to summary files, for example 'MyParser 1.0'.",
    )
    parser.add_argument(
        "--dataset-root",
        type=Path,
        default=ROOT / "data" / "gt",
        help="Dataset root containing both GT variants; defaults to data/gt in this repository.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory. Default: scores/<system-name-slug> under the project root.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of documents scored in parallel (default: 4).",
    )
    return parser.parse_args()


def one(paths: list[Path], description: str) -> Path:
    unique = sorted({path.resolve() for path in paths if path.is_file()})
    if len(unique) != 1:
        shown = ", ".join(str(path) for path in unique[:5]) or "none"
        raise RuntimeError(
            f"{description}: expected exactly one file, found {len(unique)} ({shown})"
        )
    return unique[0]


def find_gt(dataset_root: Path, doc_id: str, semi_semantic: bool) -> Path:
    standard_subdir = "semi_semantic" if semi_semantic else "primary"
    standard_path = dataset_root / standard_subdir / f"{doc_id}.md"
    if standard_path.is_file():
        return standard_path.resolve()
    suffix = (
        "*_gold_md_semi_semantic_tables.md" if semi_semantic else "*_gold_md.md"
    )
    return one(
        list(dataset_root.rglob(f"{doc_id}{suffix}")),
        f"{doc_id} {'Semi-semantic' if semi_semantic else 'Primary'} GT",
    )


def find_prediction(pred_dir: Path, doc_id: str) -> Path:
    exact = pred_dir / f"{doc_id}.md"
    if exact.is_file():
        return exact.resolve()

    candidates = [
        path
        for path in pred_dir.glob(f"{doc_id}*.md")
        if "report" not in path.stem.lower()
    ]
    if len(candidates) == 1:
        return candidates[0].resolve()

    aliases = ALIASES[doc_id]
    alias_candidates = [
        path
        for path in pred_dir.glob("*.md")
        if any(alias in path.name.lower() for alias in aliases)
        and "report" not in path.stem.lower()
    ]
    return one(candidates or alias_candidates, f"prediction {doc_id}")


def slugify(name: str) -> str:
    slug = re.sub(r"[^\w.-]+", "_", name, flags=re.UNICODE).strip("_.-")
    return slug or "external_parser"


def run_document(
    dataset_root: Path,
    pred_dir: Path,
    output_dir: Path,
    system_name: str,
    doc_id: str,
    document_name: str,
) -> dict:
    primary_gt = find_gt(dataset_root, doc_id, semi_semantic=False)
    semi_gt = find_gt(dataset_root, doc_id, semi_semantic=True)
    prediction = find_prediction(pred_dir, doc_id)

    report_dir = output_dir / "documents"
    report_dir.mkdir(parents=True, exist_ok=True)
    json_report = report_dir / f"{doc_id}_report.json"
    markdown_report = report_dir / f"{doc_id}_report.md"
    log_path = report_dir / f"{doc_id}.log"
    command = [
        sys.executable,
        str(SCORER),
        "--gt",
        str(primary_gt),
        "--gt-table-alt",
        str(semi_gt),
        "--pred",
        str(prediction),
        "--table-gt-strategy",
        "max",
        "--json-out",
        str(json_report),
        "--md-out",
        str(markdown_report),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    log_path.write_text(completed.stdout + completed.stderr, encoding="utf-8")
    if completed.returncode:
        raise RuntimeError(f"scorer failed; see {log_path}")

    result = json.loads(json_report.read_text(encoding="utf-8"))
    scores = result["scores"]
    tables = result["table_evaluation"]["selected_table_score"]
    return {
        "system": system_name,
        "id": doc_id,
        "document": document_name,
        "final_score": scores["final_score"],
        "table_score": scores["table_score"],
        "title_layout_score": scores["title_layout_score"],
        "text_score": scores["text_score"],
        "table_structure_score": tables["table_structure_score"],
        "table_content_score": tables["table_content_score"],
        "matched_table_count": tables["matched_table_count"],
        "missing_table_count": tables["missing_table_count"],
        "extra_table_count": tables["extra_table_count"],
        "primary_selected_pair_count": tables["primary_selected_pair_count"],
        "semi_semantic_selected_pair_count": tables["alt_selected_pair_count"],
        "prediction": str(prediction),
        "primary_gt": str(primary_gt),
        "semi_semantic_gt": str(semi_gt),
        "report": str(markdown_report),
    }


def write_outputs(output_dir: Path, system_name: str, rows: list[dict], errors: list[str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows.sort(key=lambda row: row["id"])
    (output_dir / "errors.json").write_text(
        json.dumps(errors, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "summary.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if rows:
        with (output_dir / "summary.csv").open(
            "w", newline="", encoding="utf-8-sig"
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    lines = [
        f"# {system_name} 评分报告",
        "",
        "评分协议：双 GT 单表最高匹配；总分 = 表格 40% + 标题布局 20% + 正文 40%；"
        "标题布局 = F1 80% + 相对层级 10% + 顺序 10%。",
        "",
    ]
    if rows:
        average = lambda key: sum(float(row[key]) for row in rows) / len(rows)
        lines.extend(
            [
                "## 平均分",
                "",
                "| 文件数 | 总分 | 表格 | 标题布局 | 正文 |",
                "|---:|---:|---:|---:|---:|",
                f"| {len(rows)} | {average('final_score'):.2f} | "
                f"{average('table_score'):.2f} | "
                f"{average('title_layout_score'):.2f} | "
                f"{average('text_score'):.2f} |",
                "",
                "## 逐文档结果",
                "",
                "| 编号 | 文档 | 总分 | 表格 | 标题布局 | 正文 | 匹配表 | 漏表 | 冗余表 |",
                "|---:|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for row in rows:
            lines.append(
                f"| {row['id']} | {row['document']} | {row['final_score']:.2f} | "
                f"{row['table_score']:.2f} | {row['title_layout_score']:.2f} | "
                f"{row['text_score']:.2f} | {row['matched_table_count']} | "
                f"{row['missing_table_count']} | {row['extra_table_count']} |"
            )
    if errors:
        lines.extend(["", "## 错误", ""] + [f"- {error}" for error in errors])
    lines.append("")
    (output_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    pred_dir = args.pred_dir.resolve()
    dataset_root = args.dataset_root.resolve()
    if not pred_dir.is_dir():
        raise NotADirectoryError(pred_dir)
    if not dataset_root.is_dir():
        raise NotADirectoryError(dataset_root)
    if args.workers < 1:
        raise ValueError("--workers must be at least 1")

    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else (ROOT / "scores" / slugify(args.system_name)).resolve()
    )
    rows: list[dict] = []
    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=min(args.workers, len(DOCUMENTS))) as executor:
        futures = {
            executor.submit(
                run_document,
                dataset_root,
                pred_dir,
                output_dir,
                args.system_name,
                doc_id,
                document_name,
            ): doc_id
            for doc_id, document_name in DOCUMENTS
        }
        for future in as_completed(futures):
            doc_id = futures[future]
            try:
                row = future.result()
                rows.append(row)
                print(
                    f"DONE {doc_id} final={row['final_score']:.2f} "
                    f"table={row['table_score']:.2f}",
                    flush=True,
                )
            except Exception as exc:
                message = f"{doc_id}: {exc}"
                errors.append(message)
                print(f"ERROR {message}", flush=True)

    write_outputs(output_dir, args.system_name, rows, errors)
    print(f"Summary: {output_dir / 'summary.md'}", flush=True)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
