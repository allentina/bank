"""
Тесты для widget.py
"""

from src.widget import mask_account_card


def test_mask_account_card_incorrect_data() -> None:
    input_data = "НекорректныйТип 123456"
    result = mask_account_card(input_data)
    # Тест разрешает либо полностью замаскированный вариант (16 цифр),
    # либо вернуть исходную строку "НекорректныйТип 123456".
    assert result == "НекорректныйТип 1234 56** **** 3456" or result == input_data
