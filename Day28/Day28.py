'''
Topic to be Covered:
- Canvas Widget, Adding Images
- Adding a Count Down Mechanism
- Dynamic Typing
- Setting Different Timer Sessions and Values
- Adding Checkmarks and Resetting the Application
'''

from tkinter import *
from PIL import Image, ImageTk  # Import from Pillow

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Tomato Timer")
window.config(padx=100, pady=50, bg="#FFFF00")  # Add padding and background color

# Add title label
title_label = Label(text="Timer", fg="#66ff00", bg="#FFFF00", font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

# Create a canvas for the tomato image and timer text
canvas = Canvas(width=200, height=224, bg="#FFFF00", highlightthickness=0)
tomato_image = Image.open("C:\\Users\\PAYAL\\Desktop\\Payal STUDY\\Python-BootCamp\\Day28\\tomato.jpeg")
tomato_img = ImageTk.PhotoImage(tomato_image)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 25, text="00:00", fill="black", font=("Courier", 25, "bold"))
canvas.grid(column=1, row=1)

# Add start and reset buttons
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Add checkmark label below the tomato
checkmark_label = Label(text="", fg="#66ff00", bg="#FFFF00", font=("Courier", 24, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()