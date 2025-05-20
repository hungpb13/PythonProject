# if = do some code IF condition is True
# else = do something else

name = input("Enter your name: ")

if name != "":
    print(f"Hello, {name}!")
else:
    print("You did not enter your name!")

age = int(input("Enter your age: "))

if age > 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")

response = input("Would you like food? (Y/N): ").upper()

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")