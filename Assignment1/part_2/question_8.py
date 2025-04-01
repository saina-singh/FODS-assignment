'''
Program to create a number guessing game.
'''

import random

# Generating a random number between 1 and 100
answer = random.randint(1, 100)
attempts = 5

print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the correct number.")

# Allow the user to guess up to 5 times
for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == answer:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    remaining_attempts = attempts - (i + 1)
    print(f"Remaining attempts: {remaining_attempts}")

# If user doesn't guess correctly in 5 attempts
if guess != answer:
    print(f"Game Over! The correct number was {answer}.")
