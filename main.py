# While loop = execute some code WHILE condition remains True

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Please, enter your name: ")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative!")
    age = int(input("Please, enter a valid age: "))

food = input("Enter a food you like (press Q to quit): ")

while not food.upper() == "Q":
    print(f"You like {food}")
    food = input("Enter another food you like (press Q to quit): ")

number = int(input("Enter a number between 1 and 10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Please, enter a number between 1 and 10: "))

print("Hello " + name)
print(f"Next year, you will be {age + 1}")
print(f"Your number is {number}")