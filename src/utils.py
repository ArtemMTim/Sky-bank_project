import json
import logging
import os
from json import JSONDecodeError
from typing import Dict, List, Union

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
    filename=f"{log_path}utils.log",
    filemode="w",
)

# Определяем логгеры для каждой из представленных функций
transact_logger = logging.getLogger("app.transact")


def transactions_list_func(file_name: str) -> List[Dict[str, Union[str, int, dict, float]]]:
    """Принимает название JSON файла с информацией о транзакциях.
    Файл располагается в директории data корневого каталого проекта.
    Возвращает список словарей транзакций."""
    transact_logger.info("Программа начинает работу.")
    if os.name == "nt":
        project_path = "\\".join((os.path.dirname(os.path.abspath(__file__))).split("\\")[:-1])
        data_path = f"{project_path}\\data\\"
    else:
        project_path = "/".join((os.path.dirname(os.path.abspath(__file__))).split("/")[:-1])
        data_path = f"{project_path}/data/"
    try:
        transact_logger.info(f"Программа пытается открыть файл '{file_name}'.")
        with open(f"{data_path}{file_name}", "r", encoding="UTF-8") as file:
            transact_logger.info(f"Программа начинает обработку файла '{file_name}'.")
            try:
                data = json.load(file)
                transact_logger.info(f"Программа успешно обработала файл '{file_name}'.")
                if isinstance(data, list):
                    transact_logger.info("Программа завершает свою работу.")
                    return data
                else:
                    transact_logger.info("Программа завершает свою работу.")
                    return []
            except JSONDecodeError:
                print("Невозможно декодировать файл. Проверьте содержимое файла!")
                transact_logger.error("Невозможно декодировать файл!'.")
                return []
    except FileNotFoundError:
        print("Указанный файл не найден!")
        transact_logger.error("Файл не найден!")
        return []
