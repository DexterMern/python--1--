class Animal:
    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def info(self):
        print(f'hello,im a animal.my name is {self.name}, i am {self.color} .')

    def make_sound(self):
        print('i can make sound!')


class Cat(Animal):
    def __init__(self, name='', color=''):
        super().__init__(name, color)

    def make_sound(self):
        print('Mew...')


class Cow(Animal):
    def __init__(self, name='', color=''):
        super().__init__(name, color)

    def info(self):
        print(f'hello,I am a cow.my name is {self.name} , i am {self.color} .')

    def make_sound(self):
        print('Mooo...')


animal = Animal()
cat = Cat('jaki', 'black')
cow = Cow('gavi', 'brown')

animal.info()
cat.info()
cow.info()