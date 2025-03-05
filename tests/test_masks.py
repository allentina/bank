"""
Тесты для masks.py
"""

from src.masks import mask_card_number, mask_account_number


def test_mask_card_number_normal() -> None:
    assert mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_mask_card_number_empty() -> None:
    assert mask_card_number("") == ""


def test_mask_card_number_short() -> None:
    assert mask_card_number("12345") == "**12345"


def test_mask_account_number_normal() -> None:
    assert mask_account_number("9876543210") == "**43210"


def test_mask_account_number_empty() -> None:
    assert mask_account_number("") == ""


def test_mask_account_number_short() -> None:
    assert mask_account_number("123") == "**123"
