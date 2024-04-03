class NameField:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if 0 < len(value) < 15:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f'invalid name {value!r}')

    def __delete__(self, instance):
        print(f'Deleting(({self.name}))...')
        del instance.__dict__[self.name]


class Parent:
    child_name = NameField()
    father_name = NameField()
    mother_name = NameField()

    def __init__(self, child_name, father_name, mother_name):
        self.child_name = child_name
        self.father_name = father_name
        self.mother_name = mother_name


p = Parent('reza', 'mahdi', 'maya')
print(p.child_name)
print(p.mother_name)
print(p.father_name)
del p.mother_name
