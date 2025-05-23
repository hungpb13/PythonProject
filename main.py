# super() = function used in a child to call methods from a parent class (super class)
# Extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        return f"{self.color} and {'filled' if self.is_filled else 'not filled'}"


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        return f"It is a {super().describe()} circle with an area of {3.14 * pow(self.radius, 2)}cm^2"


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        return f"It is a {super().describe()} square with an area of {pow(self.width, 2)}cm^2"


class Rectangle(Shape):
    def __init__(self, color, is_filled, width, length):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length

    def describe(self):
        return f"It is a {super().describe()} rectangle with an area of {self.width * self.length}cm^2"


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=10)
rectangle = Rectangle(color="yellow", is_filled=True, width=10, length=20)

print(circle.describe())
print(square.describe())
print(rectangle.describe())
