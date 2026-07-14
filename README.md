# 한국어 방언·고령자 음성 전사 벤치마크

> **TL;DR (EN):** A small-sample benchmark of open ASR checkpoints on Korean elderly and dialectal conversational speech.
> What worked: a transparent comparison of accuracy, speed, and memory on two restricted-data files.
> What remains: a frozen multi-speaker holdout, critical-error review, and a consented public demo set. (2026-07, local CUDA/CPU runs)

이 저장소는 노인보호전문기관 등의 상담 기록 업무를 보조할 수 있는 로컬 음성인식 후보를 탐색하며, 강원도 중·노년층 2인 대화에 가까운 조건에서 공개 ASR 모델을 비교한 기록입니다.

새 모델을 학습하거나 음성·전사·가중치를 배포하는 프로젝트가 아닙니다. 모델별 집계 점수, 평가 규칙, 실행 조건, 공개 가능한 최소 유틸리티만 제공합니다.

## 현재 스냅샷

2026-07-14 기준, 제한된 AI-Hub 강원도 2인 대화 Validation에서 선택한 여성-여성 파일 2개(총 3.20분)를 사용했습니다. 이 두 파일은 후보 선별용 소표본이며, 강원도 고령자 전체나 실제 상담 현장 성능을 대표하지 않습니다.

- 가장 낮은 표준어형 CER: `OpenMOSS-Team/MOSS-Transcribe-Diarize`, 파일별 문맥 설정, **12.38%**
- 가장 빠른 정확도 중심 GPU 기준선: `faster-whisper-large-v3-turbo`, **16.91% CER**, **4.59초**
- CPU·저메모리 후보: Zipformer 174M chunk 64, **14.72% CER**, **795MB RAM**, **15.41초**

파일별 문맥 설정은 다른 무문맥 모델과 완전히 동일한 조건이 아닙니다. 따라서 기본 MOSS, 공통 문맥 MOSS, 무문맥 기준선을 함께 기록했습니다.

## 결과 보기

- [정적 모델 비교 워크벤치](dashboard/index.html)
- [집계 결과 JSON](results/model-summary.json)
- [모델·설정 레지스트리](docs/model-registry.md)
- [평가 규칙](docs/evaluation-rules.md)
- [데이터 접근·라이선스](DATA_SOURCES.md)

브라우저에서 `dashboard/index.html`을 열면 저장된 결과를 볼 수 있습니다. 로컬 HTTP 서버가 필요하면 다음 명령을 사용합니다.

```powershell
python -m http.server 8000 -d dashboard
```

## 이 결과가 말하는 것과 말하지 않는 것

확인한 것:

- 같은 제한 자료와 정규화 규칙에서 여러 모델·설정을 비교할 수 있었다.
- 정확도, 처리 시간, RAM/VRAM 사이의 선택지를 수치로 남길 수 있었다.
- 고령자 특화 또는 한국어 파인튜닝이라는 이름만으로 이 소표본에서 우위를 보장하지는 않았다.

확인하지 않은 것:

- 실제 기관 상담 기록에서의 품질, 안전성, 업무시간 감소
- 강원도 방언·고령자 전체에 대한 일반화
- 화자 분리, 타임스탬프, 중대 오류(이름·날짜·금액·부정 표현)의 충분한 평가
- 사람 검토 없이 공식 기록으로 사용할 수 있는 수준

실제 적용은 사람의 원음 검토, 승인된 자료, 기관의 개인정보·보안 검토를 전제로 해야 합니다.

## 공개 범위

포함:

- 제한 자료에서 전사문과 파일 식별자를 제거한 집계 결과
- 모델 ID, 설정, 점수, 속도, 메모리
- 정규화·CER/WER 계산 규칙과 표준 라이브러리 기반 점수 도구
- 데이터 접근 및 라이선스 안내

제외:

- 원본 오디오, 정답 전사, 모델 출력 전문, 파일명·매니페스트
- AI-Hub 및 기타 제한 자료의 라벨·압축 파일
- 실제 상담 자료, API 키·토큰·다운로드 도구
- 모델 가중치, 가상환경, 캐시, 실행 로그

## 결과 갱신 규칙

새 체크포인트를 추가할 때는 이전 결과를 덮어쓰지 않습니다. 같은 고정 평가 묶음, 정규화 규칙, 장치·정밀도·분할 설정, 보고 필드를 유지한 새 날짜 스냅샷을 추가해야 합니다. 정식 비교 전에는 화자 단위로 분리한 개발 세트와 holdout 세트를 구성해야 합니다.

## 라이선스

코드는 [MIT License](LICENSE)입니다. 직접 작성한 문서는 [CC BY 4.0](LICENSE-DOCS.md)입니다. 외부 데이터와 모델에는 각각의 원래 라이선스와 접근 조건이 적용되며, 이 저장소의 라이선스로 재허가되지 않습니다.
