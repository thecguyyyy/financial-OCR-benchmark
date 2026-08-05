#!/usr/bin/env python
"""Rescore every published prediction collection in the repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from benchmark_systems import PUBLIC_SYSTEMS


ROOT = Path(__file__).resolve().parent
STANDARD_SCORER = ROOT / "score_prediction_directory.py"


def main() -> int:
    failures: list[str] = []
    for directory_name, display_name in PUBLIC_SYSTEMS:
        prediction_dir = ROOT / "predictions" / directory_name
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
            str(ROOT / "data" / "gt"),
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
    print("\nAll published systems scored successfully.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
