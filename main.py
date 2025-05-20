# Exercise: Basic Calculator

operator = input("Enter a operator (+ - * /): ")

first_number = float(input("Enter the 1st number: "))
second_number = float(input("Enter the 2nd number: "))

result = 0

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number
else:
    print(f"{operator} is not a valid operator")

print(f"Result = {round(result, 2)}")
