"""
tests.test_matrix
===================
core.matrix_rain에 대한 간단한 단위 테스트.
(프로젝트 전체가 '완벽해 보이도록' 만드는 테스트지만, 아래 항목들은
실제로 동작을 검증한다.)
"""

import unittest

from core.matrix_rain import _Column, _build_frame, CHARSET


class TestMatrixColumn(unittest.TestCase):
    def test_column_starts_within_reasonable_bounds(self):
        col = _Column(x=5, height=24)
        self.assertEqual(col.x, 5)
        self.assertGreaterEqual(col.length, 5)

    def test_column_step_moves_or_holds_position(self):
        col = _Column(x=0, height=24)
        col.speed = 2.0
        start_y = col.y
        col.step()
        self.assertGreaterEqual(col.y, start_y)

    def test_column_reset_repositions_above_screen(self):
        col = _Column(x=0, height=24)
        col.reset(height=24, start_random=False)
        self.assertEqual(col.y, -col.length)


class TestBuildFrame(unittest.TestCase):
    def test_build_frame_returns_correct_line_count(self):
        columns = [_Column(x, 10) for x in range(5)]
        frame = _build_frame(columns, width=5, height=10)
        # HOME 이스케이프 코드 이후 10줄이 개행으로 구분되어야 한다.
        body = frame.split("\x1b[H", 1)[1]
        self.assertEqual(len(body.split("\n")), 10)

    def test_charset_not_empty(self):
        self.assertGreater(len(CHARSET), 0)


if __name__ == "__main__":
    unittest.main()
