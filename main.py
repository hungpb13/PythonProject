# @property = decorator used to define a method as a property
# Benefit: Add additional logic when read, write, or delete attributes
# getter, setter, deleter methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(10, 20)

# Access to a protected member _attribute of a class
# print(f"Width = {rectangle._width}")
# print(f"Height = {rectangle._height}")

rectangle.width = 5
rectangle.height = 10

print(f"Width = {rectangle.width}")
print(f"Height = {rectangle.height}")

del rectangle.width
del rectangle.height
