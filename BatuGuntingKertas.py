import random

game_rule = ["Rock", "Paper", "Scissors"]  # Urutan yang benar

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())

# Cek input valid
if user_choice < 0 or user_choice > 2:
    print("Invalid Number")
else:
    print(f"You chose: {game_rule[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_rule[computer_choice]}")

    if computer_choice == user_choice:
        print("You Draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You Win")
    else:
        print("You Lose")
