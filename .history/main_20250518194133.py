import inspect

def strict(func):
    def wrapped(*args):
        allowed_types = {int, float, str, bool}

        income = [type(i).__name__ for i in args]
        sig = inspect.signature(func).parameters
        base_date = [i.annotation.__name__ for i in sig.values()]
        raise TypeError("Не соответсвие типом")
        return func(*args) if income == base_date else TypeError 
    return wrapped
    


# @strict
def sum_two(a: str, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
