# src/utils.py

import json
import os
from typing import List, Dict, Any


def read_transactions_from_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Считывает JSON-файл по заданному пути и возвращает список словарей.

    :param filepath: Путь к JSON-файлу
    :type filepath: str
    :return: Список транзакций (каждая транзакция — словарь)
    :rtype: List[Dict[str, Any]]

    Если файл пустой, содержит не список или не найден, возвращается пустой список.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                # Если JSON содержит не список
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        # Если файл пустой / битый / не найден
        return []
