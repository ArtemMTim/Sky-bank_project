import os

# Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

# Директория для логов
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

# Директория для файлов с данными
DATA_DIR = os.path.join(ROOT_DIR, "data")


# Создание каталога для логов, если он не существует
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

UTILS_LOGS = os.path.join(LOGS_DIR, "utils.log")
MASKS_LOGS = os.path.join(LOGS_DIR, "masks.log")
CSV_EXCEL_LOGS = os.path.join(LOGS_DIR, "csv_excel.log")
