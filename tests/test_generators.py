"""
Тесты для generators.py
"""

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            },
            "description": "Перевод 1",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "RUB"}
            },
            "description": "Перевод 2",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"code": "USD"}
            },
            "description": "Перевод 3",
        },
    ]


def test_filter_by_currency_usd(sample_transactions: list[dict]) -> None:
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    gen = transaction_descriptions(sample_transactions)
    descs = list(gen)
    assert descs == ["Перевод 1", "Перевод 2", "Перевод 3"]


def test_card_number_generator() -> None:
    gen = card_number_generator(1, 1)
    result = list(gen)
    # 1 -> "0000 0000 0000 0001"
    assert result == ["0000 0000 0000 0001"]
