import inspect

def strict(func):
    def wrapped(*args):
        allowed_types = {int, float, str, bool}
        sig = inspect.signature(func).parameters
        base_date = []
        for param in sig.values():
            if param.annotation not in allowed_types:
                raise TypeError("Не подходящий тип данных")
            base_date.append(param.annotation)

        income = [type(i) for i in args]
        if income != base_date:
            raise TypeError("Не соответсвие типо")
        return func(*args)
    return wrapped
    

@strict
def sum_two(a: int, b: int) -> int:
    return a + b



print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
