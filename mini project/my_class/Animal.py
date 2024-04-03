class Cat:
    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def info(self):
        print(f'hello,I am a cat.my name is {self.name}')

    @staticmethod
    def make_sound():
        print('Mew...')


class Cow:
    def __init__(self, name='', color=''):
        self.name = name
        self.color = color

    def info(self):
        print(f'hello,I am a cow.my name is {self.name}')

    @staticmethod
    def make_sound():
        print('Mooo...')


def func(obj):
    obj.info()
    obj.make_sound()


cat = Cat('jaki', 'black')
cow = Cow('gavi', 'brown')

func(cat)
func(cow)
