import json
import logging
import os
from json import JSONDecodeError
from typing import Dict, List, Union

from config import DATA_DIR, UTILS_LOGS

# Проводим настройку логгеров для логирования в файл (уровень DEBUG) и в консоль (уровень ERROR)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(UTILS_LOGS, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_list_func(file_name: str) -> List[Dict[str, Union[str, int, dict, float]]]:
    """Принимает название JSON файла с информацией о транзакциях.
    Файл располагается в директории data корневого каталого проекта.
    Возвращает список словарей транзакций."""
    logger.info("Программа начинает работу.")
    file_with_dir = os.path.join(DATA_DIR, file_name)

    try:
        logger.info(f"Программа пытается открыть файл '{file_name}'.")
        with open(file_with_dir, "r", encoding="UTF-8") as file:
            logger.info(f"Программа начинает обработку файла '{file_name}'.")
            try:
                data = json.load(file)
                logger.info(f"Программа успешно обработала файл '{file_name}'.")
                if isinstance(data, list):
                    logger.info("Программа завершает свою работу.")
                    return data
                else:
                    logger.info("Программа завершает свою работу.")
                    return []
            except JSONDecodeError:
                print("Невозможно декодировать файл. Проверьте содержимое файла!")
                logger.error("Невозможно декодировать файл!'.")
                return []
    except FileNotFoundError:
        print("Указанный файл не найден!")
        logger.error("Файл не найден!")
        return []


transactions_list_func("operations.json")
