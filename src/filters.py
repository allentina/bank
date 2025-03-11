
import re
from typing import List, Dict, Any
from collections import Counter


def search_transactions_by_description(
    transactions: List[Dict[str, Any]],
    search_string: str
) -> List[Dict[str, Any]]:
    """
    Ищет search_string в поле 'description' (regex, ignorecase).
    Возвращает только те транзакции, где найдена подстрока.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    result = []
    for tx in transactions:
        desc = tx.get("description", "")
        if pattern.search(desc):
            result.append(tx)
    return result


def count_operations_by_category(
    transactions: List[Dict[str, Any]],
    categories: List[str]
) -> Dict[str, int]:
    """
    Считает, сколько раз каждая категория (из списка categories)
    встречается в поле 'description' транзакции (registронезависимо).
    """
    cat_count = Counter()
    for tx in transactions:
        desc_lower = tx.get("description", "").lower()
        for cat in categories:
            if cat.lower() in desc_lower:
                cat_count[cat] += 1
    return dict(cat_count)
