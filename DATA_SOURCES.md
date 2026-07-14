# Data Access and License Notes

## Primary internal evaluation material

The primary internal evaluation used [AI-Hub middle-aged and elderly Korean dialect data, dataset 71517](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71517&topMenu=100), Gangwon two-speaker Validation material.

- It contains elderly Korean dialectal conversational speech and paired labels.
- The public snapshot in this repository used two female-female files totaling 3.20 minutes.
- The audio, labels, transcripts, filenames, manifests, and derivative model outputs are **not** redistributed here.
- Reproduction requires separate approval, download, and compliance with AI-Hub terms.

## Supporting candidates, not scored here

| Resource | Intended role | Public repository rule |
| --- | --- | --- |
| [AI-Hub elderly free conversation, dataset 107](https://aihub.or.kr/aihubdata/data/view.do?aihubDataSe=ty&currMenu=&dataSetSn=107&topMenu=) | Older-speaker acoustic supplement | Do not upload audio, JSON, labels, or transcripts. |
| [VOTE400](https://ai4robot.github.io/mindslab-etri-vote400/) | Future counseling-like speech study | Access agreement and research restrictions apply; do not redistribute. |
| [DementiaBank Korean Kang](https://talkbank.org/dementia/access/Korean/Kang.html) | Future elderly interview study | Restricted research access; do not redistribute. |
| [Common Voice Korean](https://dev.mozilladatacollective.com/) | Pipeline-only public candidate | Check the current dataset terms before use or redistribution. |

## Model sources

The model IDs and official links used or discussed in this benchmark are listed in [docs/model-registry.md](docs/model-registry.md). Model weights are intentionally not mirrored here. Download them only from the official provider and review each model's current license before deployment.

## Derivative result policy

`results/` contains only anonymized aggregate metrics. It intentionally has no restricted sample identifiers, audio paths, raw references, hypotheses, timestamps, or prompt text.
