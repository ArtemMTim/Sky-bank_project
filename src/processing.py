from datetime import datetime
from typing import List


def state_func(dict_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция принимает список словарей и занчение ключа 'state' по-умолчанию равного 'EXECUTED'.
    Вщзвращает список словарей с ключом 'state' равным заданному значению"""
    return [dictionary for dictionary in dict_list if dictionary.get("state") == state]


def date_sort_func(dict_list: List[dict], direction: bool = True) -> List[dict]:
    """Функция принимает список словарей и необязательное значение направления сортировки - возрастание либо убывание.
    По-умолчанию необязательный параметр равен 'False' - убывание.
    Возвращает отсортированный  согласно направлению сортировки список словарей."""
    return sorted(dict_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=direction)
