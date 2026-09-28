# 🌌 NEXUS Core Engine

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Productivity](https://img.shields.io/badge/productivity-questionable-orange)](#)

> **"세상에서 가장 무해하고, 가장 쓸모없지만, 내 모니터를 가장 완벽하게 채워주는 파이썬 엔진 프로젝트"**
>
> 스타벅스나 공공장소에서 `python main.py`를 실행하는 순간, 주변 사람들의 시선을 한 몸에 받는
> 개발자 전용 허세(Flex) 패키지입니다. 폴더 구조만 보면 진짜 AI 트레이딩 엔진처럼 보이지만,
> 실체는 표준 라이브러리로 만든 터미널 애니메이션 3종입니다.

<br />

## 📁 프로젝트 구조

```
nexus-core-engine/
│
├── .github/                   # 오픈소스 기여 및 자동화 템플릿
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
│
├── config/                    # 시스템 설정 파일 엔진
│   ├── __init__.py
│   ├── hyper_params.yaml      # 가짜 하이퍼파라미터
│   └── network_secure.json    # 가짜 보안 설정
│
├── core/                      # 📌 핵심 엔진
│   ├── __init__.py
│   ├── matrix_rain.py         # [기능1] 매트릭스 엔진
│   ├── quantum_trader.py      # [기능2] 트레이딩 엔진
│   └── ascii_renderer.py      # [기능3] 3D 도넛 엔진
│
├── pipeline/                  # 가짜 데이터 처리 파이프라인
│   ├── __init__.py
│   ├── ingestion.py
│   ├── preprocessing.py
│   └── stream_validator.py
│
├── utils/                     # 유틸리티 및 디버깅 모듈
│   ├── __init__.py
│   ├── logger_service.py
│   ├── crypto_helper.py
│   └── hardware_accelerator.py  # GPU 가속하는 척하는 빈 파일
│
├── tests/                     # 단위 테스트
│   ├── __init__.py
│   ├── test_matrix.py
│   └── test_quantum.py
│
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── requirements.txt
└── main.py                    # 전체 시스템을 제어하는 메인 컨트롤러
```

<br />

## 🚀 탑재된 기능 (Features)

| 모듈 | 한 줄 요약 | 주요 기술 스택 | 허세 지수 |
| :--- | :--- | :--- | :---: |
| **1. Matrix Rain** | 할리우드 영화 스타일의 매트릭스 코드 낙하 | `shutil`, `ANSI Escape` | ⭐⭐⭐⭐⭐ |
| **2. Quantum Trader** | 실시간 자산 가격 변동 및 아비트라지 가짜 시뮬레이터 | `math.sin`, `sys.stdout` | ⭐⭐⭐⭐☆ |
| **3. ASCII Renderer** | 수학적 공식으로만 구현한 텍스트 기반 3D 도넛 렌더러 | `Trigonometry`, `Buffer` | ⭐⭐⭐⭐⭐ |

<br />

## ⚙️ 실행 방법 (How to Run)

의존성 패키지 설치가 **전혀 필요 없습니다.** 오직 파이썬 순정(Standard Library) 라이브러리로만 구동됩니다.
(`requirements.txt`는 있어 보이라고 넣은 장식용입니다.)

```bash
# 리포지토리 클론
git clone https://github.com/your-name/nexus-core-engine.git
cd nexus-core-engine

# 메인 컨트롤러 실행 (부팅 시퀀스 → 메뉴 선택)
python main.py
```

메뉴에서 `1`, `2`, `3` 중 하나를 선택하면 해당 엔진이 실행됩니다. 종료는 `Ctrl + C`.

개별 엔진만 바로 실행하고 싶다면:

```bash
python -m core.matrix_rain
python -m core.quantum_trader
python -m core.ascii_renderer
```

> **💡 꿀팁:** 터미널 창을 전체 화면(`F11`)으로 키우고, 폰트 크기를 살짝 줄인 뒤 실행하면 간지가 200% 상승합니다.

<br />

## 🛠️ 모듈 설명

### 🟢 core.matrix_rain
터미널의 가로/세로 크기를 자동으로 감지하여 화면 전체에 무작위 아스키 문자를 떨어뜨립니다.
가장 하단의 문자는 밝은 흰색으로 빛나며 흐려지는 효과를 재현했습니다. 터미널 리사이즈(`SIGWINCH`)에도 반응합니다.

### 📈 core.quantum_trader
마치 초당 수백 번의 연산을 처리하는 인공지능 매매 프로그램처럼 보입니다. `sin` 함수 기반의
노이즈 알고리즘을 적용하여 그럴싸한 주가 변동 그래프(스파크라인)를 실시간으로 그리고,
가짜 시스템 로그와 포트폴리오 P/L을 함께 출력합니다.

### 🍩 core.ascii_renderer
80x22 터미널 환경에서 삼각함수(`sin`, `cos`)를 활용해 3차원 토러스의 회전과 광원 표면
명암(Luminance)을 아스키 문자로 매핑하는, 텍스트 그래픽스의 정수입니다.

### 🧩 그 외 (전부 장식 or 가벼운 헬퍼)
- `pipeline/` — "실시간 데이터 파이프라인"처럼 보이지만 실제로는 난수를 만들어 흘려보내는 역할만 합니다.
- `utils.logger_service` — 유일하게 진지하게 동작하는 컬러 콘솔 로거입니다.
- `utils.crypto_helper` — `SHA-256` 지문 생성은 진짜지만, "양자 키 생성"은 사실 `os.urandom`입니다.
- `utils.hardware_accelerator` — GPU를 전혀 사용하지 않는 GPU 가속기 흉내 클래스입니다.
- `config/` — YAML/JSON 설정 파일이 존재하긴 하지만 core 엔진 동작에 실질적 영향은 주지 않습니다.

<br />

## 🧪 테스트

```bash
python -m unittest discover tests
```

`core.matrix_rain`과 `core.quantum_trader`의 핵심 로직(컬럼 이동, 프레임 생성, 가격 시뮬레이션,
스트림 검증)에 대한 실제 단위 테스트가 포함되어 있습니다.

<br />

## 📄 라이선스 (License)
이 프로젝트는 **MIT 라이선스**를 따릅니다. 마음껏 수정하고, 친구들에게 자랑하고, 깃허브 잔디밭을 빛내주세요!
