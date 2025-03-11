"""
Модуль generators.py
"""

from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], code: str) -> Iterator[Dict]:
    for tx in transactions:
        c = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if c == code:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    for num in range(start, stop + 1):
        s = str(num).zfill(16)
        # Убираем лишние пробелы (E203) вокруг ':'
        yield " ".join(s[i:i+4] for i in range(0, 16, 4))
