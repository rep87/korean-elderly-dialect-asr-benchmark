"""Reject obvious restricted-data identifiers before publishing aggregate results."""

from __future__ import annotations

import sys
from pathlib import Path


FORBIDDEN = ("ff01", "ff02", "c:\\", "data/aihub", "reference_text", "hypothesis", "audio_path")
ALLOWED = {"model-summary.json", "model-summary.csv"}


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    result_dir = root / "results"
    failed = False
    for path in result_dir.rglob("*"):
        if not path.is_file() or path.name not in ALLOWED:
            continue
        text = path.read_text(encoding="utf-8").lower()
        hits = [term for term in FORBIDDEN if term in text]
        if hits:
            print(f"FAIL {path.relative_to(root)} contains {', '.join(hits)}")
            failed = True
    if failed:
        raise SystemExit(1)
    print("PASS: public result artifacts contain no blocked identifiers.")


if __name__ == "__main__":
    main()
