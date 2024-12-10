'''
Topics to be covered:
- List Comprehension
- Dictionary Comprehension
- Iterate Over a Panda Data Frame
- NATO Alphabet Project
'''

# List Comprehension
# Old method to add 1 to each number in a list:
numbers = [1,2,3]
new_list = []
for n in numbers:
    add = n +1 
    new_list.append(add)
    print(new_list)

# New Method using List Comprehension:
# BASIC SYNTAX: new_list = [new_item for item in list]
number = [1,2,3]
new_list = [(n+1) for n in number]
print(new_list)

name = "Payal"
letters = [letter for letter in name]
print(letters)

range_list = [num*2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension
# BASIC SYNTAX : new_list = [new_item for item in list if test]

list1 = [1,2,3,4,5,6,7,8,9,10]
differentiate = [num for num in list1 if num > 5]
print(differentiate)

# Squaring Numbers
# You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [(item * item) for item in numbers]
print(squared_numbers)

# Filtering Even Numbers
# Filter out the even numbers from a series of numbers.
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if (num % 2 == 0)]
print(result)

# Dictionary Comprehension
# BASIC SYNTAX: new_dict = {new_key:new_value for item in list}

names = ["A","B","C","D","E"]
import random

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_Students = {student:score for (student,score) in student_scores.items() if score >=60}
print(passed_Students)

# Create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp * 9/5) + 32 for day, temp in weather_c.items()}
print(weather_f)

# Iteration over a Panda Dataframe
student_Dict = {"student" : ["A","B","C"],"score":[56,78,44]}

# for (key,value) in student_Dict.items():
#     print(value)  #Normal Way

import pandas

student_data_frame = pandas.DataFrame(student_Dict)
print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    print(row)

#NATO PROJECT
import csv

with open ("Day26\\nato_phonetic_alphabet.csv", mode="r") as file:
    csv_Reader = csv.DictReader(file)
    nato_dict = {row['letter'].upper():row['code'] for row in csv_Reader}

def generate_phonetic():
    user_input = input("Enter a word:").upper()
    phonetic_list = [nato_dict[letter] for letter in user_input]
    print(phonetic_list)

generate_phonetic()