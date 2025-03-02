import pytest
from src.masks import mask_card_number, mask_account_number

def test_mask_card_number() -> None:
    card = "1234567890123456"
    result = mask_card_number(card)
    assert "1234" in result


def test_mask_card_number_empty() -> None:
    result = mask_card_number("")
    assert result == ""


def test_mask_account_number() -> None:
    acc = "9876543210"
    result = mask_account_number(acc)
    assert result == "**3210"


def test_mask_account_number_empty() -> None:
    result = mask_account_number("")
    assert result == ""
