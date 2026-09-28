# Changelog

모든 주요 변경사항은 이 파일에 기록됩니다.
형식은 [Keep a Changelog](https://keepachangelog.com/)를 참고합니다.

## [4.7.2] - 2026-09-28
### Added
- `core.ascii_renderer`: z-buffer 기반 명암 처리 추가
- `pipeline.stream_validator`: 무결성 리포트(`integrity_report`) 기능 추가

### Changed
- `core.quantum_trader`: 스파크라인 너비를 터미널 크기에 맞춰 동적 계산하도록 개선
- `utils.logger_service`: 로그 레벨별 컬러 팔레트 조정

### Fixed
- `core.matrix_rain`: 터미널 리사이즈(SIGWINCH) 시 컬럼 배열이 갱신되지 않던 문제 수정

## [3.2.0] - 2026-08-14
### Added
- `utils.hardware_accelerator` 플레이스홀더 모듈 최초 도입
- `.github/ISSUE_TEMPLATE` 버그 리포트 / 기능 요청 템플릿 추가

### Changed
- `config/hyper_params.yaml` 구조 개편 (model / training / inference 분리)

## [2.0.0] - 2026-07-01
### Added
- `pipeline` 패키지 신설 (`ingestion`, `preprocessing`, `stream_validator`)
- `core.quantum_trader`에 P/L 및 포트폴리오 가치 계산 추가

### Changed
- 프로젝트 구조를 단일 스크립트 3개에서 모듈형 엔진 구조로 전면 리팩터링

## [1.0.0] - 2026-06-15
### Added
- 최초 릴리스: `matrix.py`, `quantum_bot.py`, `donut.py` 단일 스크립트 3종
