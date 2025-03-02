"""
Тесты для модуля generators.py:
filter_by_currency, transaction_descriptions, card_number_generator
"""

import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"code": "USD"}
            },
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert len(result) == 2
    assert [tx["id"] for tx in result] == [1, 3]


def test_filter_by_currency_rub(sample_transactions):
    gen = filter_by_currency(sample_transactions, "RUB")
    result = list(gen)
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_transaction_descriptions(sample_transactions):
    gen = transaction_descriptions(sample_transactions)
    result = list(gen)
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_card_number_generator():
    gen = card_number_generator(1, 3)
    result = list(gen)
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
