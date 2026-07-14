"""Score locally supplied ASR text without uploading audio or transcripts.

Input JSON files must map the same opaque item IDs to text. Keep those files
outside this public repository when they derive from restricted material.
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path


def normalize(text: str, for_cer: bool) -> str:
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"\[[^\]]*\]|\([^)]*\)", " ", text)
    text = re.sub(r"[^\w\s가-힣]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.replace(" ", "") if for_cer else text


def edit_distance(reference: list[str], hypothesis: list[str]) -> int:
    previous = list(range(len(hypothesis) + 1))
    for i, ref_token in enumerate(reference, 1):
        current = [i]
        for j, hyp_token in enumerate(hypothesis, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (ref_token != hyp_token)))
        previous = current
    return previous[-1]


def rate(reference: str, hypothesis: str, for_cer: bool) -> float:
    ref = normalize(reference, for_cer)
    hyp = normalize(hypothesis, for_cer)
    ref_tokens = list(ref) if for_cer else ref.split()
    hyp_tokens = list(hyp) if for_cer else hyp.split()
    if not ref_tokens:
        raise ValueError("Reference text becomes empty after normalization.")
    return edit_distance(ref_tokens, hyp_tokens) / len(ref_tokens)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--references", type=Path, required=True)
    parser.add_argument("--predictions", type=Path, required=True)
    args = parser.parse_args()
    references = json.loads(args.references.read_text(encoding="utf-8"))
    predictions = json.loads(args.predictions.read_text(encoding="utf-8"))
    shared = sorted(set(references) & set(predictions))
    if not shared:
        raise SystemExit("No shared opaque item IDs.")
    cer = [rate(references[key], predictions[key], True) for key in shared]
    wer = [rate(references[key], predictions[key], False) for key in shared]
    print(json.dumps({"items_scored": len(shared), "mean_cer": sum(cer) / len(cer), "mean_wer": sum(wer) / len(wer)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
