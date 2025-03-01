from src.masks import mask_account_number, mask_card_number


def mask_account_card(data: str) -> str:
    """
    Определяет, карта или счёт, и маскирует соответствующим образом.
    Если не распознаёт тип, возвращает исходную строку.
    """
    if data.startswith("Счет"):
        splitted = data.split(maxsplit=1)
        return f"{splitted[0]} {mask_account_number(splitted[1])}"
    elif any(word in data for word in ("Visa", "MasterCard", "Maestro")):
        splitted = data.rsplit(" ", 1)
        return f"{splitted[0]} {mask_card_number(splitted[1])}"
    else:
        return data


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO-строки в формат DD.MM.YYYY.
    """
    from datetime import datetime
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
