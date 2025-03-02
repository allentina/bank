
from datetime import datetime

from src.masks import mask_card_number, mask_account_number


def mask_account_card(data: str) -> str:
    """
    Функция маскирует номер карты или счёта в переданной строке.

    Примеры входных данных:
        - "Visa Platinum 7000792289606361"
        - "Maestro 7000792289606361"
        - "Счет 73654108430135874305"

    :param data: Строка с типом и номером карты или счёта.
    :type data: str
    :return: Замаскированная строка в соответствии с видом (карта или счёт).
    :rtype: str

    Пример для карты:
        Вход:  "Visa Platinum 7000792289606361"
        Выход: "Visa Platinum 7000 79** **** 6361"

    Пример для счёта:
        Вход:  "Счет 73654108430135874305"
        Выход: "Счет **4305"
    """
    # Проверим, начинается ли строка со слова "Счет"
    if data.startswith("Счет"):
        # Тогда это счёт
        # Разделим строку по пробелам один раз, чтобы получить ["Счет", "73654108430135874305"]
        splitted = data.split(maxsplit=1)
        account_number = splitted[1]
        masked_number = mask_account_number(account_number)
        return f"{splitted[0]} {masked_number}"
    else:
        # Иначе предполагаем, что это карта (Visa, Maestro и т.п.)
        # Разделим строку справа один раз, чтобы отделить номер
        splitted = data.rsplit(" ", 1)
        card_type = splitted[0]  # "Visa Platinum" или "Maestro" и т.д.
        card_number = splitted[1]
        masked_number = mask_card_number(card_number)
        return f"{card_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата "YYYY-MM-DDTHH:MM:SS.ssssss" в формат "DD.MM.YYYY".

    Пример:
        Вход:  "2024-03-11T02:26:18.671407"
        Выход: "11.03.2024"

    :param date_string: Дата и время в ISO-формате, например "2024-03-11T02:26:18.671407"
    :type date_string: str
    :return: Строка с датой в формате "DD.MM.YYYY"
    :rtype: str
    """
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")
