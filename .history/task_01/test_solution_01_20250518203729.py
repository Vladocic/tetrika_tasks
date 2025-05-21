import pytest
from solution_01 import strict

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
    with pytest.raises(TypeError):
        sum_two(1.5, 2)







