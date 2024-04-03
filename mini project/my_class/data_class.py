from dataclasses import dataclass, InitVar


@dataclass
class Person:
    name: str
    family: str
    age: int
    gender: InitVar[str]

    def __post_init__(self, gender):
        if gender == 'man':
            self.name += '*'


p = Person(name='reza', family='idolater', age=27, gender='man')
print(p.name)


# .....................
# @dataclass
# class Person1:
#     name1: str
#     family1: str
#     age1: int
#
#
# @dataclass
# class Person2(Person1):
#     name2: str
#     family2: str
#     age2: int
#
#
# p = Person2('a', 'b', 25, 'c')
# print(p)
