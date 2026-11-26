# Easy guess the number but each try tells you how close you are with: Freezing, cold, sunny, hot, melting!

import random


def cold_or_hot():
    number_to_guess = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100. Your guess: "))
        except ValueError:
            print("Enter a valid number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Enter a valid guess between 1 and 100.")
            continue

        guesses += 1

        if guess == number_to_guess:
            print(f"Correct! You guessed the number in {guesses} tries.")
            break

        difference = abs(number_to_guess - guess)

        if guess < number_to_guess:
            direction = "Try a higher number!"
        else:
            direction = "Try a lower number!"

        if difference >= 40:
            print("You are outside while it is freezing")
        elif difference >= 25:
            print("You are in a cold room")
        elif difference >= 12:
            print("You are enjoying a sunny day")
        elif difference >= 5:
            print("You are drinking hot chocolate")
        else:
            print("You are melting in the sun")

        print(direction)


if __name__ == "__main__":
    cold_or_hot()