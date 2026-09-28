"""
pipeline.preprocessing
========================
수집된 원시 데이터를 정규화/스케일링하는 '척'하는 모듈.
"""


def normalize(batch):
    """raw_value를 -1 ~ 1 범위로 정규화한다 (실제 동작은 한다)."""
    return [
        {**item, "normalized": item["raw_value"] * 2 - 1}
        for item in batch
    ]


def denoise(batch, threshold: float = 0.05):
    """작은 노이즈로 간주되는 항목을 제거한다."""
    return [item for item in batch if abs(item.get("normalized", 0)) > threshold]


def enrich_with_metadata(batch):
    """가짜 메타데이터(지연시간, 신뢰도 점수)를 덧붙인다."""
    import random

    for item in batch:
        item["latency_ms"] = round(random.uniform(0.1, 5.0), 3)
        item["confidence_score"] = round(random.uniform(0.85, 0.999), 4)
    return batch


if __name__ == "__main__":
    fake_batch = [{"raw_value": 0.5}, {"raw_value": 0.51}, {"raw_value": 0.9}]
    result = enrich_with_metadata(denoise(normalize(fake_batch)))
    print(f"처리 완료: {len(result)}건")
