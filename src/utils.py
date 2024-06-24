import json
import os
from json import JSONDecodeError
from typing import Dict, List, Union


def transactions_list_func(file_name: str) -> List[Dict[str, Union[str, int, dict, float]]]:
    """Принимает название JSON файла с информацией о транзакциях.
    Файл располагается в директории data/ корневого каталого проекта.
    Возвращает список словарей транзакций."""
    project_path = "/".join((os.path.dirname(os.path.abspath(__file__))).split("/")[:-1])
    data_path = f"{project_path}/data/"
    try:
        with open(f"{data_path}{file_name}", "r", encoding="UTF-8") as file:
            try:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []
            except JSONDecodeError:
                print("Невозможно декодировать файл. Проверьте содержимое файла!")
                return []
    except FileNotFoundError:
        print("Указанный файл не найден!")
        return []
