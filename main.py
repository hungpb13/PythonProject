# reduce(function, collection) = reduce elements in a collection to a single value
# For loop is better in most cases
# Reduce is better for a functional approach + readability

from functools import reduce

grades = [63, 45, 23, 85, 99, 74, 56, 88]

add = lambda x, y: x + y

total_grade = reduce(add, grades)

average_grade = total_grade / len(grades)

print(f"Average grade = {average_grade:.2f}")
