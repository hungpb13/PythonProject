# *args = pass multiple positional arguments ()
# **kwargs = pass multiple keyword arguments {key:value}
# * = unpacking operator
# Argument: Positional --> Default --> Keyword --> ARBITRARY

def add(*args):
    print(type(args))
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4))


def print_address(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake St.", city="Detroit", state="MI", zip="54321")
