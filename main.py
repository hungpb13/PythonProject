# input() = a function that prompts user to enter data
# Return the entered data as a string

name = input("What is your name?: ")

age = int(input("How old are you?: "))
age += 1

print(f"Hello {name}!")
print(f"You are {age} years old")