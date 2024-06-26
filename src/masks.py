import logging
import os
from typing import Union

# Определяем путь к папке "logs" для различных ОС
if os.name == "nt":
    project_path = "\\".join((os.path.dirname(os.path.abspath(__file__))).split("\\")[:-1])
    log_path = f"{project_path}\\logs\\"
else:
    project_path = "/".join((os.path.dirname(os.path.abspath(__file__))).split("/")[:-1])
    log_path = f"{project_path}/logs/"

# Проводим настройку логгеров для логирования в файл (уровень DEBUG) и в консоль (уровень ERROR)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
    filename=f"{log_path}masks.log",
    filemode="w",
)

# Определяем логгеры для каждой из представленных функций
card_logger = logging.getLogger("app.credit_card")
bank_logger = logging.getLogger("app.bank_account")


def credit_card_masking(number: Union[int, str]) -> str:
    """Функция возвращает маску номера кредитной карты по шаблону - 'ХХХХ ХХ** **** ХХХХ'"""
    # Проверяем на корректность введённый номер карты. Возвращаем предупреждение при непрохождении проверки.
    # В противном случае возвращаем маску.
    card_logger.info("Программа  начала работу.")
    if str(number).isdigit() and len(str(number)) == 16:
        card_logger.info("Программа успешно завершила свою работу.")
        return f"{str(number)[0:4]} {str(number)[4:6]}** **** {str(number)[-4:]}"
    else:
        card_logger.error("Введён не корректный номер кредитной карты!")
        return "Введён не корректный номер кредитной карты! Проверьте!"


def bank_account_masking(number: Union[int, str]) -> str:
    """Функция возвращает маску номера банковского счёта по шаблону - '**ХХХХ'"""
    # Проверяем на корректность введённый номер счёта. Возвращаем предупреждение при непрохождении проверки.
    # В противном случае возвращаем маску.
    bank_logger.info("Программа начала работу.")
    if str(number).isdigit() and len(str(number)) == 20:
        bank_logger.info("Программа успешно завершила свою работу.")
        return f"**{str(number)[-4:]}"
    else:
        bank_logger.error("Введён не корректный номер банковского счёта!")
        return "Введён не корректный номер банковского счёта! Проверьте!"
