'''
Topics to be Covered:
-Debugging
-
'''

# Debugging: The process of removing bug from the code.

#Debugging Exercise
year = int(input("Enter your Birth Year:"))
if year >= 1980 and year < 1994:
    print("Millenial")
elif year >= 1994:
    print("Gen Z")

# Leap Year (other way)
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap(2750))

#FIZZBUZZ
num = int(input("Enter number:"))
def fizzbizz(num):
    for i in range(1, num+1):
        if i % 5 == 0 and i % 3 == 0:
            print("FIZZBUZZ")
        elif i % 3 == 0:
            print("FIZZ")
        elif i % 5 == 0:
            print("BUZZ")
        else:
            print(num)

print(fizzbizz(num=num))

# We can use Try-Except block to avoid any errors
try:
    age = int(input("Enter your age:"))
    if age >18:
        print("You can drive")
    else:
        print("You can't drive")
except:
    print("Please enter a valid age.")