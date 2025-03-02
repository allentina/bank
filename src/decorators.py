"""
Модуль с декоратором log, типизированный.
"""

import functools
import sys
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор, логирующий результат работы функции (или ошибку) в файл или консоль.

    :param filename: Имя файла, в который будет записан лог. Если None, логи выводятся в консоль.
    :type filename: Optional[str]
    :return: функция-декоратор
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                message = f"{func_name} ok"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_str = str(e)
                inputs_str = f"Inputs: {args}, {kwargs}"
                message = f"{func_name} error: {error_str}. {inputs_str}"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stderr)
                raise

        return wrapper

    return decorator
