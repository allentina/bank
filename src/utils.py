"""
Модуль utils: функции для работы с файлами и логирования.
"""

import json
import os
import logging
from typing import List, Dict, Any

# Создаем папку logs, если она отсутствует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логгера для модуля utils
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler: logging.FileHandler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_from_json(filepath: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл по заданному пути и возвращает список транзакций.

    :param filepath: Путь к JSON-файлу.
    :type filepath: str
    :return: Список транзакций (если файл отсутствует – возвращается пустой список).
    :rtype: List[Dict[str, Any]]
    """
    try:
        if not os.path.exists(filepath):
            logger.error(f"File not found: {filepath}")
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Successfully read {len(data)} transactions from {filepath}")
                return data
            else:
                logger.error(f"Data in {filepath} is not a list")
                return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in file {filepath}: {str(e)}")
        return []
    except Exception as e:
        logger.error(f"Error reading file {filepath}: {str(e)}")
        return []
