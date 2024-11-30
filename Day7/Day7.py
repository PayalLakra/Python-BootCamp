'''
Topics to be covered:
- Hangman Game
'''

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ['payal', 'nikki', 'shaksham', 'vinni', 'tannu']
lives = 6
choose = random.choice(words)
print(choose)  # for testing purposes, you may want to remove this line

# Initialize display with underscores for each letter in the chosen word
display = ["_"] * len(choose)
print(" ".join(display))

game_over = False
correct_letter = []

while not game_over:
    print(f"\n********** {lives} lives left **********")
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in correct_letter:
        print(f"You have already guessed the letter '{guess}'")
        continue

    correct_letter.append(guess)

    # Update display if the guess is correct
    if guess in choose:
        for index, letter in enumerate(choose):
            if letter == guess:
                display[index] = letter
    else:
        # Reduce lives for incorrect guesses
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        print(HANGMANPICS[6 - lives])  # Print the hangman picture for the current lives

        if lives == 0:
            game_over = True
            print("********** You Lose **********")

    print(" ".join(display))

    # Check if the player has guessed all letters
    if "_" not in display:
        game_over = True
        print("********** YOU WIN **********")