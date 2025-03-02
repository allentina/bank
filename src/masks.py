"""
Модуль masks: функции для маскирования номеров карт и счетов с логированием.
"""

import os
import logging

from typing import Any

# Создаем папку logs, если отсутствует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логгера для модуля masks
logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler: logging.FileHandler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter: logging.Formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    :param card_number: Номер карты в виде строки, например "7000792289606361".
    :type card_number: str
    :return: Замаскированный номер карты, например "7000 79** **** 6361".
    :rtype: str
    """
    try:
        if not card_number:
            logger.error("Empty card number provided.")
            return ""
        result: str = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"mask_card_number successful: {result}")
        return result
    except Exception as e:
        logger.error(f"mask_card_number error: {str(e)}. Inputs: {card_number}")
        raise


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счета.

    :param account_number: Номер счета в виде строки.
    :type account_number: str
    :return: Замаскированный номер счета, например "**4305".
    :rtype: str
    """
    try:
        if not account_number:
            logger.error("Empty account number provided.")
            return ""
        result: str = f"**{account_number[-4:]}"
        logger.info(f"mask_account_number successful: {result}")
        return result
    except Exception as e:
        logger.error(f"mask_account_number error: {str(e)}. Inputs: {account_number}")
        raise
