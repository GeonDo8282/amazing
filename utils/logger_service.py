"""
utils.logger_service
======================
컬러 콘솔 로거. 실제로 동작하는 유일한 "진지한" 유틸리티.
"""

import sys
import time

_LEVEL_COLORS = {
    "INFO": "\x1b[36m",
    "WARN": "\x1b[33m",
    "ERROR": "\x1b[31m",
    "DEBUG": "\x1b[90m",
    "SUCCESS": "\x1b[32m",
}
_RESET = "\x1b[0m"


class Logger:
    def __init__(self, name: str = "NEXUS"):
        self.name = name

    def _emit(self, level: str, message: str):
        color = _LEVEL_COLORS.get(level, "")
        ts = time.strftime("%H:%M:%S")
        sys.stdout.write(f"{color}[{ts}] [{self.name}] [{level}] {message}{_RESET}\n")
        sys.stdout.flush()

    def info(self, message: str):
        self._emit("INFO", message)

    def warn(self, message: str):
        self._emit("WARN", message)

    def error(self, message: str):
        self._emit("ERROR", message)

    def debug(self, message: str):
        self._emit("DEBUG", message)

    def success(self, message: str):
        self._emit("SUCCESS", message)


default_logger = Logger()
