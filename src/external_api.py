import os
import requests
from typing import Dict, Any

def convert_to_rub(transaction: Dict[str, Any]) -> float:
    # ... логика обращения к API ...
    pass


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает словарь-транзакцию и возвращает сумму (ключ 'amount') в рублях (float).
    Если валюта 'USD' или 'EUR', происходит обращение к внешнему API для получения курса.
    Если валюта уже 'RUB', возвращается значение 'amount' как float без обращения к API.

    :param transaction: словарь с данными операции
    :type transaction: Dict[str, Any]
    :return: Сумма транзакции в рублях (float)
    :rtype: float
    """
    amount_str: Optional[str] = transaction.get("operationAmount", {}).get("amount")
    currency_code: Optional[str] = transaction.get("operationAmount", {}).get("currency", {}).get("code")
    if not amount_str or not currency_code:
        # Если данных нет, вернем 0.0 или другое поведение
        return 0.0

    # Преобразуем сумму к float
    amount = float(amount_str)

    if currency_code == "RUB":
        return amount

    # Если валюта USD или EUR, нужно сконвертировать
    api_key = os.getenv("EXCHANGE_RATES_API_KEY", "")
    if not api_key:
        # Если ключа нет, можно либо вернуть 0.0, либо бросить исключение
        raise ValueError("API key for exchange rates not found in environment variables.")

    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    # Например, хотим получить курс RUB относительно USD/EUR
    # Параметр base= указывает, по какой валюте давать курсы
    # Параметр symbols=RUB указывает, что нам нужен курс RUB

    params = {
        "base": currency_code,
        "symbols": "RUB"
    }

    headers = {
        "apikey": api_key
    }

    response = requests.get(base_url, params=params, headers=headers, timeout=10)
    response.raise_for_status()  # Если код != 200, выкинется исключение

    data = response.json()
    # В data["rates"]["RUB"] хранится курс 1 <currency_code> к рублю
    rate_rub = data["rates"]["RUB"]
    # Конвертируем
    rubles = amount * rate_rub
    return rubles
