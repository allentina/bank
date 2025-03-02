import json
import os
from typing import List, Dict, Any

def read_transactions_from_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл по заданному пути и возвращает список транзакций.

    :param filepath: путь к JSON-файлу
    :type filepath: str
    :return: список транзакций, если файл существует и содержит список, иначе []
    :rtype: List[Dict[str, Any]]
    """
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
