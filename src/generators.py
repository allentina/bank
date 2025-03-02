from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    for tx in transactions:
        code = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency_code:
            yield tx


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    for num in range(start, stop + 1):
        num_str = str(num).zfill(16)
        yield " ".join(num_str[i:i+4] for i in range(0, 16, 4))
