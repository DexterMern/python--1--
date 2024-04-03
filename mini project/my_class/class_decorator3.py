from functools import update_wrapper


class MyClassDecorator:
    def __init__(self, cls):
        update_wrapper(self, cls)
        self.cls = cls

    def __call__(self):
        print(40 * '*')
        print(self.cls.__name__)
        obj = self.cls()
        print(40 * '*')
        return obj


@MyClassDecorator
class Test:
    def __init__(self):
        self.a = 5


obj = Test()
print(obj.a)
