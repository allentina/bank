import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "TX1"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "TX2"},
    ]


def test_filter_by_currency(sample_transactions: list[dict]) -> None:
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    gen = transaction_descriptions(sample_transactions)
    descs = list(gen)
    assert descs == ["TX1", "TX2"]


def test_card_number_generator() -> None:
    gen = card_number_generator(1, 2)
    cards = list(gen)
    assert cards == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002"
    ]
