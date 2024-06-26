import pytest

from src.utils import transactions_list_func


# Тестирование считывания файла, вывода сообщений об ошибках в консоль и возврата результатов
@pytest.mark.parametrize(
    "file_name, expected_result, expected_message",
    [
        ("test_normal.json", [{"name": "test_normal.json"}], ""),
        ("test_not_list.json", [], ""),
        ("test_empty.json", [], "Невозможно декодировать файл. Проверьте содержимое файла!"),
        ("test_none.json", [], "Указанный файл не найден!"),
    ],
)
def test_transactions_list_func(file_name, expected_message, expected_result, capsys):
    result = transactions_list_func(file_name)
    captured = capsys.readouterr()
    assert result == expected_result
    assert captured.out.strip() == expected_message
