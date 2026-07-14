# Reproducibility Notes

The public repository is intentionally not a one-command reproduction of the restricted-data benchmark.

To reproduce a comparable private run:

1. Obtain authorization for the source dataset independently.
2. Build a fixed development and holdout manifest at the speaker level.
3. Keep raw audio, transcripts, manifests, outputs, and credentials outside this repository.
4. Download model weights from official sources and record revision hashes.
5. Run the same normalization rules in [evaluation-rules.md](evaluation-rules.md).
6. Export only aggregate metrics with [scripts/validate_public_results.py](../scripts/validate_public_results.py) before publication.

The provided scorer accepts user-supplied local reference and prediction JSON files. It is a small, dependency-free implementation of the public normalization rules; it does not download models, audio, or datasets.
