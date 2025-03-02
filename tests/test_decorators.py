"""
Тесты для декораторов.
"""

import pytest
from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def multiply(a, b):
        return a * b

    result = multiply(2, 5)
    assert result == 10

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error:" in captured.out
