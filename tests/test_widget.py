import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_incorrect_data():
    input_data = "НекорректныйТип 123456"
    result = mask_account_card(input_data)
    assert result == input_data  # например, проверяем, что возвращается исходная строка

def test_get_date_correct():
    input_date = "2024-03-11T02:26:18.671407"
    result = get_date(input_date)
    assert result == "11.03.2024"