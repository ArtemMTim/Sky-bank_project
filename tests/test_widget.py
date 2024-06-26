import pytest

from src.widget import date_formatting, masking_with_info

# Тестирование функции masking_with_info


@pytest.fixture
def card_masks():
    return "MasterCard 1234567890123456"


def test_masking_with_info(card_masks):
    assert masking_with_info(card_masks) == "MasterCard 1234 56** **** 3456"


@pytest.fixture
def bank_masks():
    return "Счет 12345678901234567893"


def test_masking_with_info_1(bank_masks):
    assert masking_with_info(bank_masks) == "Счет **7893"


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
        ("Visa Gold A 1234567890123456", "Visa Gold A 1234 56** **** 3456"),
        ("Счет 12345678901234567893", "Счет **7893"),
        ("Счёт 12345678901234567893", "Счёт **7893"),
        ("VisaGold1234567890123456", "Ошибка в введённых данных!"),
        ("Счет12345678901234567893", "Ошибка в введённых данных!"),
        ("Visa Gold A 123456789012345v", "Введён не корректный номер кредитной карты! Проверьте!"),
        ("Счет 1234567890123456789", "Введён не корректный номер банковского счёта! Проверьте!"),
    ],
)
def test_masking_with_info_2(numbers, expected):
    assert masking_with_info(numbers) == expected


# Тестирование функции date_formatting


@pytest.fixture
def dates():
    return "2018-07-11T02:26:18.671407"


def test_date_formatting_1(dates):
    assert date_formatting(dates) == "11.07.2018"


@pytest.mark.parametrize(
    "dates, expected", [("2018-07-11T02:26:18.671407", "11.07.2018"), ("2019-12-11T02:26:18.671407", "11.12.2019")]
)
def test_date_formatting_2(dates, expected):
    assert date_formatting(dates) == expected


# Проверяем на возникновение ошибки ValueError при введении некорректных данных


def test_date_formatting_wrong_date_format():
    with pytest.raises(ValueError):
        date_formatting("20118-07-11T02:26:18.671407")


def test_date_formatting_wrong_arg():
    with pytest.raises(ValueError):
        date_formatting("a")
