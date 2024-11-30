'''
Topics to be Covered:
- Calculator- Project
- Functions with output
- Docstrings
'''

#Convert into Title Case
f_name = input("Enter your first name:")
l_name = input("Enter your last name:")

def name(f_name, l_name):
    if f_name == "" or l_name == "":
        return     #return none on console
    title_name = f"{f_name.title()} {l_name.title()}"
    return title_name

result = name(f_name=f_name, l_name=l_name)
print(result)

#Leap Year check
def is_leap_year(year):
    """Function to check whether an year is a leap year or not."""   #this is a way to create a docstring to provide details of the function that we created.Now whenever we hover over the function then it tells us about those details that we provide as docstring.
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    return False
#The return keyword will exit function & prevent rest of the code from being executed.  
print(is_leap_year(2024))


# CALCULATOR PROJECT

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2 

dict = {"+" : add, 
        "-" : subtract,
        "*" : multiply, 
        "/" : divide}

num1 = float(input("Enter first number:"))
should_continue = True
while should_continue:
    for symbol in dict:
        print(symbol)
    operation = input("Pick an Operation:")
    num2 = float(input("Enter second number:"))
    answer = (dict[operation](num1, num2))
    print(f"{num1} {operation} {num2} = {answer} ")

    choice = input((f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation.")).lower()

if choice == "y":
    num1 = answer
elif choice == "n":
    should_continue = False
    print("\nThanks!")