"""
Модуль masks.py
"""

def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Если карта короче 16 символов, возвращает "**" + card_number.
    Если пустая строка, вернёт "".
    """
    if not card_number:
        return ""
    if len(card_number) < 16:
        return f"**{card_number}"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта, добавляя '**' + последние 5 цифр.
    Если короче 5, вернёт "**" + account_number.
    Если пустая строка => "".
    """
    if not account_number:
        return ""
    if len(account_number) < 5:
        return f"**{account_number}"
    return f"**{account_number[-5:]}"
