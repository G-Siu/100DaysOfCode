from tkinter import *

window = Tk()
window.title("Miles to Kilometres")
window.config(padx=25, pady=25)

user_input = Entry(width=10)
user_input.config(font=("Arial", 12))
user_input.grid(column=1, row=0)

equal = Label(text="is equal to", font=("Arial", 12))
equal.grid(column=0, row=1)
equal.config(padx=10, pady=10)

miles = Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

km = Label(text="km", font=("Arial", 12))
km.grid(column=2, row=1)
km.config(padx=10, pady= 10)

result = Label(text="0", justify="center", font=("Arial", 12))
result.grid(column=1, row=1)
result.config(padx=10, pady= 10)


def button_clicked():
    user_miles = round(float(user_input.get()) * 1.609)
    result.config(text=user_miles)


button = Button(text="Calculate", command=button_clicked, font=("Arial", 12))
button.grid(column=1, row=2)

window.mainloop()
