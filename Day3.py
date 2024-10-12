'''
TOPICS TO BE COVERED:
- Conditional Statement - if else, nested if else,elif
- Comparison Operator - >,>=,<,<=,==,!=
- Modulo (%) Operator
- Logical Operator - or,not,and
'''

# IF-ELSE
print("Welcome to Roller Coster!")
age = int(input("Enter your age?"))
if age >= 18:
    print("Welcome")
else:
    print("You are too small.")

# = means assigning one value to a variable
# == means checking equality

#Modulo Operator results the remainder
print(10%3)

#Odd-Even
num = int(input("Enter the number you want to check:"))
even = num % 2
if even == 0:
    print("Number is even")
else:
    print("Number is Odd.")

#Nested if-else and elif
height = int(input("Enter your height:"))
if height >=18:
    age = int(input("Enter your age:"))
    if age >= 18:
        print("Fees if $20")
    elif age >=12:
        print("Fees is $10")
    else:
        print("Fees is $5")
else:
    print("Not eligible")

#Pizza Delivery
print("Welcome to Python Pizza Delivery :)")
size = input("What size do you want? S,M,L -")
pepp = input("Do you want pepproni in your pizza? Y or N -")
cheese = input("Do you want extra cheese? Y or N -")

if size == "S":
    bill = 10
    if pepp == "Y":
        bill += 5
    if cheese == "Y":
        bill += 3
    print(f"Please Pay $ {bill}")
elif size == "M":
    bill = 20
    if pepp == "Y":
        bill += 8
    if cheese == "Y":
        bill += 5
    print(f"Please Pay $ {bill}")
elif size == "L":
    bill = 30
    if pepp == "Y":
        bill += 10
    if cheese == "Y":
        bill += 8
    print(f"Please Pay $ {bill}")
else:
    print("Opt Correct Options.")

#Logical Operators - and/or/not
age = int(input("Enter age:"))
if age == 18 or age >= 18:
    print("Adult")
elif age == 17 and age == 18:
    print("Going to be Adult.")

a = int(input("Enter a number:"))
result = not a == 18      #returns true if a is not 18.
print(result)

#Project -3 (Treasure Island)
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************
''')
print("Welcome to Tresure Island.Your mission is to find the treasure.")
print("You're at the crossroad. Now, Where do you want to go?")
step1 = input("Type'Left'or 'Right'\n").lower()
if step1 == "left":
    print("You've come to a lake.There is an Island in the middle of the lake.")
    step2 = input("Type 'Wait' to wait for a boat or 'Swim' to swim across.\n").lower()
    if step2 == "wait":
        print("Which door you want to take?")
        step3 = input("Red, Yellow, Blue\n").lower()
        if step3 == "red":
            print("Burned by fire.\nGAME OVER")
        elif step3 == "yellow":
            print("HURRRRAAAAAYYYYYY!!\nYOU WIN")
        elif step3 == "blue":
            print("Eaten by beasts.\nGAME OVER")
        else:
            print("GAME OVER")
    elif step2 == "swim":
        print("Attacked by trout.\nGAME OVER")
    else:
        print("Attacked by trout.\nGAME OVER")
elif step1 == "right":
    print("You fall into a hole...\n GAME OVER") 
else:
    print("You fall into a hole...\n GAME OVER")       