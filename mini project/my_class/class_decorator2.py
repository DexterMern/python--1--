from functools import update_wrapper


class MyClassDecorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self):
        print(40 * '*')
        self.func()
        print(40 * '*')


@MyClassDecorator
def my_func():
    """"My Func"""
    print('reza')
    print(1 + 2)


print(my_func.__dict__)

print(40 * '/')


@MyClassDecorator
class Test:
    pass


Test()

