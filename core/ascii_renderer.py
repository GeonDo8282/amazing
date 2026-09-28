"""
core.ascii_renderer
====================
[기능3] 3D 와이어프레임 도넛 렌더러.
Andy Sloane의 donut.c 알고리즘을 파이썬으로 포팅.
삼각함수(sin, cos)만으로 3D 토러스를 회전·음영 처리한다.
표준 라이브러리만 사용.
"""

import math
import sys
import time

HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"
HOME = "\x1b[H"
CLEAR_SCREEN = "\x1b[2J"

WIDTH = 80
HEIGHT = 22
LUMINANCE_CHARS = ".,-~:;=!*#$@"

R1 = 1.0
R2 = 2.0
K2 = 5.0
THETA_SPACING = 0.07
PHI_SPACING = 0.02


def _render_frame(A: float, B: float) -> str:
    cos_A, sin_A = math.cos(A), math.sin(A)
    cos_B, sin_B = math.cos(B), math.sin(B)

    output = [" "] * (WIDTH * HEIGHT)
    zbuffer = [0.0] * (WIDTH * HEIGHT)
    K1 = WIDTH * K2 * 3 / (8 * (R1 + R2))

    theta = 0.0
    while theta < 2 * math.pi:
        cos_theta, sin_theta = math.cos(theta), math.sin(theta)
        phi = 0.0
        while phi < 2 * math.pi:
            cos_phi, sin_phi = math.cos(phi), math.sin(phi)

            circle_x = R2 + R1 * cos_theta
            circle_y = R1 * sin_theta

            x = circle_x * (cos_B * cos_phi + sin_A * sin_B * sin_phi) - circle_y * cos_A * sin_B
            y = circle_x * (sin_B * cos_phi - sin_A * cos_B * sin_phi) + circle_y * cos_A * cos_B
            z = K2 + cos_A * circle_x * sin_phi + circle_y * sin_A
            ooz = 1 / z

            xp = int(WIDTH / 2 + K1 * ooz * x)
            yp = int(HEIGHT / 2 - K1 * ooz * y * 0.5)

            luminance = (
                cos_phi * cos_theta * sin_B
                - cos_A * cos_theta * sin_phi
                - sin_A * sin_theta
                + cos_B * (cos_A * sin_theta - cos_theta * sin_A * sin_phi)
            )

            if 0 <= xp < WIDTH and 0 <= yp < HEIGHT and luminance > 0:
                idx = xp + yp * WIDTH
                if ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    lum_index = max(0, min(len(LUMINANCE_CHARS) - 1, int(luminance * 8)))
                    output[idx] = LUMINANCE_CHARS[lum_index]

            phi += PHI_SPACING
        theta += THETA_SPACING

    rows = ["".join(output[r * WIDTH:(r + 1) * WIDTH]) for r in range(HEIGHT)]
    return HOME + "\n".join(rows) + "\n"


def run(rotation_speed: float = 1.0):
    """회전하는 3D ASCII 도넛을 렌더링한다. Ctrl+C로 종료."""
    A, B = 1.0, 1.0
    sys.stdout.write(HIDE_CURSOR + CLEAR_SCREEN)
    sys.stdout.flush()

    try:
        while True:
            sys.stdout.write(_render_frame(A, B))
            sys.stdout.flush()
            A += 0.07 * rotation_speed
            B += 0.03 * rotation_speed
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    run()
