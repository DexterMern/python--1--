def func(x: int, y: int):
    assert isinstance(x, int) and isinstance(y, int)
    print(x + y)


func('7', '5')
print('ok')
