from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json
PASSWORD_LENGTH = 16
PASSWORD_CHARS={
        0:["!","@","#","$","%","&","(",")","~"],
        1:["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],
        2:["0","1","2","3","4","5","6","7","8",],
        3:["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
}
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #password=""

    #for _ in range(0,PASSWORD_LENGTH):
    #    index=random.randrange(0,4)
    #    password += random.choice(PASSWORD_CHARS[index])
    password_list = [random.choice(PASSWORD_CHARS[random.randrange(0, len(PASSWORD_CHARS))]) for _ in
                     range(0, PASSWORD_LENGTH)]
    random.shuffle(password_list)
    password="".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    is_ok =messagebox.askokcancel(message=f"Are you ok to save password?\nWebsite:{website_entry.get()}"
                           f"\nEmail:{email_entry.get()}\nPassword:{password_entry.get()}")
    if is_ok:

        save_data= {
            website_entry.get():{
                "email":email_entry.get(),
                "password":password_entry.get(),
            }
        }
        data ={}
        try:
            with open("password.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password.json", "w") as data_file:
                json.dump(save_data, data_file,indent=4)
        else:
            data.update(save_data)
            with open("password.json", "w") as data_file:
                json.dump(data,data_file, indent=4)

        password_entry.delete(0,END)
        website_entry.delete(0,END)

def search_password():
    website_name= website_entry.get()
    try:
        with open("password.json", "r") as data_file:
            data = json.load(data_file)
            if website_name in data:
                details = data[website_name]
                password = details["password"]
                email = details["email"]
                password_entry.delete(0,END)
                password_entry.insert(0,password)
                email_entry.delete(0,END)
                email_entry.insert(0,email)
                messagebox.showinfo(website_name, f"Password Found:{password}")
            else:
                messagebox.showerror("Error","No record found for this website")
    except FileNotFoundError:
        messagebox.showerror("Error","No record found for this website")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
canvas= Canvas(window,width=200,height=200)
img=PhotoImage(file="lock.png")
canvas.create_image(100,100, image=img)

website_label= Label(text="Website")
email_label= Label(text="Email/UserName")
password_label= Label(text="Password")

website_entry= Entry(width=20)
email_entry= Entry(width=39)
password_entry= Entry(width=20)

password_button=Button(text="Generate Password",command=generate_password)
add_button=Button(text="Add",width=36,command=save_password)
search_button=Button(text="Search Password", command=search_password)

#--- Layout -- #
canvas.grid(row=0,column=1)
website_label.grid(row=1,column=0, sticky=E)
website_entry.grid(row=1,column=1,sticky=W)
search_button.grid(row=1,column=2,sticky=W)
website_entry.focus()
email_label.grid(row=2,column=0, sticky=E)
email_entry.grid(row=2,column=1,columnspan=2, sticky=W)
email_entry.insert(0,"manas.mk@gmail.com")
password_label.grid(row=3,column=0, sticky=E)
password_entry.grid(row=3,column=1, sticky=W)
password_button.grid(row=3,column=2, sticky=W)
add_button.grid(row=4,column=1,columnspan=2, sticky=W)

window.mainloop()