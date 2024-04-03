class Shape:
    def __init__(self, **kwargs):
        self.area = None
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.permiter = 0

    def calculate_area(self):
        pass

    def calculate_permit(self):
        pass

    def show(self):
        info = ''
        for key, value in self.__dict__.items():
            if value > 0:
                info += f'{key}: {value:.2f}\n'
        print(info)

    def __str__(self):
        return self.__class__.__name__


# length , width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.perimeter = None
        self.width = None
        self.length = None

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_permit(self):
        self.perimeter = (self.length + self.width) * 2


# length
class Squre(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.length = None

    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_permit(self):
        self.permeter = 4 * self.length


# base , height , base , side1 , side2
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.height = None
        self.side2 = None
        self.side1 = None
        self.base = None

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_permit(self):
        self.permeter = self.base + self.side1 + self.side2


# diameter1,diameter2,length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.length = None
        self.dimeter2 = None
        self.diameter1 = None

    def calculate_area(self):
        self.area = (self.diameter1 * self.dimeter2) / 2

    def calculate_permit(self):
        self.permeter = self.length * 4


# length,height,width
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.width = None
        self.height = None
        self.length = None

    def calculate_area(self):
        self.area = self.length * self.height

    def calculate_permit(self):
        self.permeter = 2 * (self.length + self.width)


# height,top,base,side1,side2
class Tapzium(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.side2 = None
        self.side1 = None
        self.base = None
        self.top = None
        self.height = None

    def calculate_area(self):
        self.area = 1 / 2 * self.height * (self.top + self.base)

    def calculate_permit(self):
        self.permeter = self.top + self.base + self.side1 + self.side2


# redus
class circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.permeter = None
        self.redus = None

    def calculate_area(self):
        self.area = self.redus ** 2 * 3.14

    def calculate_permit(self):
        self.permeter = 2 * self.redus * 3.14


# .........................................
s = Rectangle(length=2, width=4)
print(s)
s.calculate_permit()
s.calculate_area()
s.show()
print('*' * 40)
# # .........................................
# r = Squre(length=5)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
# # .........................................
# r = Triangle(base=10, height=6, side1=10, side2=10)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
# # .........................................
# r = Rhombus(diameter1=9, diameter2=4, length=5)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
# # .........................................
# r = Parallelogram(length=5, height=7, width=4)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
# # .........................................
# r = Tapzium(height=8, top=10, base=15, side1=20, side24=20)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
# # .........................................
# r = circle(redus=15)
# print(r)
# r.calculate_permit()
# r.calculate_area()
# r.show()
# print('*' * 40)
