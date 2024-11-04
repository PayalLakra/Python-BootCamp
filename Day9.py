'''
Topics to be covered:
- Dictionary
- Auction Program -Project
'''

# Dictionary = {}, key-value pairs

dict1 = {0:"Payal",2:"Nikki",3:"Shaksham"}
print(dict1[0])
#print(dict[1])    #get key error as 1 is not in the dict1

dict1[1] = "tannu"   #add this value at the end of dict1
dict1[2] = "vinny"    #update the value
print(dict1)

empty_dict = {}    #way to create empty dictionary then we can add values
print(empty_dict)

#Loop through dictionary
for num in dict1:
    print(num)    #it will give only keys
    print(dict1[num])  #now this will give values

# Write a program that converts their scores to grades
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

#Nested Dictionary
travel = {"France": ["Paris","Lille","Dijon"],
          "Germany" : {"Berlin","Stuttgart"}}
print(travel["France"][1])    #Gives Lille

#Nested List
nested_list = ["A","B","C",["D","E"]]
print(nested_list[3][1])    #Gives E

#list nested inside a dictionary which is nested inside another dictionary
travel_log = {
    "France":{
        "cities_visited": ["Paris","Lille","Dijon"],
        "total_visited" :12
    },
    "Germany":{
        "cities_visited": ["Berlin","Stuttgart"],
        "total_visited" :8
    }
}
print(travel_log["Germany"]) 
print(travel_log["Germany"]["cities_visited"][1]) 

#AUCTION PROGRAM
print('''
___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
''')
print("WELCOME TO THE SECRET AUCTION PROGRAM")
name = input("What is your name?:").lower()
age = int(input("What's your bid?: $"))
permit = input("Are there any other bidders? Type 'yes' or 'no'.\n")