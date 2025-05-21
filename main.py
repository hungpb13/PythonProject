# Exercise: Number Guessing Game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guess = 0
num_of_guesses = 0
is_running = True

print("Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        num_of_guesses += 1

        if guess < lowest_num or guess > highest_num:
            print(f"{guess} is out of range!")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer is {answer}")
            print(f"Number of guesses: {num_of_guesses}")
            is_running = False
    else:
        print("Invalid guess!")
        print(f"Please select a number between {lowest_num} and {highest_num}")
