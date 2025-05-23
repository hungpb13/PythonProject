# Lambda function = a small anonymous function for one time use
# Take any number of arguments, but have only one expression
# Keep the namespace clean
# Useful with higher order functions: sort(), map(), filter(), reduce()
# lambda parameters: expression

double = lambda x: x * 2
add = lambda x, y: x + y
max_val = lambda x, y: x if x > y else y
min_val = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: True if x % 2 == 0 else False
is_odd = lambda x: True if x % 2 != 0 else False
is_adult = lambda age: True if age >= 18 else False

print(double(2))
print(add(1, 2))
print(max_val(2, 3))
print(min_val(2, 3))
print(full_name("Bro", "Code"))
print(is_even(3))
print(is_odd(3))
print(is_adult(30))
