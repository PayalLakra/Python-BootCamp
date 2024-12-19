'''
Topic to be Covered:
- Canvas Widget, Adding Images
- Adding a Count Down Mechanism
- Dynamic Typing
- Setting Different Timer Sessions and Values
- Adding Checkmarks and Resetting the Application
'''

from tkinter import *
from PIL import Image, ImageTk
import time

# ------------------------ CONSTANTS -------------------------- #
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
YELLOW = "#FFFF00"
GREEN = "#66ff00"
FONT_NAME = "Courier"
TIMER = None
reps = 0

# ------------------------ TIMER RESET -------------------------- #
def reset_timer():
    global reps
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    reps = 0

# ------------------------ TIMER MECHANISM -------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg="blue")
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ------------------------ COUNTDOWN MECHANISM -------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Tomato Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Add title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

# Create a canvas for the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = Image.open("C:\\Users\\PAYAL\\Desktop\\Payal STUDY\\Python-BootCamp\\Day28\\tomato.jpeg")
tomato_img = ImageTk.PhotoImage(tomato_image)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 25, text="00:00", fill="black", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# Add start and reset buttons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Add checkmark label below the tomato
checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()

# Dynamic Typing: Change a variable's data type by changing the content in that variable.