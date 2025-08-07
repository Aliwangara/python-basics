
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0

is_running = True

print("Python Number Guessing Game")

print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter Your Guess: ")

    if guess.isdigit():
        pass
    else:
        print("invalid guess")
        print(f"select a number between {lowest_num} and {highest_num}")






