#from datetime import datetime
from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Возвращает новый список словарей из 'data',
    содержащий только те элементы, где значение по ключу 'state' равно указанному.

    :param data: Исходный список словарей. Пример:
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    :type data: List[Dict]
    :param state: Значение ключа 'state', которое нужно найти. По умолчанию 'EXECUTED'.
    :type state: str
    :return: Отфильтрованный список словарей.
    :rtype: List[Dict]
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Возвращает новый список словарей из 'data', отсортированных по ключу 'date'.

    :param data: Исходный список словарей.
    :type data: List[Dict]
    :param reverse: Порядок сортировки. True = по убыванию (самые свежие даты в начале).
                    False = по возрастанию (самые старые даты в начале).
                    По умолчанию True.
    :type reverse: bool
    :return: Отсортированный по дате список словарей.
    :rtype: List[Dict]
    """
    # Преобразуем строку даты в datetime-объект для корректной сортировки
    # date в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    # Например: "2019-07-03T18:35:29.512364"
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
