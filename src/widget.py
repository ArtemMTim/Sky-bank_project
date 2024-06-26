# Импортируем необходимые модули
from datetime import datetime

from src.masks import bank_account_masking, credit_card_masking


def masking_with_info(number: str) -> str:
    """Функция принимает на вход сообщение вида: '<Вид банковской карты/счет> <номер>' и
    выводит замаскированный счёт карты/банковского счёта
    в соответсвии с шаблоном: '<Вид банковской карты/счет> <*****>'
    """
    # Разбиваем вводные данные на вид банковской карты/счет и номер
    number_info = number.split()
    # Проверяем введён ли вид банковской карты/счет.
    # В случае отсутствия вида банковской карты/счета выводим сообщение об ошибке в введённых данных.
    if len(number_info) == 1:
        result_message = "Ошибка в введённых данных!"
    else:
        # Проверяем, какой номер был введён: карты либо банковского счёта.
        # Выбираем необходимую функцию из модуля "masks".
        # Применяем функции из модуля "masks".
        # Проверяем результат работы функции маскировки: сообщение об ошибке либо маска.
        # Формируем и выводим результирующее сообщение.
        if number_info[0] == "Счет" or number_info[0] == "Счёт":
            if "*" in bank_account_masking(number_info[-1]):
                result_message = f"{number_info[0]} {bank_account_masking(number_info[-1])}"
            else:
                result_message = bank_account_masking(number_info[-1])
        else:
            if "*" in credit_card_masking(number_info[-1]):
                result_message = f"{' '.join(number_info[:-1])} {credit_card_masking(number_info[-1])}"
            else:
                result_message = credit_card_masking(number_info[-1])
    return result_message


def date_formatting(date_string: str) -> str:
    """Функция получает дату и время в ISO формате и выводит в соответствии с шаблоном: 'day.month.year'"""
    # Преобразуем ISO строку в объект datetime.
    date_time = datetime.fromisoformat(date_string)
    # Форматируем вывод под заданный шаблон.
    return date_time.strftime("%d.%m.%Y")
