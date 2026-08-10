#!/usr/bin/env python
"""Normalize and rescore every published prediction collection."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

from benchmark_systems import PUBLIC_SYSTEMS


ROOT = Path(__file__).resolve().parent
STANDARD_SCORER = ROOT / "score_prediction_directory.py"
NORMALIZE_ALL = ROOT / "normalize_all_predictions.py"


def write_leaderboard() -> None:
    rows: list[dict] = []
    for directory_name, display_name in PUBLIC_SYSTEMS:
        summary_path = ROOT / "scores" / directory_name / "summary.json"
        documents = json.loads(summary_path.read_text(encoding="utf-8"))
        if len(documents) != 6:
            raise RuntimeError(f"{directory_name}: expected 6 scored documents")
        mean = lambda key: sum(float(row[key]) for row in documents) / len(documents)
        rows.append(
            {
                "system": directory_name,
                "system_name": display_name,
                "document_count": len(documents),
                "final_score": round(mean("final_score"), 4),
                "table_score": round(mean("table_score"), 4),
                "title_layout_score": round(mean("title_layout_score"), 4),
                "text_score": round(mean("text_score"), 4),
            }
        )
    rows.sort(key=lambda row: row["final_score"], reverse=True)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    (ROOT / "scores" / "leaderboard.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    csv_rows = [
        {"rank": row["rank"], **{key: value for key, value in row.items() if key != "rank"}}
        for row in rows
    ]
    with (ROOT / "scores" / "leaderboard.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dataset-root",
        type=Path,
        default=ROOT / "data" / "gt",
        help="GT root containing primary/ and semi_semantic/.",
    )
    parser.add_argument(
        "--skip-normalization",
        action="store_true",
        help="Reuse already validated normalized_predictions/ outputs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dataset_root = args.dataset_root.resolve()
    if not args.skip_normalization:
        print("NORMALIZING ALL PUBLISHED SYSTEMS", flush=True)
        normalized = subprocess.run([sys.executable, str(NORMALIZE_ALL)], cwd=ROOT)
        if normalized.returncode:
            return normalized.returncode

    failures: list[str] = []
    for directory_name, display_name in PUBLIC_SYSTEMS:
        prediction_dir = ROOT / "normalized_predictions" / directory_name
        output_dir = ROOT / "scores" / directory_name
        if not prediction_dir.is_dir():
            failures.append(f"missing prediction directory: {prediction_dir}")
            continue
        command = [
            sys.executable,
            str(STANDARD_SCORER),
            "--pred-dir",
            str(prediction_dir),
            "--system-name",
            display_name,
            "--dataset-root",
            str(dataset_root),
            "--output-dir",
            str(output_dir),
        ]
        print(f"SCORING {display_name}", flush=True)
        completed = subprocess.run(command)
        if completed.returncode:
            failures.append(f"{display_name}: exit code {completed.returncode}")

    if failures:
        print("\nFAILED", flush=True)
        for failure in failures:
            print(f"- {failure}", flush=True)
        return 1
    write_leaderboard()
    print("\nAll published systems scored successfully.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
