import pytest
from solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_words(a: str, b: int) -> int:
    return a + b