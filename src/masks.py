def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    :param card_number: Строка с номером карты, например '7000792289606361'.
    :return: Маскированная строка, например '7000 79** **** 6361'.
    """
    # Для примера берём формат: 4 цифры, пробел, 2 цифры, '**', '****', и последние 4 цифры
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта.

    :param account_number: Строка с номером счёта, например '73654108430135874305'.
    :return: Маскированная строка, например '**4305'.
    """
    return f"**{account_number[-4:]}"

