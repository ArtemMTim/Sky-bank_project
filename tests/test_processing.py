import pytest

from src.processing import date_sort_func, state_func

# Тестирование функции state_func


@pytest.fixture
def state_dicts():
    return [{"name": 1, "state": "EXECUTED"}, {"name": 2, "state": "NOT"}, {"name": 3, "state": "EXECUTED"}]


def test_state_func_1(state_dicts):
    assert state_func(state_dicts) == [{"name": 1, "state": "EXECUTED"}, {"name": 3, "state": "EXECUTED"}]


# Проверка со значением "state" по-умолчанию
@pytest.mark.parametrize(
    "list_of_dicts, expected",
    [
        (
            [
                {"name": 1, "state": "EXECUTED"},
                {"name": 2, "state": "NOT"},
                {"name": 3, "state": "EXECUTED"},
                {"name": 4, "state": "EXECUTED"},
                {"name": 5, "state": "NOT"},
                {"name": 6, "state": "YES"},
            ],
            [{"name": 1, "state": "EXECUTED"}, {"name": 3, "state": "EXECUTED"}, {"name": 4, "state": "EXECUTED"}],
        ),
        (
            [
                {"name": 1, "state": "NOT"},
                {"name": 2, "state": "NOT"},
                {"name": 3, "state": "AAA"},
                {"name": 4, "state": "YES"},
                {"name": 5, "state": "NOT"},
                {"name": 6, "state": "YES"},
            ],
            [],
        ),
        ([], []),
    ],
)
def test_state_func_2(list_of_dicts, expected):
    assert state_func(list_of_dicts) == expected


# Проверка спроизвольно заданным значением "state"
@pytest.mark.parametrize(
    "list_of_dicts, state, expected",
    [
        (
            [
                {"name": 1, "state": "EXECUTED"},
                {"name": 2, "state": "NOT"},
                {"name": 3, "state": "EXECUTED"},
                {"name": 4, "state": "EXECUTED"},
                {"name": 5, "state": "NOT"},
                {"name": 6, "state": "YES"},
            ],
            "NOT",
            [{"name": 2, "state": "NOT"}, {"name": 5, "state": "NOT"}],
        ),
        (
            [
                {"name": 1, "state": "NOT"},
                {"name": 2, "state": "NOT"},
                {"name": 3, "state": "AAA"},
                {"name": 4, "state": "YES"},
                {"name": 5, "state": "NOT"},
                {"name": 6, "state": "YES"},
            ],
            "A",
            [],
        ),
    ],
)
def test_state_func_3(list_of_dicts, state, expected):
    assert state_func(list_of_dicts, state) == expected


# Проверка функции state_func на возникновение ошибок
def test_state_func_wrong_arg_str():
    with pytest.raises(AttributeError):
        state_func("A")


def test_state_func_wrong_arg_int():
    with pytest.raises(TypeError):
        state_func(1)


# Тестирование функции date_sort_func
# Тестирование с направлением сортировки по-умолчанию
@pytest.fixture
def sort_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_date_sort_func_1(sort_dicts):
    assert date_sort_func(sort_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Тесстирование с заданным направлением сортировки
@pytest.mark.parametrize(
    "list_of_dicts, direction, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_date_sort_func_2(list_of_dicts, direction, expected):
    assert date_sort_func(list_of_dicts, direction) == expected


# Проверка функции date_sort_func на возникновение ошибок
def test_date_sort_func_wrong_arg_str():
    with pytest.raises(TypeError):
        date_sort_func("A")


def test_date_sort_func_wrong_arg_int():
    with pytest.raises(TypeError):
        date_sort_func(1)


def test_date_sort_func_wrong_dateformat_in_data():
    with pytest.raises(ValueError):
        date_sort_func(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20118-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
