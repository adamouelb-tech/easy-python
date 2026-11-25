import random

choices = ["Rock", "Paper", "Scissors"]


def get_choice():
    while True:
        print("Choose an option:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if 1 <= choice <= 3:
            return choice

        print("Please enter a valid choice (1-3).\n")


def wants_to_play_again():
    while True:
        play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()

        if play_again in ("y", "yes"):
            return True
        if play_again in ("n", "no"):
            return False

        print("Please enter Y or N.")


def determine_winner(choice, computer_choice):
    if choice == computer_choice:
        return "tie"
    if (
        (choice == 1 and computer_choice == 3)
        or (choice == 2 and computer_choice == 1)
        or (choice == 3 and computer_choice == 2)
    ):
        return "user"
    return "computer"


def main():
    print("Welcome to Rock-Paper-Scissors!\n")
    print("Winning Rules:")
    print("Rock vs Paper -> Paper wins")
    print("Rock vs Scissors -> Rock wins")
    print("Paper vs Scissors -> Scissors wins\n")

    while True:
        choice = get_choice()
        user_choice = choices[choice - 1]
        computer_choice = choices[random.randint(1, 3) - 1]

        print("\nUser choice is:", user_choice)
        print("Now it's Computer's Turn...")
        print("Computer choice is:", computer_choice)
        print(user_choice, "vs", computer_choice)

        result = determine_winner(choice, choices.index(computer_choice) + 1)
        if result == "tie":
            print("<== It's a Tie! ==>")
        elif result == "user":
            print("<== User Wins! ==>")
        else:
            print("<== Computer Wins! ==>")

        if not wants_to_play_again():
            break
        print()

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()