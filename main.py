# List comprehension = a concise way to create a list
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]

doubles = [i * 2 for i in range(1, 11)]

# for i in range(1, 11):
#     doubles.append(i * 2)

print(doubles)

numbers = [i for i in range(1, 101)]
print(numbers)

even_numbers = [i for i in numbers if i % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(even_numbers)
print(odd_numbers)
