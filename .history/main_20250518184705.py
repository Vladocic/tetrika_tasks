def strict(func):
    ...


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

fun.__annotatiob
print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
