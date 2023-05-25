from tkinter import *


def miles_to_kilo():
    miles = float(inputs.get())
    miles *= 1.60934
    # num_label["text"] = miles
    num_label.config(text=miles)


window = Tk()
window.title("Miles to kilometer converter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

inputs = Entry(width=10)
inputs.get()
inputs.grid(column=1, row=0)


mile_label = Label(text="Miles", font=("Arial", 20, 'bold'))
mile_label.grid(column=2, row=0)

op_label = Label(text="is equal to", font=("Arial", 20, "bold"))
op_label.grid(column=0, row=1)

num_label = Label(text=0, font=("Arial", 20, "bold"))
num_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(column=2, row=1)

btn = Button(text="calculate", command=miles_to_kilo)
btn.grid(column=1, row=2)

window.mainloop()
