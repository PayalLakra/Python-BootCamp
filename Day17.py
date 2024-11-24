'''
Topics to be Covered:
- Classes
- Attributes of class
- Adding methods to class
- pass keyword
- Constructor
- Quiz Game
'''

# Class Creat

class UpsideDownLabs:          # Class is creates
    def __init__(self):        # Constructor is initilized
        pass

payal = UpsideDownLabs()            # Object created
payal.user_id = "111"               # Attributes of object
payal.dept = "Tech"
print(payal.dept)

# OR we can use the below method

class User:
    def __init__(self, user_id, user_name, followers=0):    # This is Constructor
        self.id = user_id
        self.username = user_name
        self.followers = followers
        self.following = 0

# When a function is attached to an object, then it is called as a Method.
    def follow(self, user):    # This is a Method
        user.followers += 1
        self.following += 1

user_1 = User(1, "Payal")
user_2 = User(2, "Ritika")
print(user_1.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)