# Object = a "bundle" of related attributes (variables) and methods (functions)
# Class = a blueprint used to design the structure and layout of an Object
# A Class --> create many Objects

from car import Car

# Create Object
car_one = Car("Mustang", 2025, "red", True)
car_two = Car("Corvette", 1999, "blue", False)
car_three = Car("Charger", 2016, "yellow", True)

# <__main__.Car object at 0x000002753AF5D2B0> --> memory address
print(car_one)

# Dot . operator --> to access attributes and methods

# Attributes
print(car_one.model)
print(car_one.year)
print(car_one.color)
print(car_one.for_sale)

# Methods
car_one.drive()
car_two.drive()
car_three.drive()

car_one.stop()
car_two.stop()
car_three.stop()
