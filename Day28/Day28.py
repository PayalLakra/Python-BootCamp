'''
Topic to be Covered:
- Canvas Widget, Adding Images
- Adding a Count Down Mechanism
- Dynamic Typing
- Setting Different Timer Sessions and Values
- Adding Checkmarks and Resetting the Application
'''

## UI SETUP
from tkinter import *
from PIL import Image, ImageTk  # Import from Pillow

window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg="#FFFF00")

# Create a Canvas
canvas = Canvas(width=200, height=224)
canvas.pack()

# Load the image using Pillow
tomato_image = Image.open("C:\\Users\\PAYAL\\Desktop\\Payal STUDY\\Python-BootCamp\\Day28\\tomato.jpeg")
tomato_img = ImageTk.PhotoImage(tomato_image)

# Add the image to the Canvas
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100,70, text="00:00", font=(30))

window.mainloop()