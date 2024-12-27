from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")    # get request to API
    response.raise_for_status()                          # raise exception
    data = response.json()                               # Parse the JSON to obtain quote text
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)            # Display the quote in canvas widget


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day33\\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day33\\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()