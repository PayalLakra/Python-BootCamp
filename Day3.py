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