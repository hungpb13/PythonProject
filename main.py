# Exercise: Find the Factorial of a Number
# n! = n x (n-1) x (n-2) x ... x 1

# Iterative
def factorial_i(num):
    result = 1
    if num > 0:
        for i in range(1, num + 1):
            result *= i
        return result
    return result


print(factorial_i(2))


# Recursive
def factorial(num):
    # Base case
    if num == 1 or num <= 0:
        return 1

    # Recursive call
    return num * factorial(num - 1)


print(factorial_i(5))
