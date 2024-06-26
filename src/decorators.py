from functools import wraps
from typing import Any, Callable


# Декоратор производящий логирование работы декорируемой функции в файл, если передано название,
# либо в консоль.
def log(filename: str = "") -> Any:
    """Декоратор принимает функцию. Проводит логирование результата её работы в консоль либо
    в заданный в качестве необязательного параметра файл. При положительной отработке функции
    возвращает результат."""

    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                stop_massage = f"{func.__name__} ok"
                if filename:
                    with open(filename, "w", encoding="UTF-8") as file_out:
                        file_out.write(stop_massage)
                else:
                    print(stop_massage)
                return result
            except Exception as err:
                error_message = f"{func.__name__}: {err}. Inputs: {args}, {kwargs}."
                if filename:
                    with open(filename, "w", encoding="UTF-8") as file_out:
                        file_out.write(error_message)
                else:
                    print(error_message)

        return inner

    return wrapper
