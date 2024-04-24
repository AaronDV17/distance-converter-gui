from tkinter import *


def button_click():
    miles = float(miles_in.get())
    km = miles * 1.609344
    km_out.config(text=f"{km:.2f}")


window = Tk()
window.title = "Miles to Kilometers Converter"
window.config(padx=20, pady=20)

miles_in = Entry(width=5)
miles_in.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_out = Label(text="0")
km_out.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=button_click)
calc_button.grid(column=1, row=2)

window.mainloop()
