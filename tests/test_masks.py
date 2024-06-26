import pytest

from src.masks import bank_account_masking, credit_card_masking


# Тестирование функции credit_card_masking
@pytest.fixture
def card_masks():
    return "1234567890123456"


def test_credit_card_masking_1(card_masks):
    assert credit_card_masking(card_masks) == "1234 56** **** 3456"


@pytest.mark.parametrize(
    "numbers, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("123", "Введён не корректный номер кредитной карты! Проверьте!"),
        ("123 456789012345", "Введён не корректный номер кредитной карты! Проверьте!"),
        ("abcdefghijklmnop", "Введён не корректный номер кредитной карты! Проверьте!"),
    ],
)
def test_credit_card_masking_2(numbers, expected):
    assert credit_card_masking(numbers) == expected


# Тестирование функции bank_account_masking
@pytest.fixture
def bank_masks():
    return "12345678901234567890"


def test_bank_account_masking_1(bank_masks):
    assert bank_account_masking(bank_masks) == "**7890"


@pytest.mark.parametrize(
    "numbers, expected",
    [
        (12345678901234567890, "**7890"),
        ("12345678901234567890", "**7890"),
        ("123", "Введён не корректный номер банковского счёта! Проверьте!"),
        ("123 4567890123456789", "Введён не корректный номер банковского счёта! Проверьте!"),
        ("abcdefghijklmnop1234", "Введён не корректный номер банковского счёта! Проверьте!"),
    ],
)
def test_bank_account_masking_2(numbers, expected):
    assert bank_account_masking(numbers) == expected
