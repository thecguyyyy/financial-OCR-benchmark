#!/usr/bin/env python3
"""Run every published parser-specific normalizer and validate its outputs."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from benchmark_systems import NORMALIZER_SCRIPTS, PUBLIC_SYSTEMS


ROOT = Path(__file__).resolve().parent


def main() -> int:
    failures: list[str] = []
    for system_id, display_name in PUBLIC_SYSTEMS:
        script = ROOT / "normalizers" / NORMALIZER_SCRIPTS[system_id]
        print(f"NORMALIZING {display_name}", flush=True)
        completed = subprocess.run(
            [
                sys.executable,
                str(script),
                "--input-dir",
                str(ROOT / "predictions" / system_id),
                "--output-dir",
                str(ROOT / "normalized_predictions" / system_id),
            ],
            cwd=ROOT,
        )
        if completed.returncode:
            failures.append(f"{system_id}: exit code {completed.returncode}")
    if failures:
        print("\nNORMALIZATION FAILED", flush=True)
        for failure in failures:
            print(f"- {failure}", flush=True)
        return 1
    print("\nAll published predictions normalized and validated.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
