# Импортируем необходимые библиотеки
from typing import Generator, Iterator, List


def filter_by_currency(transactions: List[dict], currency: str) -> Iterator:
    """Функция принимает список словарей (информация о транзакциях) и название валюты,
    возвращает итератор с отфильтрованными по заданной валюте транзакциями"""
    return filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions)


def description(transactions: List[dict]) -> Generator:
    """Функция принимает список словарей, возвращает генератор
    с описанием каждой транзакции в формате строки"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция принимает начальное и конечное значение диапазона
    возвращает генератор со сгенерированными в заданных рамках номерами банковских карт в формате строки"""
    for i in range(start, stop + 1):
        generated_num = f"{'0' * (16 - len(str(i))) + str(i)}"
        result_card_num = f"{generated_num[:4]} {generated_num[4: 8]} {generated_num[8: 12]} {generated_num[12:]}"
        yield result_card_num
