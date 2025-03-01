def mask_card_number(card_number: str) -> str:

    """
    Маскирует номер карты.
    Пример:
      Вход:  '7000792289606361'
      Выход: '7000 79** **** 6361'
    """
    # Проверка на пустую строку
    if not card_number:
        return ""
    # Основная логика: [0:4], [4:6], '**', '****', [-4:]
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта.
    Пример:
      Вход:  '73654108430135874305'
      Выход: '**4305'
    """
    # Проверка на пустую строку
    if not account_number:
        return ""
    return f"**{account_number[-4:]}"

