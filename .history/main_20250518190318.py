import inspect

def strict(func):
    pass
    


# @strict
def sum_two(a: int, b: int) -> in:
    return a + b

    
aba = inspect.signature(sum_two)
print(aba)

# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
