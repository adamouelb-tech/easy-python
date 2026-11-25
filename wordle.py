import random

def guess_the_word():
    word_lst = [
    "Apple",
    "Beach",
    "Black",
    "Bread",
    "Break",
    "Brown",
    "Chair",
    "Child",
    "Clean",
    "Cloud",
    "Color",
    "Dance",
    "Drink",
    "Earth",
    "Entry",
    "Every",
    "Field",
    "First",
    "Floor",
    "Fresh",
    "Front",
    "Fruit",
    "Glass",
    "Green",
    "Group",
    "Guide",
    "Heart",
    "Horse",
    "House",
    "Juice",
    "Knife",
    "Laugh",
    "Lemon",
    "Light",
    "Model",
    "Money",
    "Music",
    "Night",
    "Paper",
    "Party",
    "Plant",
    "Power",
    "Quiet",
    "River",
    "Smile",
    "Space",
    "Sport",
    "Stone",
    "Sugar",
    "Water"
]

    guess_word = random.choice(word_lst).lower()
    lifes = 5
    while True:
        user_guess = input("Guess the word from the list. Your guess is: ").lower()
        if len(user_guess) != len(guess_word):
            print(f"{user_guess} hasn't got the right lenght" )
        elif user_guess == guess_word:
            print(f"{user_guess} is the correct word")
            break
        else:
            lifes -= 1
            if user_guess[0] == guess_word[0]:
                print(f"{user_guess[0]}")
            elif user_guess[0] != guess_word[0]:
                print("_")
                
            if user_guess[1] == guess_word[1]:
                print(f"{user_guess[1]}")
            elif user_guess[1] != guess_word[1]:
                print("_")
                
            if user_guess[2] == guess_word[2]:
                print(f"{user_guess[2]}")
            elif user_guess[2] != guess_word[2]:
                print("_")
                
            if user_guess[3] == guess_word[3]:
                print(f"{user_guess[3]}")
            elif user_guess[3] != guess_word[3]:
                print("_")
                
            if user_guess[4] == guess_word[4]:
                print(f"{user_guess[4]}")
            elif user_guess[4] != guess_word[4]:
                print("_")
            
            if lifes == 0:
                print(f"You ran out of lifes. The word was {guess_word}")
                break

if __name__ == "__main__":
    name = input("What is your name: ")
    print(f"Good luck {name}!")
    guess_the_word()