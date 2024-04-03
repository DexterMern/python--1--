class MyClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print(40 * '*')
        self.func()
        print(40 * '*')


@MyClassDecorator
def my_func():

    print('reza')


my_func()
