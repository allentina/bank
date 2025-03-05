"""
Модуль my_funcs.py
"""

import re


def sum_divisible_by_3_or_5(n: int) -> int:
    """
    Сумма чисел 1..n, кратных 3 или 5
    """
    total = 0
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


def check_email(email: str) -> bool:
    """
    Простейшая проверка email
    """
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def count_number_in_list(lst: list[int], x: int) -> int:
    return lst.count(x)


def calculate_area(width: float, height: float) -> float:
    return width * height
