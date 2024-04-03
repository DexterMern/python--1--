class Vehicle:
    def __init__(self, speed: str, color: str, weight: str):
        self.speed = speed
        self.color = color
        self.weight = weight


class Airplane(Vehicle):
    def __init__(self, the_length: str, **kwargs):
        super().__init__(**kwargs)
        self.the_length = the_length


class Bicycle(Vehicle):
    def __init__(self, gear: str, **kwargs):
        super().__init__(**kwargs)
        self.gear = gear


class Car(Vehicle):
    def __init__(self, cylinder=None, **kwargs):
        super().__init__(**kwargs)
        self.cylinder = cylinder


class Lamborghini(Car):
    def __init__(self, number_of_doors=None, **kwargs):
        super().__init__(**kwargs)
        self.number_of_doors = number_of_doors


class Benz(Car):
    def __init__(self, modellings=None, **kwargs):
        super().__init__(**kwargs)
        self.modellings = modellings


a = Benz(speed='192.6', color='red', weight='568kg', cylinder=7, modellings='s7')
print(a.modellings, a.color, a.speed, a.weight, a.cylinder)
