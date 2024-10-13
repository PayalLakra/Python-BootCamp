'''
Topics to be Covered:
- For loops
- Inbuilt functions - sum,max,range
- Password Generator
-
-
'''
#Loops - to repeat a process untill a certain condiiton is not met.
#Loops - allows us to execute multiple times the same code.
fruits = ["APPLE","MANGO","PEAR","PAPAYA","BANANA"] 
for i in fruits:
    print(i)

student_score = [12,43,53,21,45,78,43,78,43,89,34,67,89,54,25,25,78] 
total = sum(student_score)     # an inbuilt function to perform summation
print(total)

#sum function
sum =0
for score in student_score:
    sum += score
print(sum)    #this is how the sum function is created but as it is inbuilt we can use it anytime with just one keyword sum.

#max function
max = 0
for score in student_score:
    if score > max:
        max = score     # Note that only 1 = is used here
print(max)

#range function
for i in range(1,10):
    print(i)
for i in range(1,11,2):
    print(i)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

#FIZZ BUZZ
for number in range(1,101):
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

#Py Password Generator
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
print("Welcome to PyPassword generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

password_list = []     # Create lists for each character type
password_list += [random.choice(letters) for _ in range(nr_letters)]  # Add random letters to the password list
password_list += [random.choice(symbols) for _ in range(nr_symbols)]  # Add random symbols to the password list
password_list += [random.choice(numbers) for _ in range(nr_numbers)]  # Add random numbers to the password list
random.shuffle(password_list)         # Shuffle the password list to make it more random
password = ''.join(password_list)     # Convert the list to a string to form the final password

print(f"Your Password is: {password}")