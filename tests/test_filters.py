
from src.filters import search_transactions_by_description, count_operations_by_category

def test_search_transactions_by_description() -> None:
    txs = [
        {"description": "Перевод со счета"},
        {"description": "Оплата услуг"},
        {"description": "Перевод организации"},
    ]
    res = search_transactions_by_description(txs, "перевод")
    assert len(res) == 2

def test_count_operations_by_category() -> None:
    txs = [
        {"description": "Перевод со счета"},
        {"description": "Оплата услуг"},
        {"description": "Вклад"},
        {"description": "Перевод org"},
    ]
    cats = ["Перевод", "Оплата", "Вклад"]
    result = count_operations_by_category(txs, cats)
    assert result["Перевод"] == 2
    assert result["Оплата"] == 1
    assert result["Вклад"] == 1
