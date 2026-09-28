"""
pipeline.ingestion
===================
실시간 시장 데이터 수집기 (가짜).
실제로는 외부 소스에 연결하지 않으며, core 엔진의 난수 기반
시뮬레이션 데이터를 "수집한 것처럼" 포장하는 역할만 한다.
"""

import random
import time


class DataIngestionEngine:
    """수백 개의 거래소에서 실시간 스트림을 수집하는 '척'하는 엔진."""

    def __init__(self, sources=None):
        self.sources = sources or [
            "NYSE-FEED", "NASDAQ-FEED", "QUANTUM-DARKPOOL",
            "ARBX-RELAY", "SYNTH-EXCHANGE",
        ]
        self.connected = False

    def connect(self):
        """가짜 커넥션 핸드셰이크."""
        time.sleep(0.05)
        self.connected = True
        return {"status": "connected", "sources": len(self.sources)}

    def fetch_batch(self, size: int = 32):
        """가짜 원시 데이터 배치를 생성한다."""
        if not self.connected:
            self.connect()
        return [
            {
                "source": random.choice(self.sources),
                "timestamp": time.time(),
                "raw_value": random.uniform(0, 1),
            }
            for _ in range(size)
        ]


if __name__ == "__main__":
    engine = DataIngestionEngine()
    print(engine.connect())
    print(f"샘플 배치: {len(engine.fetch_batch())}건 수집됨")
