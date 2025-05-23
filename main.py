# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = many
# Morphe = form
# Inheritance -> override methods in child classes

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(radius=5), Square(width=5), Rectangle(width=5, length=10), Pizza("pepperoni", 10)]

for shape in shapes:
    print(f"Area: {shape.area()}cm²")
