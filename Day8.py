'''
Topics to be covered:
- Cipher Program
- Functions with input,parameters and arguments
- 
'''

#Function with inputs
def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice?")
greet("payal")

#the parameter is the name of the data that's being passed in. Here parameter is name
#the argument is the actual value of the data.Here argument is payal

#Your life in weeks

current_age = int(input("What is your current age?"))
def life_in_weeks(current_age):
    left_weeks = int(90*52)
    current_age_week = current_age*52
    X = int(left_weeks - current_age_week)
    print(f"You have {X} weeks left.")

life_in_weeks(current_age)

#function with two parameters
def greet_with(name,location):
    print(f"How are you {name}?")
    print(f"Oh! so you are living in {location}.")

greet_with("Payal","Delhi")   #Positional argument
greet_with(location="New Delhi",name="Nikki")   #Keyword argument

#LOVE SCORE
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')
    love_score = int(f"{true_count}{love_count}")
    print(love_score)

calculate_love_score("Anil", "Babita")