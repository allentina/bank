# tests/test_decorators.py

import pytest
import os
from src.decorators import log


# Для проверки вывода в консоль используем capsys
def test_log_to_console_success(capsys):
    @log()
    def multiply(a, b):
        return a * b

    result = multiply(2, 5)
    assert result == 10

    captured = capsys.readouterr()
    # Проверяем, что в консоль вывелось "multiply ok"
    assert "multiply ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    # Проверяем, что декоратор вывел сообщение об ошибке
    assert "divide error: division by zero. Inputs: (1, 0)," in captured.out


def test_log_to_file_success(tmp_path):
    """
    Проверяем запись в файл при успешной работе функции.
    """
    logfile = tmp_path / "testlog.txt"

    @log(filename=str(logfile))
    def summation(a, b):
        return a + b

    summation(3, 7)  # ожидаем "summation ok"
    with open(logfile, 'r', encoding='utf-8') as f:
        contents = f.read()
    assert "summation ok" in contents


def test_log_to_file_error(tmp_path):
    """
    Проверяем запись в файл при ошибке.
    """
    logfile = tmp_path / "errorlog.txt"

    @log(filename=str(logfile))
    def do_something_wrong(x):
        return 10 / x  # Может привести к делению на 0

    with pytest.raises(ZeroDivisionError):
        do_something_wrong(0)

    with open(logfile, 'r', encoding='utf-8') as f:
        contents = f.read()

    # Проверяем, что записано сообщение об ошибке
    assert "do_something_wrong error: division by zero. Inputs: (0,)," in contents
