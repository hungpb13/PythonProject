# Exercise: Calc Area of a Circle

import math

pi = math.pi

radius = float(input("Enter the radius of a circle: "))

area = pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)} cm²")