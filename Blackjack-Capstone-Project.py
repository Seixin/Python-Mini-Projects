import random
from replit import clear

print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      '------'     
""")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == 0:
        return "You won with a Blackjack!"
    elif computer_score == 0:
        return "You lost. Computer has a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    elif user_score < computer_score:
        return "You lose."
    else:
        return "Draw."

def playgame():
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    should_continue = True
    while should_continue:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_continue = False
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                user_card.append(deal_card())
            elif choice == 'n':
                should_continue = False
            else:
                print("Invalid input. Please type 'y' or 'n'.")

    if calculate_score(user_card) <= 21:
        while calculate_score(computer_card) != 0 and calculate_score(computer_card) < 17:
            computer_card.append(deal_card())


    print(f"\nYour final hand: {user_card}, final score: {calculate_score(user_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {calculate_score(computer_card)}")
    print(compare(calculate_score(user_card), calculate_score(computer_card)))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower() == "y":
    clear()
    playgame()
