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
        sum



@strict
def sum_words(a: str, b: str) -> str:
    return a + b

def test_sum_correct_types():
    assert sum_two(2, 3) == 5
    assert sum_two(2, 3) == 5

@strict
def sum_words(a: str, b: str) -> str:
    return a + b
def test_sum__words_correct_types():
    assert sum_two(2, 3) == 5



@strict
def broken_func(a: list, b: int) -> int:
    return b