''' TOPICS TO BE COVERED ON DAY1 :
- STRINGS
- PRINT STATEMENTS (\n)
- CONCATENATION
- ERRORS: Identation, Syntax, Name, 
- INPUT() FUNCTION
- COMMENTS: "#" - FOr Single Line , "''''''" - for multiple line
- VARIABLES
- LENGTH - len() function
'''

#STRINGS -- A Sequence of Characters {"Hello World" - Eg}
print("Hello World!")

#CODING EXERCISE
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

#NOTE: \n is used to create a new line.

#CONCATENATION
print("HELLO" + " " + "EARTH" + "!")    #(adding space before EARTH)

#INPUT - A Prompt for the user
#VARIABLES -- A Container that store data values.
name = input("What is your name?")    #A Variable name is created and name of the person is stored into it.
print("Hello " + name + "!")    # Put an input statement into another print statement
print(len(name))

#PROJECT:1 
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew in?\n")
pet_name = input("What's your pet's name?\n")
print("Your band name could be "+ city + " " + pet_name)