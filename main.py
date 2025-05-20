# For loop = execute a block of code a fixed number of times
# Iterate over a range, string, sequence, etc.

for i in range(1, 11):
    print(i, end=" ")
print("\nReversed range")
for i in reversed(range(1, 11)):
    print(i)
print("HAPPY NEW YEAR!")

credit_card = "1234-5678-9012-3456"

for number in credit_card:
    if number == "-":
        continue
    print(number, end=" ")
