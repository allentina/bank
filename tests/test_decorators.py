"""
Тесты для decorators.py
"""

import pytest
from pathlib import Path
from src.decorators import log


def test_log_to_console_ok(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert "[OK] add finished successfully." in captured.out


def test_log_to_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    @log()
    def div(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)
    captured = capsys.readouterr()
    assert "[ERROR] div failed:" in captured.err


def test_log_to_file_ok(tmp_path: Path) -> None:
    logfile = tmp_path / "log_ok.txt"

    @log(filename=str(logfile))
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)
    contents = logfile.read_text(encoding="utf-8")
    assert "[OK] multiply finished successfully." in contents


def test_log_to_file_error(tmp_path: Path) -> None:
    logfile = tmp_path / "log_err.txt"

    @log(filename=str(logfile))
    def failing_func() -> None:
        raise ValueError("Custom error")

    with pytest.raises(ValueError, match="Custom error"):
        failing_func()

    text = logfile.read_text(encoding="utf-8")
    assert "[ERROR] failing_func failed: Custom error" in text
