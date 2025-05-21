import inspect

def strict(func):
    ...


# @strict
def sum_two(a: int, b: int) -> int:
    return a + b

print(sum_two.__annotations__)
print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
