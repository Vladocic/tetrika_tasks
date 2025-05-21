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
        if actual_types != expected_types:
            raise TypeError("Аргументы не соответствуют аннотированным типам параметров функции")        
        return func(*args)
    return wrapped
    

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

abg = [str, int, float]

fg = [int, str, float]


for i in enumerate(zip(abg,fg)),s:
    print(i)
print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
