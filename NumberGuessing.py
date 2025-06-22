import random

print(r"""
  ____                     _                ____                      
 / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
| |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                   |___/                              
 """)

def choice_level():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == 'easy':
            return 10
        elif level == 'hard':
            return 5
        else:
            print("Choose only hard or easy")

def playgame():
    correct_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")

    lives = choice_level()
    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess > correct_number:
            lives -=1
            print("Too High")
            if lives != 0:
                print("Guess Again")
            else:
                print("You Lose")

        elif correct_number > guess:
            lives -=1
            print("Too Low")
            if lives != 0:
                print("Guess Again")
            else:
                print("You Lose")
        else:
            print(f"You got it! The answer was {correct_number}")
            break

while True:
    playgame()
    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
