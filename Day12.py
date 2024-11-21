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

import random
from art import number_guessing

num = random.choice(1,100)
print(num)

def num_guess():
    return

print(number_guessing)
print("Welcome to Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty level. Type'easy' or 'hard'").lower()

if level == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    num_guess()
elif level == 'hard':
    print("You have 5 attempts remaining to guess the number.")
    num_guess()