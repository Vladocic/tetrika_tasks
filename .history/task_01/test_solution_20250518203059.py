import pytest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_sum_correct_types():
    assert sum_two(2, 3) == 5

def test_sum_str_and_int():
    with pytest.raises(TypeError):
        sum_two("1",2)

def test_sum_list_and_int():
    with pytest.raises(TypeError):
        sum_two([1,2],3)

def test_sum_two_bool_and_int():
    with pytest.raises(TypeError):
        sum_two(True, 1)

def test_sum_two_float_and_int():
    assert sum_two(1.5, 2) == 3.5

def test_sum_two_int_and_float():
    assert sum_two(2, 3.0) == 5.0

@strict
def sum_words(a: str, b: str) -> str:
    return a + b

def test_sum_words_correct_types():
    assert sum_words("1", "3") == "13"




