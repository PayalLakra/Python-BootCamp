'''
Topics to be covered:
- Randomization
- Modules
- Lists
- Nested lists
- Coin Tossing randomization
- Index Error
- Project:Rock Scissor Paper Game
'''

#Randomization = generates random numbers
import random
random_int = random.randint(3,7)    #both 3&7 are included
print(random_int)
random_float = random.random()    #to create random between 0 and 1 in floats. a is included while b is not
print(random_float)
random_float_any = random.random() * 10    #to create random between 0 and whatever multiplied in floats. a is included while b is not
print(random_float_any)
random_float_inc = random.uniform(19,29)    #to create random between 0 and 1 in floats. a & b both included 
print(random_float_inc)

#Modules- A file containing python definitions and statements
#To create a module - first create a .py file with name like my_module then in the Day4.py file write-
# import my_module
# print(my_module.number)   #this number is in the my_module.py file.

# Coin Tossing
random_headtail = random.randint(0,1)
if random_headtail == 0:
    print("Head")
else:
    print("Tail")

#LIST - [], used to store data ,separated by commmas, immutable
fruits = ["APPLE","MANGO","PEAR","PAPAYA","BANANA"]    #example of a list
print(fruits[1])   #retreive using index
print(fruits[-1])   #retreive using back indexing
fruits[3] = "GRAPES"     #alter the value of 3rd index
print(fruits)
fruits.append("PAPAYA")
print(fruits)    #add new item in list at end always

#randomization from a list
#OPTION 1
import random
friends = ["A","B","C","D","E","F"]
print(f"{random.choice(friends)} is going to pay the bill.")
#OPTION 2
friends = ["A","B","C","D","E","F"]
rann=random.randint(0,5)
print(f"{friends[rann]} is going to pay the bill.")

#index Error:
friends = ["A","B","C","D","E","F"]
#print(friends[10])   #throws index error
#So to prevent from that situation we can first check the length of the list
print(len(friends))

#NESTED LISTS
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][1])    # The first index takes list number
print(dirty_dozen[1][3])    # second one takes the index pf that particular list
print(dirty_dozen[0][2])
print(dirty_dozen[1][1])

#ROCK PAPER SCISSORS
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [Rock,Paper,Scissors]
user_choice = int(input("What do you want to choose? Type 0 for rock , 1 for paper or 2 for scissors.\n"))
print("You Choose\n")
print(game_images[user_choice])
computer_choice = random.randint(0,2)
print(f"Computer choice is {computer_choice}")
print(game_images[computer_choice])

#0 is rock, 1 is paper, and 2 is scissors

if user_choice >=3:
    print("You typed a wrong number.Try Again")
elif user_choice == 0 & computer_choice == 2:
    print("You Wins...")
elif user_choice == 2 & computer_choice == 0:
    print("You Lose...")
elif user_choice == computer_choice :
    print("It's a Draw...")
elif computer_choice > user_choice:
    print("You Lose")
elif user_choice > computer_choice:
    print("You Win...")