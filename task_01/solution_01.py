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
        for num, (actual,expect) in enumerate(zip(actual_types,expected_types), start=1):
            if actual != expect:
                raise TypeError(f"Аргумент в позиции №{num} имеет тип {actual.__name__}, ожидался {expect.__name__}")
        return func(*args)
    return wrapped
    
