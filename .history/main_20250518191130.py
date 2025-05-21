import inspect

def strict(func):
    def wrapped():
        func()
        return 
    return wrapped
    


# @strict
def sum_two(a: int, b: int) -> int:
    return a + b

    
sig = inspect.signature(sum_two).parameters
print(sig.parameters.items())

# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
