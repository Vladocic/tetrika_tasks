import inspect

def strict(func):
    pass
    


# @strict
def sum_two(a: int, b: int) -> int:
    return a + b

    
bn = sum_two.__annotations__
for i,b in bn.items():
    print(b+"t")
print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
