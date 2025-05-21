import inspect

def strict(func):
    pass
    


# @strict
def sum_two(a: int, b: int) -> int:
    return a + b

    
bn = sum_two.__annotations__
print(bn.[])
print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
