from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def pwordgen():
    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_nums = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_nums

    shuffle(password_list)

    pword = "".join(password_list)
    pwrdEntry.delete(0, END)
    pwrdEntry.insert(0, pword)
    pyperclip.copy(pword)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = websiteEntry.get()
    emailuser = emuserEntry.get()
    pword = pwrdEntry.get()
    new_data = {
        website:{
            "email": emailuser,
            "password": pword
        }
    }

    if len(website) == 0 or len(pword) == 0:
        messagebox.showinfo(title="Oops", message="no field can be empty")
    else:
        try:
            with open("loginDetails.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("loginDetails.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("loginDetails.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            websiteEntry.delete(0, END)
            emuserEntry.delete(0, END)

# ---------------------------- find Password ------------------------------- #
def findPword():
    website = websiteEntry.get()
    try:
        with open("loginDetails.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="data file does not  exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n {password}")
        else:
            messagebox.showinfo(title="Error", message="Website does not exist")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website")
websiteLabel.grid(column=0, row=1)

websiteEntry = Entry(width=21)
websiteEntry.focus()
websiteEntry.grid(column=1, row=1)

emuserLabel = Label(text="Email/Username:")
emuserLabel.grid(column=0, row=2)

emuserEntry = Entry(width=38)
emuserEntry.insert(0, 'alex@gmail.com')
emuserEntry.grid(column=1, row=2, columnspan=2)

pwrdLabel = Label(text="password:")
pwrdLabel.grid(column=0, row=3)

pwrdEntry = Entry(width=21)
pwrdEntry.grid(column=1, row=3)

srcBtn = Button(text="serach", width=13, command=findPword)
srcBtn.grid(column=2, row=1)

genBtn = Button(text="Generate password", command=pwordgen)
genBtn.grid(column=2, row=3)

addBtn = Button(text="Add", width=36, command=save_to_file)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()
