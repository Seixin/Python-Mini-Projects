import HigherLowerData as HLD
import random

print(r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/        
""")

def random_person():
    return random.choice(HLD.data)

def compare(A, B, guess):
    if guess == 'A' and A['follower_count'] >= B['follower_count']:
        return True
    elif guess == 'B' and B['follower_count'] >= A['follower_count']:
        return True
    else:
        return False

def playgame():
    score = 0
    gameover = False
    person1 = random_person()
    person2 = random_person()
    while person1 ==person2:
        person2 = random_person
    while not gameover:
        

        print(f"Compare A: {person1["name"]}, {person1["description"]}, {person1["country"]}.")

        print(r"""
        _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)
        """)
        print(f"Against B: {person2["name"]}, {person2["description"]}, {person2["country"]}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        check = compare(person1, person2, guess)

        if check == True:
            score +=1
            print(f"You're right! Current score: {score}.")
            person1 = person2
            person2 = random_person()
            while person1 == person2:
                person2 = random_person()
        else:
            print("You are lose")
            gameover = True

playgame()