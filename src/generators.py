"""
Модуль generators содержит генераторы и вспомогательные функции
для работы с банковскими транзакциями и номерами карт.
"""

from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Принимает список транзакций (список словарей) и код валюты (например, 'USD' или 'RUB').
    Возвращает итератор (генератор), который выдаёт только те транзакции,
    у которых currency['code'] == currency_code.

    :param transactions: список транзакций (каждая транзакция — словарь)
    :type transactions: List[Dict]
    :param currency_code: код валюты, например 'USD'
    :type currency_code: str
    :return: генератор транзакций подходящей валюты
    :rtype: Iterator[Dict]
    """
    for tx in transactions:
        code = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который по одному выдаёт description каждой транзакции из списка.

    :param transactions: список транзакций (каждая транзакция — словарь, где есть ключ 'description')
    :type transactions: List[Dict]
    :return: генератор строк (описаний транзакций)
    :rtype: Iterator[str]
    """
    for tx in transactions:
        desc = tx.get("description", "")
        yield desc


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, который выдаёт номера банковских карт в формате 'XXXX XXXX XXXX XXXX'.
    Диапазон — от start до stop включительно.
    Каждое число дополняется ведущими нулями до 16 цифр.

    :param start: начальное значение
    :type start: int
    :param stop: конечное значение
    :type stop: int
    :return: генератор форматированных номеров
    :rtype: Iterator[str]

    Пример:
    >>> for card in card_number_generator(1, 3):
    ...     print(card)
    0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    """
    for num in range(start, stop + 1):
        # Превращаем число в 16-значную строку с ведущими нулями
        num_str = str(num).zfill(16)
        # Делим на группы по 4 цифры
        formatted = " ".join(num_str[i:i+4] for i in range(0, 16, 4))
        yield formatted
