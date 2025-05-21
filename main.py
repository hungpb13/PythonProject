# Default argument = a default value for certain parameter
# Default is used when that argument is omitted
# Make function more flexible, reduce number of arguments
# Argument: Positional --> DEFAULT --> Keyword --> Arbitrary

import time


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))


def count(end, start=1):
    for i in range(start, end + 1):
        print(i)
        time.sleep(1)
    print("Time's up!")


count(20, 15)
