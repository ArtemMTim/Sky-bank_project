import pytest
from src.csv_excel_reader import csv_excel_reader
from unittest.mock import patch


# Тестирование с mock patch
# Тестирование считывания csv файла
@patch("pandas.read_csv")
def test_csv_reader(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    result = csv_excel_reader("test_file.csv")
    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


# Тестирование считывания xlsx файла
@patch("pandas.read_excel")
def test_excel_reader(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]
    result = csv_excel_reader("test_file.xlsx")
    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
        }
    ]


# Тестирование выдачи ошибок
# Тестируем выдачу ошибки о неподдерживаемом формате файла
def test_csv_excel_reader_with_wrong_format_file():
    with pytest.raises(ValueError) as exc_info:
        csv_excel_reader("test.txt")
        assert str(exc_info.value) == "Неподдерживаемый формат файла."


# Тестируем выдачу ошибки о непредвиденном событии при считывании файла
def test_csv_excel_reader_with_no_file():
    with pytest.raises(Exception) as exc_info:
        csv_excel_reader("test_none.csv")
        assert str(exc_info.value) == "При считывании файла произошла ошибка."
