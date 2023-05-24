from tkinter import *


def button_click():
    my_lable['text'] = input.get()


window = Tk()
window.title("My first GUI programme")
window.minsize(500, 300)
# window.config(padx=20, pady=20)

# label
my_lable = Label(text="I am a label", font=("Arial", 25, "bold"))
my_lable['text'] = "Changing the text"
my_lable.grid(column=0, row=0)
my_lable.config(padx=50, pady=50)

# button
button = Button(text="click me", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

# input
inputs = Entry(width=10)
inputs.get()
inputs.grid(column=3, row=2)
# inputs.pack()

window.mainloop()
