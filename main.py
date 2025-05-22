# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local --> Enclosed --> Global --> Built-in

# Built-in
from math import pi

# Global
global_var = "This is from global"


# Local
def function_a():
    a = 1  # Local
    print(a)
    print(global_var)
    print(pi)


def function_b():
    b = 2  # Local
    print(b)
    # print(a) --> cannot access variable 'a'
    print(global_var)
    pi = 3.14 # Local
    print(pi)


function_a()
function_b()


# Enclosed
def outer_function():
    x = "This is from outer"  # Enclosed when used in inner_function()

    def inner_function():
        x = "This is from inner"  # Local
        print(x)

    print(x)
    inner_function()


outer_function()
