import os
from typing import Dict

import requests
from dotenv import load_dotenv


def transaction_convertation(trasaction: Dict) -> float:
    """Принимает информацию о транзакции в формате словаря. Возвращает сумму транзакции в рублях,
    если транзакция осуществлялась в другой валюте, производит конвертацию в рубли через API."""
    amount = trasaction["amount"]
    currency = trasaction["currency_code"]
    if currency == "RUB":
        return float(amount)
    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            result = response.json()
            return float(result["result"])
        except requests.exceptions.ConnectionError:
            print("Произошла ошибка 'Connection Error'! Проверьте, пожалуйста, Ваше соединение!")
        except requests.exceptions.HTTPError:
            print("Произошла ошибка 'HTTP Error'! Проверьте, пожалуйста, адрес!")
        except requests.exceptions.Timeout:
            print("Превышено время ожидания ответа! Проверьте, пожалуйста, Ваше соединение!")
        except requests.exceptions.TooManyRedirects:
            print("Превышено максимальное количество перенаправлений! Проверьте, пожалуйста, адрес!")
