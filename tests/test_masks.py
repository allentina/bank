from src.masks import mask_card_number, mask_account_number

def test_get_mask_card_number():
    # СТАЛО: передаем строку вместо int
    card_number = "7000792289606361"
    assert mask_card_number(card_number) == "7000 79** **** 6361"

def test_get_mask_account():
    # СТАЛО: передаем строку вместо int
    account_number = "73654108430135874305"
    assert mask_account_number(account_number) == "**4305"


def test_mask_card_number_empty():
    # если вход - пустая строка, ожидаем пустую строку
    result = mask_card_number("")
    assert result == ""


def test_mask_account_number_empty():
    # если вход - пустая строка, ожидаем пустую строку
    result = mask_account_number("")
    assert result == ""
