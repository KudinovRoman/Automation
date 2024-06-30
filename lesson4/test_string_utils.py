import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("string, result", [
    # positive
    ("skypro", "Skypro"),
    ("sky pro", "Sky pro"),
        ("кирилл", "Кирилл"),
     # negative
    ("123", "123"),
    ("",""),
    ("   ", "   "),
    ("123qwe", "123qwe")
    ])
def test_capitilize(string, result):
    string_utils = StringUtils()
    res = string_utils.capitilize(string)
    assert res == result

@pytest.mark.parametrize("string, result", [
    # positive
    ("   skypro   ", "skypro   "),
    ("   skypro", "skypro"),
    ("   123", "123"),
    ("  Всем привет", "Всем привет"),
    # negative
    ("", "")
    ])
def test_trim(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result

    # negative
@pytest.mark.parametrize("string, result", [
    ("   SKY   ", "SKY")])
@pytest.mark.xfail(reason="возвращается со всех сторон без пробелов")
def test_trim_spaces(string, result):
    string_utils = StringUtils()
    res = string_utils.trim(string)
    assert res == result
   
    # negative
@pytest.mark.xfail()
def test_trim_number():
    assert string_utils.trim(123) == "123"



@pytest.mark.parametrize("length, delimeter, result", [
    # positive
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("a/b/c", "/", ["a", "b", "c"]),
    # negative
    ("", ",", []),
    ("", None, []),
    ("1,2,3", None, ["1", "2", "3"]),
    ])
def test_to_list(length, delimeter, result):
    string_utils = StringUtils() 
    if delimeter is None:
        res = string_utils.to_list(length)
    else:
        res = string_utils.to_list(length, delimeter)
    assert res == result

    
@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Skypro" , "S", True),
    ("Skypro" , "p", True),
    ("Игорь" , "И", True),
    ("", "",True),
    ("123" , "1", True),
    # negative
    ("123" , "И", False),
    # ("Игорь", "", False), отображает ошибку, хотя проверка должна проходить (баг-репорт 2 в файле defects)
    ("Skypro" , "s", False)
    ])
def test_contains(string, symbol, result):
     string_utils = StringUtils() 
     res = string_utils.contains(string, symbol)
     assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Skypro" , "S", "kypro"),
    ("казнить, нельзя, помиловать" , ",", "казнить нельзя помиловать"),
    ("123" , "2", "13"),
    ("Skypro" , "p", "Skyro"),
    # negative
    ("Skypro" , "s", "Skypro"),
    ("Skypro" , "H", "Skypro"),
    ("123", "Y", "123")
    ])
def test_delete_symbol(string, symbol, result):
     string_utils = StringUtils() 
     res = string_utils.delete_symbol(string, symbol)
     assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Skypro" , "S", True),
    ("Игорь", "И", True),
    ("123", "1", True),
    # negative
    ("Skypro" , "s", False),
    ("1234" , "s", False),
    ("Skypro" , "1", False),
    ("Skypro" , "H", False),
    ("Skypro" , "p", False)
    ])
def test_starts_with(string, symbol, result):
     string_utils = StringUtils() 
     res = string_utils.starts_with(string, symbol)
     assert res == result

@pytest.mark.parametrize("string, symbol, result", [
    # positive
    ("Skypro" , "o", True),
    ("123" , "3", True),
    ("Где Вадим?" , "?", True),
    ("каво", "о", True),
    # negative
    ("Skypro" , "O", False),
    ("123" , "1", False),
    ("Где Вадим?" , "м", False),
    ("Gendalf" , "ф", False),
    ("Skypro" , "O", False)
    ])
def test_end_with(string, symbol, result):
     string_utils = StringUtils() 
     res = string_utils.end_with(string, symbol)
     assert res == result


@pytest.mark.parametrize("string, result", [
    # positive
    ("" , True),
    (" ", True),
    # negative
    ("Skypro", False),
    ("    Skypro", False),
    ("123", False),
    ("Ходор", False),
    ])
def test_is_empty(string, result):
     string_utils = StringUtils() 
     res = string_utils.is_empty(string)
     assert res == result


@pytest.mark.parametrize("length, delimeter, result", [
    # positive
    (["a", "b", "c", "d"], ",", "a,b,c,d"),
    (["a", "b", "c"], "/",  "a/b/c"),
    (["К", "и", "б", 'о', 'р', 'г'], "",  "Киборг"),
    # negative
    ([], ",", ""),
    ([], None, "")
    ])
def test_list_to_string(length, delimeter, result):
    if delimeter is None:
            res = string_utils.list_to_string(length) 
    else:
        res = string_utils.list_to_string(length, delimeter)
    assert res == result