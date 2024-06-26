from src.decorators import log


# Тестирование декоратора log при выводе результатов в консоль
@log()
def func_1(a, b):
    return a / b


def test_func_1(capsys):
    result = func_1(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "func_1 ok\n"
    assert result == 2


def test_func_1_error_str(capsys):
    func_1("a", "b")
    captured = capsys.readouterr()
    assert (
        captured.out.strip() == "func_1: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('a', 'b'), {}."
    )


def test_func_1_error_zero(capsys):
    func_1(4, 0)
    captured = capsys.readouterr()
    assert captured.out.strip() == "func_1: division by zero. Inputs: (4, 0), {}."


# Тестирование декоратора log при записи результатов в заданный файл
@log("log_test.txt")
def func_2(a, b):
    return a / b


def test_func_2():
    result = func_2(4, 2)
    with open("log_test.txt", "r", encoding="UTF-8") as file_in:
        result_message = file_in.read()
    assert result_message == "func_2 ok"
    assert result == 2


def test_func_2_error_str():
    func_2("a", "b")
    with open("log_test.txt", "r", encoding="UTF-8") as file_in:
        result_message = file_in.read()
    assert result_message == "func_2: unsupported operand type(s) for /: 'str' and 'str'. Inputs: ('a', 'b'), {}."


def test_func_2_error_zero(capsys):
    func_2(4, 0)
    with open("log_test.txt", "r", encoding="UTF-8") as file_in:
        result_message = file_in.read()
    assert result_message == "func_2: division by zero. Inputs: (4, 0), {}."
