# Exercise: Calc The Hypotenuse of a Right Angled Triangle

import math

a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))

c = math.sqrt(pow(a, 2) * pow(b, 2))

print(f"Side C = {c}")
