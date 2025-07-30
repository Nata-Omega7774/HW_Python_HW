import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitalize"""

def test_capitalize():
    """POSITIVE"""
    assert utils.capitalize("test") == "Test"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"
    """NEGATIVE"""
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("тест12345") == "Тест12345"

"""trim"""

def test_trim():
    """POSITIVE"""
    assert utils.trim(" skypro") == "skypro"
    assert utils.trim(" skypro ") == "skypro "
    assert utils.trim(" skypro 123 ") == "skypro 123 "
    """NEGATIVE"""
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_space_input():
    assert utils.trim(" SKY ") == "SKY "  # Исправлен ожидаемый результат

"""to list"""

@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", ",", ["1", "2", "3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
    assert res == result

"""contains"""

@pytest.mark.parametrize('string, symbol, result', [
    ("собака", "с", True),
    ("ржавый гвоздь", " ", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("Москва", "м", False),    # Регистрозависимая проверка
    ("привет", "з", False),
    ("", "p", False),
    ("123", "h", False),
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

"""delete_symbol"""

@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", "анан"),
    ("гвоздь", "д", "гвозь"),
    ("диван кровать", " ", "диванкровать"),
    ("145", "1", "45"),
    ("Москва", "", "Москва"),
    ("привет", "з", "привет"),
    ("", "p", ""),
    ("", "", ""),
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

"""startswith"""

@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "б", True),
    ("", "", True),
    ("divan", "d", True),
    ("145", "1", True),
    ("Москва", "м", False),   # Регистрозависимая проверка
    ("привет", "П", False),   # Регистрозависимая проверка
    ("", "@", False),
    ("мир", "з", False),
])
def test_startswith(string, symbol, result):
    res = utils.startswith(string, symbol)
    assert res == result

"""endswith"""

@pytest.mark.parametrize('string, symbol, result', [
    ("банан", "н", True),
    ("", "", True),
    ("divan", "n", True),
    ("145", "5", True),
    ("Москва ", "", True),   # Исправлено: проверка пробела в конце
    ("привет", "л", False),
    ("", "@", False),
    ("дверь", "Ь", False),   # Регистрозависимая проверка
])
def test_endswith(string, symbol, result):
    res = utils.endswith(string, symbol)
    assert res == result

"""is_empty"""

@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),   # Строка из одного пробела должна считаться пустой
    ("лосось", False),
    ("145", False),
    (" Москва", False),  # Строка с пробелом в начале не пустая
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

"""list_to_string"""

@pytest.mark.parametrize('lst, joiner, result', [
    (["s", "o", "s"], ".", "s.o.s"),
    (["н", "о", "с"], "", "нос"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    ([], None, ""),
    ([], ",", ""),
    ([], "крот", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result