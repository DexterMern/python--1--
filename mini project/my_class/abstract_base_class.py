# abstract Base class
from abc import ABC, abstractmethod


# abstract base class
class vehicle(ABC):
    @abstractmethod
    def move(self):
        """"this method should be implemented!"""

    @abstractmethod
    def repair(self):
        """"this method should be implemented!"""

    def class_name(self):
        print(self.__class__)


class LandVehicle(vehicle):
    @abstractmethod
    def brake(self):
        """"this method should be implemented!"""


class AirVehicle(vehicle):
    @abstractmethod
    def eject(self):
        """"this method should be implemented!"""


# concrete class
class Car(vehicle):
    def move(self):
        super(Car, self).move()

    def repair(self):
        print('Under repair...')


class Airplane(vehicle):
    def move(self):
        print('Flying.....')

    def repair(self):
        print('Under repair...')

    def eject(self):
        print('Ejecting...')


car = Car()
a = Airplane()
