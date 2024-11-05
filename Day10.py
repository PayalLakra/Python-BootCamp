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