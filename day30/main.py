from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

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

    if len(website) <= 0:
        messagebox.showinfo(title=website, message="website cannot be null")
    elif len(emailuser) <= 0:
        messagebox.showinfo(title=emailuser, message="Email cannot be null")
    elif len(pword) <= 0:
        messagebox.showinfo(title=pword, message="Password cannot be null")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered \n {website} \n {emailuser} \n {pword}")

        if is_ok:
            with open("loginDetails.txt", "a") as file:
                file.write(f"{website} | {emailuser} | {pword} \n")
                websiteEntry.delete(0, END)
                emuserEntry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logoImg = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logoImg)
canvas.grid(column=1, row=0)

websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0, row=1)

websiteEntry = Entry(width=35)
websiteEntry.focus()
websiteEntry.grid(column=1, row=1, columnspan=2)

emuserLabel = Label(text="Email/Username:")
emuserLabel.grid(column=0, row=2)

emuserEntry = Entry(width=35)
emuserEntry.insert(0, 'alex@gmail.com')
emuserEntry.grid(column=1, row=2, columnspan=2)

pwrdLabel = Label(text="password:")
pwrdLabel.grid(column=0, row=3)

pwrdEntry = Entry(width=21)
pwrdEntry.grid(column=1, row=3)

genBtn = Button(text="Generate password", command=pwordgen)
genBtn.grid(column=2, row=3)

addBtn = Button(text="Add", width=36, command=save_to_file)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()
