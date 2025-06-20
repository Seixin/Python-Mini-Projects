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
      '------'     """)

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
        return "You Won with a blackjack"
    elif computer_score == 0:
        return "You Lost. Computer has a blackjack"
    elif user_score > 21:
        return "You Lost"
    elif computer_score > 21:
        return "You Won"
    elif computer_score > user_score:
        return "You Lost"
    elif user_score > computer_score:
        return "You Won"
    else:
        return "Draw"

def playgame():
    user_card = []
    computer_card = []
    for _ in range(2):
        computer_card.append(deal_card())
        user_card.append(deal_card())
        
    computer_score = calculate_score(computer_card)
    user_score = calculate_score(user_card)
    should_continue = True
    while should_continue:
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score > 21:
            should_continue = False
            break

        while True:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                user_card.append(deal_card())
                user_score = calculate_score(user_card)
                if user_score > 21:
                    should_continue = False
                break
            elif choice == 'n':
                should_continue = False
                break
            else:
                print("invalid input, please type correctly")

    while calculate_score(computer_card) < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    user_score = calculate_score(user_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    play = input("Do you want to play a game of blackjack. Type y or n: ").lower()
    while play == "y":
        clear()
        playgame()

playgame()
