# class MyClass:
#     __slots__ = ('a', 'c', 'b')
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# obj = MyClass(1, 2)
# obj.c = 5
# print(obj.a)
# print(obj.b)
# print(obj.c)
class ParenClass:
    __slots__ = ('a', 'b')

    def __init__(self, a, b):
        self.a = a
        self.b = b


class MyClass(ParenClass):
    def __init__(self, a, b):
        super().__init__(a, b)


obj = MyClass(1, 2)
print(obj.__dict__)
