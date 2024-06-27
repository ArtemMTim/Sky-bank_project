import logging
from typing import Union

from config import MASKS_LOGS

# Проводим настройку логгеров для логирования в файл (уровень DEBUG) и в консоль (уровень ERROR)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(MASKS_LOGS, mode="w")
file_formatter = logging.Formatter(
    "%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s",
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Определяем логгеры для каждой из представленных функций
card_logger = logging.getLogger("app.credit_card")
bank_logger = logging.getLogger("app.bank_account")


def credit_card_masking(number: Union[int, str]) -> str:
    """Функция возвращает маску номера кредитной карты по шаблону - 'ХХХХ ХХ** **** ХХХХ'"""
    # Проверяем на корректность введённый номер карты. Возвращаем предупреждение при непрохождении проверки.
    # В противном случае возвращаем маску.
    logger.info("Программа  начала работу.")
    if str(number).isdigit() and len(str(number)) == 16:
        logger.info("Программа успешно завершила свою работу.")
        return f"{str(number)[0:4]} {str(number)[4:6]}** **** {str(number)[-4:]}"
    else:
        logger.error("Введён не корректный номер кредитной карты!")
        return "Введён не корректный номер кредитной карты! Проверьте!"


def bank_account_masking(number: Union[int, str]) -> str:
    """Функция возвращает маску номера банковского счёта по шаблону - '**ХХХХ'"""
    # Проверяем на корректность введённый номер счёта. Возвращаем предупреждение при непрохождении проверки.
    # В противном случае возвращаем маску.
    logger.info("Программа начала работу.")
    if str(number).isdigit() and len(str(number)) == 20:
        logger.info("Программа успешно завершила свою работу.")
        return f"**{str(number)[-4:]}"
    else:
        logger.error("Введён не корректный номер банковского счёта!")
        return "Введён не корректный номер банковского счёта! Проверьте!"
