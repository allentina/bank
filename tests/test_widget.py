"""
Тесты для widget.py
"""

# import pytest  # Убираем, если не используем pytest.raises или маркировки

from src.widget import mask_account_card, get_date


def test_mask_account_card_incorrect_data():
    input_data = "НекорректныйТип 123456"
    result = mask_account_card(input_data)
    assert result == input_data


def test_get_date_correct():
    input_date = "2025-01-01T12:00:00.123456"
    result = get_date(input_date)
    assert result == "01.01.2025"
