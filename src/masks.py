def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    """
    if not card_number:
        return ""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта.
    """
    if not account_number:
        return ""
    return f"**{account_number[-4:]}"
