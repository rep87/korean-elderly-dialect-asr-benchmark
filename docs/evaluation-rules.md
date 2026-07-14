# Evaluation Rules

## Snapshot scope

This public snapshot records a quick candidate-selection run on two restricted-data files from the Gangwon two-speaker Validation material. Both are female-female conversations and total 3.20 minutes. The official source split name is `Validation`, but this run is not a full validation evaluation or an independent test.

## Metrics

- **Standard CER**: character error rate against the standard-Korean transcript variant.
- **Dialect CER**: character error rate against the dialect transcript variant.
- **Dialect WER**: whitespace-token word error rate against the dialect transcript variant.
- **Transcription time**: repeat transcription elapsed seconds for the two-file run.
- **Peak RAM/VRAM**: observed process peak, not a hardware requirement guarantee.

## Normalization

1. Normalize text to Unicode NFC.
2. Collapse line breaks and repeated whitespace.
3. Remove timestamps, speaker labels, and segment markers from hypotheses before scoring.
4. Remove whitespace and punctuation for CER.
5. Remove punctuation and split on whitespace for WER.
6. Do not silently normalize numbers, fillers, repetitions, or negative expressions.

Some streaming Zipformer outputs did not restore spaces reliably. Their WER is shown as `not comparable` rather than treated as recognition quality.

## Comparability limits

- MOSS file-specific context receives information unavailable to the base configurations; it is a usefulness experiment, not a fully controlled baseline.
- Engines, segmentation choices, VAD, precision, and hardware paths differ by model.
- Model-training overlap with the restricted evaluation material was not independently audited.
- No model selection should be read as a production recommendation for counseling records.
