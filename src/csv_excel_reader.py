import logging
import os
from typing import Dict, List

import pandas as pd

from config import CSV_EXCEL_LOGS, DATA_DIR

# Проводим настройку логгеров для логирования в файл (уровень DEBUG)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(CSV_EXCEL_LOGS, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def csv_excel_reader(file_name: str) -> List[Dict]:
    """Принимает название (путь) csv либо xlsx файла с информацией о транзакциях.
    Возвращает список словарей транзакций."""
    logger.info("Программа начинает работу.")
    # Определяем вид файла и применяем необходимый метод обработки.
    if file_name.endswith("csv"):
        try:
            logger.info("Программа считывает csv файл.")
            file_with_dir = os.path.join(DATA_DIR, file_name)
            transactions_df = pd.read_csv(file_with_dir, sep=";", decimal=",", encoding="utf-8")
            logger.info("Программа формирует список транзакций по считанным из файла данным.")
            result = transactions_df.to_dict(orient="records")
            logger.info("Программа успешно завершила свою работу.")
            return result
        except Exception as err:
            logger.error(f"При считывании файла произошла ошибка {err}.")
    elif file_name.endswith("xlsx"):
        try:
            logger.info("Программа считывает xlsx файл.")
            file_with_dir = os.path.join(DATA_DIR, file_name)
            transactions_df = pd.read_excel(file_with_dir)
            logger.info("Программа формирует список транзакций по считанным из файла данным.")
            result = transactions_df.to_dict(orient="records")
            logger.info("Программа успешно завершила свою работу.")
            return result
        except Exception as err:
            logger.error(f"При считывании файла произошла ошибка {err}.")
    else:
        logger.error("Произошла ошибка ValueError: Неподдерживаемый формат файла.")
        raise ValueError("Неподдерживаемый формат файла.")
