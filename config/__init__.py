"""
NEXUS Config Engine
====================
시스템 전역 설정을 로드하는 모듈. (실제로는 로드할 필요가 없는 가짜 설정)
"""

import json
import os

_CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))


def load_hyper_params():
    """hyper_params.yaml 경로를 반환한다. (파싱은 하지 않음 — 허세용)"""
    return os.path.join(_CONFIG_DIR, "hyper_params.yaml")


def load_secure_config():
    path = os.path.join(_CONFIG_DIR, "network_secure.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
