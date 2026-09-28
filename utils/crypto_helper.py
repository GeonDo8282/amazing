"""
utils.crypto_helper
=====================
"포스트 퀀텀 암호화"를 흉내 내는 헬퍼.
실제로는 hashlib 기반의 단순 해시/난독화만 수행한다.
절대 실제 보안 목적으로 사용하지 말 것.
"""

import hashlib
import base64
import os


def obfuscate(data: str) -> str:
    """base64 인코딩 + salt. 암호화가 아니라 난독화일 뿐이다."""
    salt = os.urandom(4)
    payload = salt + data.encode("utf-8")
    return base64.b64encode(payload).decode("ascii")


def deobfuscate(token: str) -> str:
    raw = base64.b64decode(token.encode("ascii"))
    return raw[4:].decode("utf-8")


def fingerprint(data: str) -> str:
    """SHA-256 해시 지문 (실제로 동작함)."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def fake_quantum_key(bits: int = 256) -> str:
    """'양자 키'라고 부르지만 사실 os.urandom이다."""
    return os.urandom(bits // 8).hex()
