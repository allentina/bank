"""
Модуль для конвертации валют (пример, типизирован).
"""

import os
import requests
from typing import Dict, Any, Optional


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Пример функции, конвертирующей сумму транзакции в рубли.
    Если currency = 'RUB', возвращаем amount как есть.
    Если USD/EUR, запрашиваем курс через API (apilayer.com/exchangerates_data).

    :param transaction: словарь с транзакцией, содержит operationAmount -> {amount, currency: {code}}
    :type transaction: Dict[str, Any]
    :return: сумма в рублях
    :rtype: float
    """
    amount_str: Optional[str] = transaction.get("operationAmount", {}).get("amount")
    currency_code: Optional[str] = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not amount_str or not currency_code:
        return 0.0

    amount: float = float(amount_str)
    if currency_code == "RUB":
        return amount

    api_key: str = os.getenv("EXCHANGE_RATES_API_KEY", "")
    if not api_key:
        raise ValueError("API key not found in environment variables.")

    url = "https://api.apilayer.com/exchangerates_data/latest"
    params: Dict[str, str] = {
        "base": currency_code,
        "symbols": "RUB"
    }
    headers: Dict[str, str] = {
        "apikey": api_key
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()

    data: Dict[str, Any] = response.json()
    # Предполагаем, что data["rates"]["RUB"] точно float
    rate: float = float(data["rates"]["RUB"])
    return amount * rate
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()

    rate = data["rates"]["RUB"]
    return amount * rate
