
from src.masks import mask_card_number, mask_account_number


def mask_account_card(data: str) -> str:
    """
    Определяет, карта или счёт, и маскирует соответствующим образом.
    """
    if data.startswith("Счет"):
        splitted = data.split(maxsplit=1)
        return f"{splitted[0]} {mask_account_number(splitted[1])}"
    splitted = data.rsplit(" ", 1)
    return f"{splitted[0]} {mask_card_number(splitted[1])}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату ISO в формат DD.MM.YYYY.
    """
    from datetime import datetime
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
