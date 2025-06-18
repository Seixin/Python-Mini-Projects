import random

stages = [
    r"""
    +---+
    |   |
        |
        |
        |
        |
=========
""", r"""
    +---+
    |   |
    O   |
        |
        |
        |
=========
""", r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
""", r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
""", r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
""", r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
""", r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
"""]


word_list = ["aardvark", "baboon", "camel"]
lives = 6
#Pilih kata acak
kata = random.choice(word_list)
print(kata)
placeholder = (len(kata)*"-")
print(placeholder)

tebakan_benar = []

#suruh nebak
game_over = False
while not game_over:
    pilihan= input("Guess a letter: ").lower()
    display=""
    for letter in kata:
        if letter == pilihan:
            display += letter
            tebakan_benar.append(letter)
        elif letter in tebakan_benar:
            display +=letter
        else:
            display+= "_"
    print(display)
    if pilihan not in kata:
        lives-=1
        if lives == 0:
            game_over=True
            print("You Lose")
       

    if "_" not in display:
        game_over = True
        print("You Win")

    print(stages[6-lives])