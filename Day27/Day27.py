'''
Topics to be Covered:
- Labels and Windows in tkinter
- args, kwargs
- Buttons, Entry and setting component options
- Tkinter Widgets -  Radiobuttons, Scales, Checkbuttons
- Tkinter layout Managers: pack(), place(), grid()
- Project : Mile to kilometres Converter project
'''

import tkinter

window = tkinter.Tk()                       # Window
window.title("My first GUI Program.")       # Title
window.minsize(width =100,height =300)      # Size

my_label = tkinter.Label(text = "I am a Label", font =("Arial",24,"italic"))   # Label
my_label.pack(side="left")          # To pack the label onto the screen

window.mainloop()