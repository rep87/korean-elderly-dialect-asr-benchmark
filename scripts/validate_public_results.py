"""Reject obvious restricted-data identifiers before publishing public documentation."""

from __future__ import annotations

import sys
from pathlib import Path


FORBIDDEN = ("ff01", "ff02", "c:\\", "data/aihub", "reference_text", "hypothesis", "audio_path")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    public_paths = [root / "README.md", root / "DATA_SOURCES.md"]
    public_paths.extend((root / "docs").rglob("*.md"))
    failed = False
    for path in public_paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8").lower()
        hits = [term for term in FORBIDDEN if term in text]
        if hits:
            print(f"FAIL {path.relative_to(root)} contains {', '.join(hits)}")
            failed = True
    if failed:
        raise SystemExit(1)
    print("PASS: public documentation contains no blocked identifiers.")


if __name__ == "__main__":
    main()
