
import pytest
from pathlib import Path
from src.decorators import log


def test_log_to_file_success(tmp_path: Path) -> None:
    """
    Пример теста, проверяющего запись в файл при успехе.
    """
    logfile = tmp_path / "testlog.txt"

    @log(filename=str(logfile))
    def summation(a: int, b: int) -> int:
        return a + b

    summation(3, 4)
    contents = logfile.read_text(encoding="utf-8")
    assert "summation ok" in contents


def test_log_to_file_error(tmp_path: Path) -> None:
    """
    Пример теста, проверяющего запись в файл при ошибке.
    """
    logfile = tmp_path / "errorlog.txt"

    @log(filename=str(logfile))
    def problematic(x: int) -> float:
        return 10 / x

    with pytest.raises(ZeroDivisionError):
        problematic(0)

    contents = logfile.read_text(encoding="utf-8")
    assert "problematic error:" in contents
