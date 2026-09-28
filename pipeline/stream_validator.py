"""
pipeline.stream_validator
===========================
데이터 스트림 무결성을 검증하는 '척'하는 모듈.
실제로는 스키마 키 존재 여부만 확인하는 가벼운 체크다.
"""

REQUIRED_KEYS = {"source", "timestamp"}


class StreamValidator:
    def __init__(self):
        self.total_checked = 0
        self.total_rejected = 0

    def validate(self, batch):
        valid, rejected = [], []
        for item in batch:
            self.total_checked += 1
            if REQUIRED_KEYS.issubset(item.keys()):
                valid.append(item)
            else:
                rejected.append(item)
                self.total_rejected += 1
        return valid, rejected

    def integrity_report(self):
        rate = (
            1 - (self.total_rejected / self.total_checked)
            if self.total_checked else 1.0
        )
        return {
            "checked": self.total_checked,
            "rejected": self.total_rejected,
            "integrity_rate": round(rate, 4),
        }


if __name__ == "__main__":
    v = StreamValidator()
    valid, rejected = v.validate([{"source": "A", "timestamp": 1}, {"bad": True}])
    print(v.integrity_report())
