#!/usr/bin/env python3
"""
NEXUS Core Engine — Main Controller
=====================================
전체 시스템을 제어하는 진입점.
설정 로드 → 하드웨어 가속기 초기화 → 데이터 파이프라인 워밍업 →
사용자가 선택한 core 엔진 실행, 순서로 동작한다.

실행:
    python main.py
"""

import sys
import time

from config import load_secure_config
from core import matrix_rain, quantum_trader, ascii_renderer
from pipeline.ingestion import DataIngestionEngine
from pipeline.stream_validator import StreamValidator
from utils.logger_service import default_logger as log
from utils.hardware_accelerator import default_accelerator
from utils.crypto_helper import fake_quantum_key

BANNER = r"""
 _   _ _______  ___   _ ____
| \ | | ____\ \/ / | | / ___|
|  \| |  _|  \  /| | | \___ \
| |\  | |___ /  \| |_| |___) |
|_| \_|_____/_/\_\\___/|____/

        CORE ENGINE  v4.7.2
"""

MENU = """
  [1] Matrix Digital Rain      (core.matrix_rain)
  [2] Quantum Trading Engine   (core.quantum_trader)
  [3] 3D ASCII Donut Renderer  (core.ascii_renderer)
  [0] Exit
"""


def _boot_sequence():
    """진지해 보이는 척 부팅 시퀀스를 수행한다."""
    print(BANNER)
    log.info("NEXUS Core Engine 부팅 시작...")

    try:
        secure_cfg = load_secure_config()
        log.success(
            f"보안 설정 로드 완료 (protocol={secure_cfg['network']['protocol']})"
        )
    except Exception as e:  # noqa: BLE001
        log.warn(f"보안 설정 로드 실패, 기본값 사용: {e}")

    accel_status = default_accelerator.initialize()
    log.success(f"가속기 초기화 완료: {accel_status}")

    key = fake_quantum_key()
    log.info(f"세션 키 생성: {key[:16]}...(생략)")

    ingestion = DataIngestionEngine()
    conn = ingestion.connect()
    log.success(f"데이터 파이프라인 연결됨 (sources={conn['sources']})")

    validator = StreamValidator()
    batch = ingestion.fetch_batch(16)
    valid, rejected = validator.validate(batch)
    log.info(
        f"초기 스트림 검증 완료: valid={len(valid)}, rejected={len(rejected)}"
    )

    time.sleep(0.3)
    log.success("모든 서브시스템 정상. 대기 중.\n")


def _run_menu():
    while True:
        print(MENU)
        choice = input("  실행할 엔진을 선택하세요 > ").strip()

        if choice == "1":
            log.info("Matrix Digital Rain 엔진 시작 (Ctrl+C로 종료)")
            time.sleep(0.5)
            matrix_rain.run()
        elif choice == "2":
            log.info("Quantum Trading 엔진 시작 (Ctrl+C로 종료)")
            time.sleep(0.5)
            quantum_trader.run()
        elif choice == "3":
            log.info("3D ASCII Donut 렌더러 시작 (Ctrl+C로 종료)")
            time.sleep(0.5)
            ascii_renderer.run()
        elif choice == "0":
            log.info("NEXUS Core Engine 종료.")
            sys.exit(0)
        else:
            log.warn("잘못된 입력입니다. 0~3 중에서 선택해주세요.")


def main():
    try:
        _boot_sequence()
        _run_menu()
    except KeyboardInterrupt:
        print()
        log.info("사용자에 의해 중단됨. 종료합니다.")
        sys.exit(0)


if __name__ == "__main__":
    main()
