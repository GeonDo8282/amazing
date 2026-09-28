"""
core.matrix_rain
=================
[기능1] 매트릭스 디지털 레인 엔진.
터미널 크기를 자동 감지하여 화면 전체에 무작위 문자를 낙하시킨다.
표준 라이브러리만 사용.
"""

import random
import shutil
import sys
import time
import signal

HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
CLEAR_SCREEN = "\x1b[2J"
HOME = "\x1b[H"
RESET = "\x1b[0m"
BRIGHT_WHITE = "\x1b[97m"
GREEN = "\x1b[32m"
DIM_GREEN = "\x1b[2;32m"

CHARSET = (
    "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ$+-*/=%\"'#&_(),.;:?!\\|{}<>[]^~"
)


class _Column:
    __slots__ = ("x", "y", "length", "speed", "_carry")

    def __init__(self, x: int, height: int):
        self.x = x
        self.reset(height, start_random=True)

    def reset(self, height: int, start_random: bool = False):
        self.length = random.randint(5, height // 2 + 5)
        self.speed = random.uniform(0.5, 1.5)
        self._carry = 0.0
        self.y = random.randint(-height, 0) if start_random else -self.length

    def step(self):
        self._carry += self.speed
        if self._carry >= 1:
            self.y += int(self._carry)
            self._carry -= int(self._carry)


def _build_frame(columns, width, height):
    screen_rows = [[" "] * width for _ in range(height)]
    color_rows = [[None] * width for _ in range(height)]

    for col in columns:
        head = col.y
        for i in range(col.length):
            y = head - i
            if 0 <= y < height:
                ch = random.choice(CHARSET)
                if i == 0:
                    color_rows[y][col.x] = BRIGHT_WHITE
                elif i < col.length * 0.15:
                    color_rows[y][col.x] = GREEN
                else:
                    color_rows[y][col.x] = DIM_GREEN
                screen_rows[y][col.x] = ch

    lines = []
    for y in range(height):
        parts = []
        current_color = None
        for x in range(width):
            ch = screen_rows[y][x]
            color = color_rows[y][x]
            if ch == " ":
                if current_color is not None:
                    parts.append(RESET)
                    current_color = None
                parts.append(" ")
            else:
                if color != current_color:
                    parts.append(color)
                    current_color = color
                parts.append(ch)
        if current_color is not None:
            parts.append(RESET)
        lines.append("".join(parts))

    return HOME + "\n".join(lines)


def run(fps: float = 20.0):
    """매트릭스 레인 애니메이션을 시작한다. Ctrl+C로 종료."""
    size = shutil.get_terminal_size(fallback=(80, 24))
    width, height = size.columns, size.lines - 1
    columns = [_Column(x, height) for x in range(width)]

    def handle_resize(signum=None, frame=None):
        nonlocal width, height, columns
        s = shutil.get_terminal_size(fallback=(80, 24))
        width, height = s.columns, s.lines - 1
        columns = [_Column(x, height) for x in range(width)]

    if hasattr(signal, "SIGWINCH"):
        signal.signal(signal.SIGWINCH, handle_resize)

    sys.stdout.write(HIDE_CURSOR + CLEAR_SCREEN)
    sys.stdout.flush()

    try:
        while True:
            sys.stdout.write(_build_frame(columns, width, height))
            sys.stdout.flush()
            for col in columns:
                col.step()
                if col.y - col.length > height:
                    col.reset(height)
                elif random.random() < 0.002:
                    col.reset(height)
            time.sleep(1.0 / fps)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(RESET + SHOW_CURSOR + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    run()
