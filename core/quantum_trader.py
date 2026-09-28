"""
core.quantum_trader
====================
[기능2] 퀀텀 알고리즘 트레이딩 시뮬레이터 (가짜).
math.sin 기반 노이즈로 실시간 자산 가격 변동을 그럴싸하게 그린다.
표준 라이브러리만 사용.
"""

import math
import random
import shutil
import sys
import time

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
GREEN = "\x1b[32m"
RED = "\x1b[31m"
CYAN = "\x1b[36m"
YELLOW = "\x1b[33m"
MAGENTA = "\x1b[35m"
GRAY = "\x1b[90m"
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
CLEAR_SCREEN = "\x1b[2J"
HOME = "\x1b[H"

TICKERS = ["QNTX", "ARBX", "NRAL", "SYNQ", "VECT", "HLIX", "ZEN0", "FLUX"]

FAKE_LOG_MESSAGES = [
    "레이턴시 최적화: {n}ns 단축",
    "오더북 스캔 완료 ({n}개 거래소)",
    "차익거래 기회 탐색 중...",
    "슬리피지 보정 계수 재계산",
    "신경망 가중치 미세조정 (epoch {n})",
    "리스크 헤지 포지션 재조정",
    "다크풀 유동성 확인",
    "스프레드 임계값 갱신: {n}bps",
    "몬테카를로 시뮬레이션 {n}회 수행",
    "양자 난수 생성기 시드 리프레시",
]


class _Asset:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.price = random.uniform(50, 5000)
        self.phase = random.uniform(0, math.tau)
        self.freq = random.uniform(0.05, 0.2)
        self.vol = random.uniform(0.002, 0.02)
        self.t = 0.0
        self.history = [self.price] * 30
        self.change_pct = 0.0

    def step(self):
        self.t += 1
        wave = math.sin(self.t * self.freq + self.phase)
        wave += 0.3 * math.sin(self.t * self.freq * 2.7 + self.phase)
        noise = random.gauss(0, self.vol)
        prev = self.price
        self.price = max(0.01, self.price * (1 + wave * self.vol + noise))
        self.change_pct = (self.price - prev) / prev * 100
        self.history.append(self.price)
        if len(self.history) > 40:
            self.history.pop(0)

    def sparkline(self, width: int) -> str:
        data = self.history[-width:]
        if len(data) < 2:
            return " " * width
        lo, hi = min(data), max(data)
        blocks = " ▁▂▃▄▅▆▇█"
        span = (hi - lo) or 1
        return "".join(
            blocks[int((v - lo) / span * (len(blocks) - 1))] for v in data
        ).rjust(width)


def _render(assets, log_lines, width, tick):
    lines = []
    title = " QUANTUM ALGORITHMIC TRADING ENGINE — v4.7.2 "
    pad = max(0, (width - len(title)) // 2)
    lines.append(f"{BOLD}{CYAN}{'═' * width}{RESET}")
    lines.append(f"{BOLD}{CYAN}{' ' * pad}{title}{RESET}")
    lines.append(f"{CYAN}{'═' * width}{RESET}")
    lines.append(
        f"{GRAY}TICK #{tick:06d}  |  THREADS: 512  |  EXCHANGES: 34  |  "
        f"LATENCY: {random.randint(80, 240)}μs{RESET}"
    )
    lines.append("")
    header = f"{'TICKER':<8}{'PRICE':>12}{'CHG%':>9}   {'TREND (40 ticks)'}"
    lines.append(f"{BOLD}{header}{RESET}")
    lines.append(f"{GRAY}{'-' * width}{RESET}")

    for a in assets:
        color = GREEN if a.change_pct >= 0 else RED
        arrow = "▲" if a.change_pct >= 0 else "▼"
        spark_width = max(10, width - 34)
        spark = a.sparkline(spark_width)
        lines.append(
            f"{BOLD}{a.ticker:<8}{RESET}"
            f"{a.price:>12,.2f}"
            f"{color}{arrow}{abs(a.change_pct):>6.2f}%{RESET}   "
            f"{color}{spark}{RESET}"
        )

    lines.append("")
    lines.append(f"{YELLOW}{'-' * width}{RESET}")
    lines.append(f"{BOLD}SYSTEM LOG{RESET}")
    for msg in log_lines[-6:]:
        lines.append(f"{GRAY}› {msg}{RESET}")

    portfolio_value = sum(a.price for a in assets) * random.uniform(0.8, 1.2)
    lines.append("")
    lines.append(
        f"{MAGENTA}PORTFOLIO VALUE: ${portfolio_value:,.2f}   "
        f"P/L: {random.choice([GREEN, RED])}{random.uniform(-3, 5):+.2f}%{RESET}"
    )

    return HOME + "\n".join(lines) + "\n"


def run(interval: float = 0.4):
    """퀀텀 트레이딩 대시보드를 시작한다. Ctrl+C로 종료."""
    size = shutil.get_terminal_size(fallback=(100, 30))
    width = size.columns

    assets = [_Asset(t) for t in TICKERS]
    log_lines = []
    tick = 0

    sys.stdout.write(HIDE_CURSOR + CLEAR_SCREEN)
    sys.stdout.flush()

    try:
        while True:
            tick += 1
            for a in assets:
                a.step()
            if random.random() < 0.6:
                template = random.choice(FAKE_LOG_MESSAGES)
                log_lines.append(template.format(n=random.randint(1, 9999)))

            sys.stdout.write(_render(assets, log_lines, width, tick))
            sys.stdout.flush()
            time.sleep(interval)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(RESET + SHOW_CURSOR + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    run()
