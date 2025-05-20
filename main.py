# Conditional expression = an oneline shortcut for the if-else statement (ternary operator)
# Print or assign one of the two values based on a condition
# Formula: value_if_true if condition else value_if_false

number = -5
a = 3
b = 4
age = 18
temperature = 30
user_role = "admin"

print("Positive" if number > 0 else "Negative")

even_or_odd = "Even" if number % 2 == 0 else "Odd"
print(even_or_odd)

print(f"Max = {a if a > b else b}")
print(f"Min = {a if a < b else b}")

print(f"Status = {"Adult" if age >= 18 else "Child"}")

print(f"Weather = {"Hot" if temperature > 25 else "Cold"}")

print(f"Access level = {"Full" if user_role == "admin" else "Limited"}")