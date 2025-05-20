# Type Casting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Bro code"
age = 25
gpa = 3.2
is_student = True

# Float --> Int
gpa = int(gpa)
print(gpa)

# Int --> Float
age = float(age)
print(age)

# Int --> Str
age = str(age)
age += "1"
print(age)

# Str --> Bool
name = bool(name)
print(name)
print(bool(""))

# Int --> Bool
print(bool(1))
print(bool(0))