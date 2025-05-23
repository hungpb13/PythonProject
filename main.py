# Abstract class = a class that cannot be instantiated
# Meant to be subclassed (inherit by anoar class)
# Benefits:
# 1. Prevents instantiation of a class itself
# 2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod


# Abstract Class
class Vehicle(ABC):

    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    def describe(self):
        return f"{self.year} {self.color} {self.brand} {self.model}"

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Error: Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'
# car = Vehicle()

# Implemented by a subclass
class Car(Vehicle):
    def go(self):
        print(f"You drive a {self.describe()}")

    def stop(self):
        print(f"You stop a {self.describe()}")


class Motorcycle(Vehicle):

    def go(self):
        print(f"You ride a {self.describe()}")

    def stop(self):
        print(f"You stop a {self.describe()}")


car = Car("BMW", "i7", "blue", 2019)
car.go()
car.stop()
print(f"This is a {car.describe()}")

motorcycle = Motorcycle("Honda", "Air Blade", "black", 2024)
motorcycle.go()
motorcycle.stop()
print(f"This is a {motorcycle.describe()}")
