# src/generators.py

from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Принимает список словарей (транзакций) и код валюты.
    Возвращает итератор, выдающий только те транзакции,
    у которых currency['code'] совпадает с переданным currency_code.

    :param transactions: список транзакций (каждая транзакция — словарь)
    :param currency_code: код валюты (например, 'USD' или 'RUB')
    :return: итератор транзакций, отфильтрованных по валюте
    """
    for transaction in transactions:
        # Получаем код валюты у транзакции
        code = transaction.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который на вход принимает список транзакций,
    и при каждом вызове next(...) выдаёт очередное описание операции.

    :param transactions: список транзакций
    :return: генератор описаний (str)
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Диапазон от start до stop включительно (например, 1..5).

    :param start: начальное значение (целое число)
    :param stop: конечное значение (целое число)
    :return: генератор, выдающий отформатированные строки вида '0000 0000 0000 0001'
    """
    for num in range(start, stop + 1):
        # Превращаем число в строку длиной 16 символов (с ведущими нулями)
        # например, "1" -> "0000000000000001"
        card_str = str(num).zfill(16)

        # Форматируем строку в вид XXXX XXXX XXXX XXXX
        # берем подстроки с шагом 4
        formatted = ' '.join(card_str[i:i+4] for i in range(0, 16, 4))

        yield formatted
