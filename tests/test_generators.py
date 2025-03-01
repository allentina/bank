# tests/test_generators.py

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    """
    Фикстура: возвращает список транзакций для тестов.
    """
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
        }
    ]


@pytest.mark.parametrize("currency_code, expected_count", [
    ("USD", 2),
    ("RUB", 1),
    ("EUR", 0),   # нет транзакций в евро
])
def test_filter_by_currency(sample_transactions, currency_code, expected_count):
    gen = filter_by_currency(sample_transactions, currency_code)
    result_list = list(gen)  # преобразуем итератор в список
    assert len(result_list) == expected_count


def test_filter_by_currency_empty():
    # Пустой список транзакций
    transactions = []
    gen = filter_by_currency(transactions, "USD")

    # Превращаем в список, ожидаем пустой
    assert list(gen) == []


def test_transaction_descriptions(sample_transactions):
    # Получаем генератор
    gen = transaction_descriptions(sample_transactions)
    # Превращаем в список, получаем все описания
    descriptions = list(gen)
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty():
    # Пустой список транзакций
    gen = transaction_descriptions([])
    # Ожидаем пустой список описаний
    assert list(gen) == []


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
])
def test_card_number_generator(start, stop, expected):
    gen = card_number_generator(start, stop)
    result_list = list(gen)
    assert result_list == expected


def test_card_number_generator_large_range():
    # Проверим конец диапазона, например, с 9999999999999998 до 10000000000000000
    # но такой range огромный: для теста возьмем что-то поменьше
    gen = card_number_generator(9999999999999998, 10000000000000000)
    # Возьмем только первые несколько карт
    # (при желании, можно использовать islice для больших данных)
    results = []
    for _ in range(3):
        results.append(next(gen))
    assert results == [
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
        "1000 0000 0000 0000",
    ]
