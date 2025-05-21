# Random Numbers

import random

low = 1
high = 100

int_num = random.randint(low, high)
print(int_num)

# Random float number from 0 --> 1
float_num = random.random()
print(float_num)

# Random float number from 1 --> 5
float_num = random.uniform(1, 5)
print(float_num)

options = ("rock", "paper", "scissors")
option = random.choice(options)
print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
