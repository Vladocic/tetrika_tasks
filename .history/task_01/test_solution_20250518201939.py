import pytest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_sum_correct_types():
    assert sum_two(2, 3) == 5

@strict
def sum_words(a: str, b: str) -> str:
    return a + b
def test_sum__wcorrect_types():
    assert sum_two(2, 3) == 5