import requests
from tkinter import *

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())

def get_random_quote():
    response = requests.get("https://api.kanye.rest")
    canvas.itemconfig(quote, text=response.json()["quote"])

window = Tk()
window.title("Kanye Quotes")
window.config(padx=50, pady=50)

img=PhotoImage(file="background.png")
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=img)
quote= canvas.create_text(150,207, text="Click Kanye", font=("Arial", 24, "bold"), width=200)
img2=PhotoImage(file="kanye.png")
btn=Button( image=img2, command=get_random_quote)

canvas.pack()
btn.pack()





window.mainloop()