'''
TOPICS TO BE COVERED:
- PRIMITIVE DATA TYPES - 
- TYPE CONVERSION
- type() function
- MATHEMATICAL OPERATIONS
- Priority in Mathematical Operators
- NUMBER MANIPULATION
- Assignment Operator
- f- String
'''

#PRIMITIVE DATA TYPES -- Strings, Integer , Float, Boolean

# Type Conversion
print("123" + "456")    #By default everything is string, we have to convert it into required.
print(float(123 + 456))  # Convert it into float
print(123+456)    #By default it is int

# Subscripting -- is method of pulling out a particular element from a string.
name = "PAYAL"
print(name[2])    #Starting from 0 to n-1
print(name[-1])   #From Back it starts from -1 to -n

num = 12345
print(type(num))

username = input("Enter your name:")
length = len(username)
print("Characters in name is: " + str(length))    # As to Concatenate we should have same data type

#BMI CALCULATOR
h = int(input("Enter your height(in cm):"))
height = h/100
weight = int(input("Enter your weight: "))
bmi = weight / height ** 2
print(bmi)

#Mathematical Operators --  +,-,*,/,//,**
print(7+3)
print(7-3)
print(7*3)
print(6/3)   #by default it gives float
print(5//3)  #floor division & results type int
print(2**3)

#Priority of Operators - PEMDAS(Parenthesis,Exponents,Multiply,Division,Addition,Subtraction)
print(3*3+3-3)    #Gives 9

#Assignment Operator
marks = 0
marks +=1    #assignment operator
print(marks)

#f- string
print(f"The marks are: {marks}")  

#PROJECT 2 -- TIP CALCULATOR

print("Welcome to the Tip Calculator!")
bill = int(input("What's the total bill? $"))
tip = int(input("How much do you like to give? 10,20 or 30? "))
percent = (tip/100) * bill
people = int(input("How many people to split the bill?"))
amount = (bill + percent) / people
print(f"Each Person should pay : ${amount:.2f}")