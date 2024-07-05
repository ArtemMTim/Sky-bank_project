import os
from unittest.mock import patch

import pytest

from src.external_api import transaction_convertation

# Тестирование случая рублёвой транзакции
test_transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "amount": "31957.58",
    "currency_name": "руб.",
    "currency_code": "RUB",
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


@pytest.mark.parametrize("transaction, expected", [(test_transaction, 31957.58)])
def test_transaction_convertation_1(transaction, expected):
    assert transaction_convertation(transaction) == expected


# Тестирование случая транзакции отличной от рублёвой
test_transaction_non_rub = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "amount": "10",
    "currency_name": "USD",
    "currency_code": "USD",
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

request_to_return = {
    "date": "2018-02-22",
    "historical": "",
    "info": {"rate": 148.972231, "timestamp": 1519328414},
    "query": {"amount": 10, "from": "USD", "to": "RUB"},
    "result": 1000,
    "success": True,
}


@patch("requests.get")
@patch.dict(os.environ, {"API_KEY": "my_api_key"})
def test_transaction_convertation_2(mock_request):
    mock_request.return_value.json.return_value = request_to_return
    assert transaction_convertation(test_transaction_non_rub) == 1000.0
    mock_request.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10",
        headers={"apikey": "my_api_key"},
        timeout=5,
        allow_redirects=False,
    )
