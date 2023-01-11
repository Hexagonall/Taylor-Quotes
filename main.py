from tkinter import *
import requests

api = "https://api.kanye.rest"

def get_quote():
    response = requests.get(api)
    response.raise_for_status()
    data = response.json()["quote"]
    result = canvas.itemconfig(quote_text,text=data)
    return result


window = Tk()
window.title("Taylor Says...")
window.config(padx=50, pady=60)

canvas = Canvas(width=300, height=420)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Taylor Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor.png")

taylor_button = Button(image=taylor_img, highlightthickness=0, command=get_quote)
taylor_button.grid(row=1, column=0)



window.mainloop()