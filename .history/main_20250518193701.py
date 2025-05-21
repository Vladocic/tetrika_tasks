import inspect

def strict(func):
    def wrapped(*args):
        income = [type(i).__name__ for i in args]
        sig = inspect.signature(func).parameters
        base_date = []
        for i in sig.values():
            pass

        func(*args)
        return 
    return wrapped
    
def one(*args):
    return [type(i).__name__ for i in args]

print(one(1,2,'g'))

# @strict
def sum_two(a: str, b: int) -> int:
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
