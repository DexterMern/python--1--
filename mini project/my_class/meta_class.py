# هر چیزی در پایتون یک شی هست.
class HumanMeta(type):
    pass


class Human(metaclass=HumanMeta):
    pass


h = Human()
print(type(h))
print(type(Human))
