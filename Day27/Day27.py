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
from tkinter import *

window = Tk()                               # Window
window.title("My first GUI Program.")       # Title
window.minsize(width =1000,height =300)     # Size
window.config(padx=100, pady=200)

my_label = Label(text = "I am a Label", font =("Arial",24,"italic"))   # Label
# my_label.pack(side="left")          # To pack the label onto the screen

# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)

button = Button(text="Click me")      # Button
button.grid(column=1, row=1)
# button.pack()

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)                                     # Input
input.get()
input.grid(column=3, row=2)
# input.pack()

window.mainloop()

## Pack -- it basically packs each of the widgets next to each other in a vaguely logical format.
## Place -- Place is all about precise positioning.

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