#Easy guess the number game using python
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            guess = int(input("Guess the number between 1 and 100. Your guess is: "))
        except ValueError:
            print("Wrong value, write a number between 1 and 100.")
            continue

        if guess < 1 or guess > 100:
            print("Invalid, guess a number between 1 and 100.")
            continue

        guesses += 1

        if guess == number_to_guess:
            print(f"Correct! You guessed the number in {guesses} tries.")
            break
        elif guess < number_to_guess:
            print("Incorrect number. Try again with a higher number!")
        else:
            print("Incorrect number. Try again with a lower number!")

if __name__ == "__main__":
    guess_number()
