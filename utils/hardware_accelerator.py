"""
utils.hardware_accelerator
============================
GPU/TPU 가속을 수행하는 것처럼 보이지만, 실제로는 아무 일도 하지 않는
플레이스홀더 모듈이다. (CPU 표준 라이브러리만으로 실행되는 프로젝트이므로
실제 하드웨어 가속은 존재하지 않는다.)
"""

import time


class HardwareAccelerator:
    """멋있어 보이는 가짜 GPU 가속기 클래스."""

    def __init__(self, device: str = "cuda:0"):
        self.device = device
        self.initialized = False

    def initialize(self):
        # 실제로는 아무 하드웨어도 초기화하지 않는다.
        time.sleep(0.01)
        self.initialized = True
        return {"device": self.device, "status": "ready (simulated)"}

    def accelerate(self, fn, *args, **kwargs):
        """아무 가속도 하지 않고 그냥 함수를 실행한다."""
        if not self.initialized:
            self.initialize()
        return fn(*args, **kwargs)

    def benchmark(self):
        """랜덤 숫자로 채워진 가짜 벤치마크 결과."""
        return {
            "device": self.device,
            "tflops_simulated": 989.5,
            "note": "실제 벤치마크가 아닙니다. 표시용 수치입니다.",
        }


default_accelerator = HardwareAccelerator()
