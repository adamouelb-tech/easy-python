import blackjack
import calculator
import guessing_numbers
import rock_paper_scissors
import wordle


GAMES = {
    "1": ("Blackjack", blackjack.play_blackjack),
    "2": ("Wordle", wordle.guess_the_word),
    "3": ("Calculator", calculator.calculator),
    "4": ("Rock, Paper, Scissors", rock_paper_scissors.main),
    "5": ("Number Guessing", guessing_numbers.guess_number),
}


def show_menu():
    print("\n=== Game Console ===")
    for number, (name, _) in GAMES.items():
        print(f"{number}. {name}")
    print("0. Exit")


def main():
    print("Welcome to Easy Python!")

    while True:
        show_menu()
        choice = input("What would you like to play today? ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        if choice not in GAMES:
            print("Invalid option. Choose a number from the menu.")
            continue

        print(f"\nStarting {GAMES[choice][0]}...")
        GAMES[choice][1]()


if __name__ == "__main__":
    main()
