'''
Topics to be Covered:
- Catching Exceptions - Try, Catch block
- 
'''

# KeyError
a_dict = {"key":"value"}
val = a_dict["non_existing"]
print(val)

# FileNotFoundError
with open("a.txt") as file:
    file.read()

#IndexError
fruit_list = ["A","b"]
print(fruit_list[4])

# TypeError
text = "abc"
print(text + 5)

# CATCHING EXCEPTIONS ::
# -> try  : Something that might cause an exception
# -> except : Do this if there was an exception
# -> else : Do this if there were no exceptions
# -> finally : Do this no matter what happens

# Example:
try :
    with open("a.txt") as file:
        file.read()
except:    # we can have multiple except block
    print("FileNotFoundError")
else:
    print("Do this if nothing above happens.")
finally:
    print("At the end finally block always to be called.")

# Raising own exceptions
height = input("Enter height")
weight = input("Enter weight")
if height > 3:
    raise ValueError

bmi = weight / height ** 2
print(bmi)

# EXERCISE
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)

# EXERCISE
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            # If the 'Likes' key is missing, skip or assume 0 likes
            total_likes += 0
    return total_likes

print(count_likes(facebook_posts))