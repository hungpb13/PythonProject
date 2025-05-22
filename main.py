# Module = a file containing code that you want to include in your programs
# Use 'import' to include a module (built-in or your own)
# Useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("math"))

# import math
# import math as m
from math import pi

# print(math.pi)
# print(m.pi)
print(pi)

import example

print(example.pi)
print(example.square(3))
print(example.cube(3))
print(example.circumference(3))
print(example.area(3))
