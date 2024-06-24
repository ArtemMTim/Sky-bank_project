from typing import Dict
import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

base_url = "https://api.apilayer.com/axchangerates_data/convert"

def transaction_convertation(trasaction: Dict) -> float:
    amount = trasaction["operationAmount"]["amount"]
    currency = trasaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    else:
        headers = {
            "apikey": api_key
        }
        params = {
            "to": "RUB", "from": currency, "amount": amount
        }
        response = requests.get(base_url, headers=headers, params=params)
        result = response.json()
trans = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

print(transaction_convertation(trans))
