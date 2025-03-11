"""
Модуль masks.py
"""


def mask_card_number(card_number: str) -> str:
    """
    Маскирует карту:
      - Если пустая -> ""
      - Если <16 -> "**" + card_number
      - Иначе -> "XXXX XX** **** XXXX"
    """
    if not card_number:
        return ""
    if len(card_number) < 16:
        return f"**{card_number}"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует счёт:
      - Если пустой -> ""
      - Если <5 -> "**" + account_number
      - Иначе -> "**" + последние 5 цифр
    """
    if not account_number:
        return ""
    if len(account_number) < 5:
        return f"**{account_number}"
    return f"**{account_number[-5:]}"
