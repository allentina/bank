"""
Модуль utils.py
"""

import json
import os
from typing import List, Dict, Any


def read_transactions_from_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список транзакций (dict).
    Если файл отсутствует, пустой или содержит не список — возвращаем [].
    """
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []
