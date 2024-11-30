'''
Topics to be Covered:
- Game: Higher or Lower
'''

import random
from import_things import data

def format_data(account):
    """Format the data into printable format"""
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]
    return (f"{acc_name}, a {acc_desc}, from {acc_country}")

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and follower counts and return if they got it right"""
    if a_followers > b_followers:
        return user_guess.lower() == "a"
    else:
        return user_guess.lower() == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)

    print('''   __   ___       __             
    / / / (_)___ _/ /_  ___  _____
    / /_/ / / __ '/ __ \/ _ \/ ___/
    / __  / / /_/ / / / /  __/ /    
    /_/ ///_/\__, /_/ /_/\___/_/     
    / /  /____/_      _____  _____
    / /   / __ \ | /| / / _ \/ ___/
    / /___/ /_/ / |/ |/ /  __/ /    
    /_____/\____/|__/|__/\___/_/         
    ''')

    print(f"Compare A: {format_data(account_a)}.")

    print('''   
    _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)
    ''')

    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current Score: {score}")
    else:
        print(f"Sorry, that's wrong.Your Final score: {score}")
        game_should_continue = False