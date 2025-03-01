# src/decorators.py

import functools
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, логирующий результат работы функции либо ошибку при её выполнении.

    :param filename: Имя файла, в который будет записан лог.
                     Если None, то вывод идёт в консоль.
    :type filename: Optional[str]
    :return: Декорирующая функция
    :rtype: Callable
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            try:
                # Вызов оригинальной функции
                result = func(*args, **kwargs)

                # Формируем сообщение об успешном выполнении
                message = f"{func_name} ok"
                if filename:
                    # Записываем в файл
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + "\n")
                else:
                    # Выводим в консоль
                    print(message)

                return result
            except Exception as e:
                # Формируем сообщение при ошибке
                error_type = str(e)  # Можно и type(e).__name__, если нужен тип без описания
                inputs_str = f"Inputs: {args}, {kwargs}"
                message = f"{func_name} error: {error_type}. {inputs_str}"

                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + "\n")
                else:
                    print(message)

                # Повторно бросаем исключение, чтобы не скрывать ошибку
                raise

        return wrapper

    return decorator
