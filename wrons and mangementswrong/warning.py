import warnings


def func(x: int, y: int):
    if not isinstance(x, int) and not isinstance(y, int):
        warnings.warn('x and y cant be strings!!!', UserWarning)
        print(x + y)

func('r', 'b')
print('ok')
