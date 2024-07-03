import pytest
from src.csv_excel_reader import csv_excel_reader
from unittest.mock import patch, mock_open



expected = [
    {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": 3598919.0,
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": 29740.0,
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]


# Тестируем работу модуля с файлами csv, xlsx
@pytest.mark.parametrize("file_name, expected", [("test_1.csv", expected), ("test_2.xlsx", expected)])
def test_csv_excel_reader(file_name, expected):
    assert csv_excel_reader(file_name) == expected


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


#Тестирование с mock patch
data = "[{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol'}]"
expected_result = [
        {'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol'}
    ]

# При включении теста появляется assertion error - пустой список не равен ожидаемому
@patch("builtins.open", new_callable=mock_open, read_data=data)
def test_csv_excel_reader_2(mock_file):
    result = csv_excel_reader("test_file.csv")
    assert result == expected_result

# При включении теста появляется assertion error - None не равен ожидаемому
def test_csv_excel_reader_3():
    with patch('builtins.open') as mock_open:
        mock_open = [{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol'}]
        assert csv_excel_reader("test_file.csv") == expected_result