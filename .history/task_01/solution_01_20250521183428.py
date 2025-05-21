import inspect

def strict(func):
    def wrapped(*args):
        allowed_types = {int, float, str, bool}
        sig = inspect.signature(func).parameters
        expected_types = []
        for param in sig.values():
            if param.annotation not in allowed_types:
                raise TypeError(f"Функция использует тип {param.annotation}, который не входит в список разрешённых")
            expected_types.append(param.annotation)

        actual_types = [type(i) for i in args]
        print(actual_types)
        for num, (actual,expect) in enumerate(zip(actual_types,expected_types), start=1):
            print(num)
            if actual != expect:
                raise TypeError(f"Аргумент в позиции №{num} имеет тип {actual.__name__}, ожидался {expect.__name__}")
        return func(*args)
    return wrapped
    

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

sum_two(1,2)