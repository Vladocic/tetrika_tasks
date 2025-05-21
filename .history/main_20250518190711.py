import inspect

def strict(func):
    def wrapped():
        
        pass
    return wrapped
    


# @strict
def sum_two(a: int, b: int) -> int:
    return a + b

    
sig = inspect.signature(sum_two)
print(sig.parameters)

# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
