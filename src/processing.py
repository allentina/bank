from datetime import datetime
from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по ключу 'state'.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    При некорректном формате даты должно выбрасываться ValueError (из datetime.fromisoformat).
    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x['date']),  # при 'НекорректнаяДата' будет ValueError
        reverse=reverse
    )
