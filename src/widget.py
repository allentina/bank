"""
Модуль widget.py
"""

from src.masks import mask_card_number, mask_account_number


def mask_account_card(data: str) -> str:
    """
    Определяет формат (счет или карта) и маскирует соответствующим образом.
    Если формат нераспознан, возвращает исходную строку.
    """
    if data.startswith("Счет"):
        # "Счет" => маскируем как счёт
        splitted = data.split(maxsplit=1)  # ["Счет", "75106830613657916952"]
        if len(splitted) == 2:
            return splitted[0] + " " + mask_account_number(splitted[1])
        return data  # если вдруг чего-то нет

    # Пусть если не "Счет", то считаем "Карта" (либо неизвестный формат).
    # Но в вашем тесте неизвестный формат => возвращаем data.
    if not data.startswith("Карта"):
        return data

    # Если всё же "Карта", отделяем последний блок для маскирования
    splitted = data.rsplit(" ", 1)
    if len(splitted) == 2:
        return splitted[0] + " " + mask_card_number(splitted[1])
    return data
