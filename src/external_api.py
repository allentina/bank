
import os
import requests
from typing import Dict, Any


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию в виде словаря и возвращает сумму (ключ 'amount')
    в рублях (float). Если транзакция в USD или EUR, обращается к внешнему API
    для получения текущего курса валют.

    :param transaction: Словарь с данными транзакции, содержащий ключи:
                        operationAmount -> { amount, currency: { code } }
    :type transaction: Dict[str, Any]
    :return: Сумма транзакции в рублях
    :rtype: float
    :raises ValueError: Если API-ключ не найден в переменных окружения.
    """
    amount_str = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not amount_str or not currency_code:
        return 0.0

    amount = float(amount_str)
    if currency_code == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY", "")
    if not api_key:
        raise ValueError("API key for exchange rates not found in environment variables.")

    url = "https://api.apilayer.com/exchangerates_data/latest"
    params = {
        "base": currency_code,
        "symbols": "RUB"
    }
    headers = {
        "apikey": api_key
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    rate = float(data["rates"]["RUB"])
    return amount * rate
