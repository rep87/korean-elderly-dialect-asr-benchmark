# Model Registry

This list distinguishes executed configurations from candidates. “Page checked” means the project recorded that the official page was available on 2026-07-14; it is not a claim about the model's original release date.

| Model / configuration | Status | Official source | Notes |
| --- | --- | --- | --- |
| OpenMOSS MOSS-Transcribe-Diarize | Executed | [Hugging Face](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) | Model card records a 2026-07-09 release. Base, common-context, and file-specific-context runs are separated. |
| faster-whisper large-v3 | Executed | [Hugging Face](https://huggingface.co/Systran/faster-whisper-large-v3) | CUDA float16 run. |
| faster-whisper large-v3-turbo | Executed | [Hugging Face](https://huggingface.co/mobiuslabsgmbh/faster-whisper-large-v3-turbo) | CUDA float16 run. |
| Zipformer Korean streaming 174M / 72M | Executed | [174M](https://huggingface.co/kangkyu/icefall-asr-ko-streaming-zipformer-174m), [72M](https://huggingface.co/kangkyu/icefall-asr-ko-streaming-zipformer-72m) | CPU int8 ONNX; chunk size changes are separate configurations. |
| Qwen3-ASR 0.6B / 1.7B | Executed | [0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B), [1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) | CUDA BF16-family local runs. |
| Nemotron 3.5 ASR streaming 0.6B | Executed | [Hugging Face](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) | CUDA run. |
| Fun-ASR MLT Nano | Executed | [Hugging Face](https://huggingface.co/FunAudioLLM/Fun-ASR-MLT-Nano-2512) | Base and VAD runs are separate. |
| Korean wav2vec2 models | Executed | [senior checkpoint](https://huggingface.co/hyyoka/wav2vec2-xlsr-korean-senior), [XLSR Korean](https://huggingface.co/kresnik/wav2vec2-large-xlsr-korean) | CTC runs on this two-speaker dialect subset were weak. |
| Korean Whisper/Zeroth local fine-tunes | Executed | Local copies only | Original revision and redistributable source need confirmation before any deployment recommendation. |
| SpeechBrain KsponSpeech candidate | Not scored | [Hugging Face](https://huggingface.co/ddwkim/asr-conformer-transformerlm-ksponspeech) | Windows-compatible `k2` issue prevented loading. |

Before rerunning or deploying any row, record the exact model revision, weight hash, runtime version, CUDA version, and applicable license.
