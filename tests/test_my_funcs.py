"""
Тесты для my_funcs.py
"""

import pytest
from src.my_funcs import (
    sum_divisible_by_3_or_5,
    check_email,
    count_number_in_list,
    calculate_area
)


def test_sum_divisible_zero() -> None:
    assert sum_divisible_by_3_or_5(0) == 0


def test_sum_divisible_small() -> None:
    assert sum_divisible_by_3_or_5(5) == 8  # (3+5=8)
    assert sum_divisible_by_3_or_5(10) == 33


def test_check_email_valid() -> None:
    assert check_email("test@example.com")


def test_check_email_invalid() -> None:
    assert not check_email("invalid@@example..com")


def test_count_number_in_list_empty() -> None:
    assert count_number_in_list([], 5) == 0


def test_count_number_in_list_ok() -> None:
    lst = [1, 2, 2, 5, 2]
    assert count_number_in_list(lst, 2) == 3


@pytest.mark.parametrize("w,h,expected", [
    (1.0, 1.0, 1.0),
    (2.0, 5.0, 10.0),
    (3.14, 2.0, 6.28),
    (10.0, 4.2, 42.0),
])
def test_calculate_area(w: float, h: float, expected: float) -> None:
    res = calculate_area(w, h)
    assert abs(res - expected) < 1e-9