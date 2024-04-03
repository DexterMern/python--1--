class SuperClass1:
    def __init__(self, p1):
        self.p1 = p1


class SuperClass2:
    def __init__(self, p2):
        self.p2 = p2


class SubClass(SuperClass2, SuperClass1):
    def __init__(self, p1, p2, p3):
        SuperClass1.__init__(self, p1)
        SuperClass2.__init__(self, p2)
        self.p3 = p3


obj = SubClass(1, 2, 3)
print('p1: ', obj.p1)
print('p2: ', obj.p2)
print('p3: ', obj.p3)
