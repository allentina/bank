"""
Модуль generators.py
"""

from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает транзакции, у которых code == currency_code.
    """
    for tx in transactions:
        code = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор description из каждой транзакции.
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.
    """
    for num in range(start, stop + 1):
        s = str(num).zfill(16)
        yield " ".join(s[i : i + 4] for i in range(0, 16, 4))
