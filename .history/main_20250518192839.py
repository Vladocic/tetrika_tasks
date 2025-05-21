import inspect

def strict(func):
    def wrapped(*args):
        sig = inspect.signature(sum_two).parameters
        func(*args)
        return 
    return wrapped
    


# @strict
def sum_two(a: int, b: int) -> int:
    print(type(a))
    # sig = inspect.signature(sum_two).parameters
    # for i in sig.values():
    #     print(i.name)
    #     print(i.annotation.__name__)
    return a + b

    
# sig = inspect.signature(sum_two).parameters
# for i,b in sig.items():
#     print(i)
#     print(b.name)
#     print(b.annotation.__name__)

print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
