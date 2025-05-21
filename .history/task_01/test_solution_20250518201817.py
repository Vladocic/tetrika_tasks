import pytest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b