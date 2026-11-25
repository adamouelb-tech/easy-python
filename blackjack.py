#Easy blackjack game
import random


CARD_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def draw_card():
    return random.choice(CARD_VALUES)


def calculate_hand(cards):
    total = sum(cards)
    aces = cards.count(11)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def play_blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    print(f"\nYour cards: {player_hand} (total: {calculate_hand(player_hand)})")
    print(f"Dealer shows: {dealer_hand[0]}")

    if calculate_hand(player_hand) == 21:
        print("Blackjack! You win!")
        return

    while calculate_hand(player_hand) < 21:
        action = input("Do you want to hit or stand? ").strip().lower()

        if action in ("hit", "h"):
            player_hand.append(draw_card())
            total = calculate_hand(player_hand)
            print(f"\nYour cards: {player_hand} (total: {total})")

            if total > 21:
                print("You passed 21. You lose!")
                return
        elif action in ("stand", "s"):
            break
        else:
            print("Please enter 'hit' or 'stand'.")

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    print(f"\nDealer cards: {dealer_hand} (total: {dealer_total})")

    while dealer_total < 17:
        dealer_hand.append(draw_card())
        dealer_total = calculate_hand(dealer_hand)
        print(f"Dealer draws: {dealer_hand} (total: {dealer_total})")

    if dealer_total > 21:
        print("Dealer passed 21. You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a tie.")


def wants_to_play_again():
    while True:
        answer = input("\nPlay again? (Y/N): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter Y or N.")


if __name__ == "__main__":
    print("Welcome to Blackjack!")

    while True:
        play_blackjack()
        if not wants_to_play_again():
            print("Thanks for playing!")
            break