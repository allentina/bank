"""
Модуль functionality.py
Пример логики с несколькими ветвями.
"""

from src.decorators import log


@log()
def process_value(x: int) -> str:
    """
    - x < 0 => "Negative"
    - x == 0 => "Zero"
    - x > 0 и кратно 5 => "Positive multiple of 5"
    - x > 0 и не кратно => "Positive"
    """
    if x < 0:
        return "Negative"
    if x == 0:
        return "Zero"
    if x % 5 == 0:
        return "Positive multiple of 5"
    return "Positive"


def side_effect_function(flag: bool) -> str:
    """
    Пример дополнительной функции с ветвью.
    """
    if flag:
        return "Condition True"
    return "Condition False"
