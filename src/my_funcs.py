import json
import re
from typing import List, Dict, Any


def sum_divisible_by_3_or_5(n: int) -> int:
    total = 0
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


def check_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


def count_number_in_list(lst: List[int], x: int) -> int:
    return lst.count(x)


def calculate_area(width: float, height: float) -> float:
    return width * height


def read_transactions_from_json(path: str) -> List[Dict[str, Any]]:
    """
    Чтение JSON -> list[dict], если файл невалидный или не найден, возвращаем [].
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
