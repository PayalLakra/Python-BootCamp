'''
Topics to be covered:
- Hangman Game
'''

import random

words = ['payal','nikki','shaksham','vinni','tannu']

choose = random.choice(words)
print(choose)

word_length = len(choose)
placeholder = ""
for i in range(word_length):
    placeholder += "_ "
print(placeholder)

game_over = False
correct_letter = []
display = ""
while not game_over:
    guess = input("Enter a letter:").lower()

    for letter in choose:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_ "
    print(display)

    if "_" not in guess:
        game_over = True
        print("You Win")