'''
Topics to be Covered:
- Local and Global Scope
- Number Guessing Game
'''

# Global constants are variables which you define & you're never planning on changing it ever again.
# Scope: -> Local Scope =  accessible only inside the function
#        -> Global Scope =  accessible throughout the program

name = "Outside Function"      # Global Scope

def scope():
    print("Inside Function")   # Local Scope

print(name)   # Global Scope
scope()       # Local Scope

# Prime Number Checker

num = int(input("Enter any number:"))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_prime(num))

# Number Guessing Game

from random import randint
from art import number_guessing

EASY_GUESS = 10
HARD_LEVEL = 5

def check_guess(guess, num):
    """Check the user's guess against the number and provide feedback."""
    global turns
    if guess > num:
        print("Too High.")
        turns -= 1
    elif guess < num:
        print("Too Low.")
        turns -= 1
    else:
        print(f"You got it! The answer was {num}.")

def difficulty():
    """Set the difficulty level."""
    global turns
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        turns = EASY_GUESS
    elif level == 'hard':
        turns = HARD_LEVEL
    else:
        print("Invalid choice. Defaulting to 'easy'.")
        turns = EASY_GUESS

def game():
    """Main game function."""
    print(number_guessing)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = randint(1, 100)
    # print(f"(The number is {num})")  # For testing purpose.

    difficulty()

    guess = 0
    while guess != num:
        print(f"You have {turns} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        check_guess(guess, num)

        if turns == 0:
            print("You've run out of turns. You lose!")
            return
        elif guess != num:
            print("Guess again.")

# Start the game
game()