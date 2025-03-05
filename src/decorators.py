"""
Модуль decorators.py
Логирующий декоратор @log
"""

import functools
import sys
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор, логирующий результат работы функции:
    - При успехе -> "[OK] func_name finished successfully."
    - При ошибке -> "[ERROR] func_name failed: ..."
    Если filename=None, выводим в консоль, иначе дописываем в файл.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                result = func(*args, **kwargs)
                msg_ok = f"[OK] {func_name} finished successfully."
                if filename is None:
                    print(msg_ok)
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg_ok + "\n")
                return result
            except Exception as e:
                msg_err = f"[ERROR] {func_name} failed: {e}"
                if filename is None:
                    print(msg_err, file=sys.stderr)
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(msg_err + "\n")
                raise
        return wrapper
    return decorator
