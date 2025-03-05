
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Возвращает список словарей, у которых state соответствует указанному.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    from datetime import datetime
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x['date']),
        reverse=reverse
    )
