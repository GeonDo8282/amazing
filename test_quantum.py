"""
tests.test_quantum
====================
core.quantum_trader에 대한 간단한 단위 테스트.
"""

import unittest

from core.quantum_trader import _Asset, TICKERS
from pipeline.stream_validator import StreamValidator
from pipeline.preprocessing import normalize, denoise


class TestAsset(unittest.TestCase):
    def test_asset_price_stays_positive_after_many_steps(self):
        asset = _Asset("TEST")
        for _ in range(500):
            asset.step()
        self.assertGreater(asset.price, 0)

    def test_asset_history_capped_at_40(self):
        asset = _Asset("TEST")
        for _ in range(100):
            asset.step()
        self.assertLessEqual(len(asset.history), 40)

    def test_sparkline_length_matches_width(self):
        asset = _Asset("TEST")
        for _ in range(20):
            asset.step()
        spark = asset.sparkline(15)
        self.assertEqual(len(spark), 15)

    def test_ticker_list_not_empty(self):
        self.assertGreater(len(TICKERS), 0)


class TestPipelineIntegration(unittest.TestCase):
    def test_validator_rejects_malformed_items(self):
        v = StreamValidator()
        valid, rejected = v.validate([{"source": "A", "timestamp": 1}, {"bad": True}])
        self.assertEqual(len(valid), 1)
        self.assertEqual(len(rejected), 1)

    def test_normalize_and_denoise_pipeline(self):
        batch = [{"raw_value": 0.5}, {"raw_value": 0.501}]
        result = denoise(normalize(batch), threshold=0.05)
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
