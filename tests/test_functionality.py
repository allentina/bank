"""
Тесты для functionality.py
"""

import pytest
from src.functionality import process_value, side_effect_function


def test_process_value_negative() -> None:
    assert process_value(-10) == "Negative"


def test_process_value_zero() -> None:
    assert process_value(0) == "Zero"


def test_process_value_positive_5() -> None:
    assert process_value(10) == "Positive multiple of 5"


def test_process_value_positive() -> None:
    assert process_value(3) == "Positive"


@pytest.mark.parametrize("flag,expected", [
    (True, "Condition True"),
    (False, "Condition False")
])
def test_side_effect_function(flag: bool, expected: str) -> None:
    assert side_effect_function(flag) == expected
