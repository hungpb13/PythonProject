# Return = statement used to end a function and send a result back to the caller

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a, b = 1, 2

print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))


def create_name(first_name, last_name):
    first_name = first_name.capitalize();
    last_name = last_name.capitalize();
    return first_name + " " + last_name


full_name = create_name("bro", "code")
print(full_name)
