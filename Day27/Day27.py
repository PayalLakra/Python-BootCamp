'''
Topics to be Covered:
- Labels and Windows in tkinter
- Advanced Python Argument
- args, kwargs
- Buttons, Entry and setting component options
- Tkinter Widgets -  Radiobuttons, Scales, Checkbuttons
- Tkinter layout Managers: pack(), place(), grid()
- Project : Mile to kilometres Converter project
'''

import tkinter

window = tkinter.Tk()                       # Window
window.title("My first GUI Program.")       # Title
window.minsize(width =1000,height =300)      # Size

my_label = tkinter.Label(text = "I am a Label", font =("Arial",24,"italic"))   # Label
my_label.pack(side="left")          # To pack the label onto the screen

window.mainloop()

# Advanced Python Argument - Arguments with Default values
def my_function(a=1,b=2,c=3):
    print(a)
    print(b)
    print(c)

my_function()
my_function(b=5)     # Change only b value and rest remains same

# Unlimited Arguments
def adding(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(adding(3,5,6,7,8,9,10))
# *args results tuple.

# **kwargs - Many keyworded arguments
def calculate(n, **kwargs):
    for key, value in kwargs.items():
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)

calculate(2, add=3, multiply=5)
# **kwargs results dictionary.