'''
Topics to be covered:
- Inheritance
- Slice list and Dictionary
- Snake Game
'''

# Class Inheritance : By using this the child class get all the access from the parent class
# Example:
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


class Fish(Animal):   # Animal is the parent class
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()     # First get the access from parent class
        print("Under water")  # Then in addition we can get extra functionality for child class only.

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()        # This is the method of Fish class itself.
nemo.breathe()     # This is the method associated with Animal class but it is inherited by Fish class.

# Slicing
letters = ["a","b","c","d","e"]
print(letters[2:3])
print(letters[3:])
print(letters[1:5:1])
print(letters[::-1])
# Same thing can be done with Tuples as well