"""
Модуль external_api.py
"""

import os
import requests
from typing import Dict, Any, Optional


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли:
      - Если currency='RUB' -> возвращаем сумму
      - Если нет EXCHANGE_RATES_API_KEY -> ValueError
      - Если нет данных -> 0.0
      - Иначе ходим на https://api.apilayer.com/exchangerates_data
    """
    amount_str: Optional[str] = transaction.get("operationAmount", {}).get("amount")
    currency_code: Optional[str] = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not amount_str or not currency_code:
        return 0.0

    amount = float(amount_str)
    if currency_code == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY", "")
    if not api_key:
        raise ValueError("API key for exchange rates not found.")

    url = "https://api.apilayer.com/exchangerates_data/latest"
    params = {"base": currency_code, "symbols": "RUB"}
    headers = {"apikey": api_key}

    response = requests.get(url, params=params, headers=headers, timeout=5)
    response.raise_for_status()
    data = response.json()
    rate = float(data["rates"]["RUB"])
    return amount * rate
