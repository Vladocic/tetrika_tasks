import inspect

def strict(func):
    def wrapped(*args):
        func()
        return 
    return wrapped
    


# @strict
def sum_two(a: int, b: int) -> int:
    sig = inspect.signature(sum_two).parameters
    for i,c in sig.items():
        print(i)
        print(c.name)
        print(c.annotation.__name__)
    return a + b

    
# sig = inspect.signature(sum_two).parameters
# for i,b in sig.items():
#     print(i)
#     print(b.name)
#     print(b.annotation.__name__)

print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
