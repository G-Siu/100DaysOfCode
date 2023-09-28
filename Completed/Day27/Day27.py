from tkinter import *

window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # Adds boundary around program

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()  # .pack() places element on screen and centres it
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)  # Can't use grid with pack
my_label.config(padx=50, pady= 50)
# my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="I'm New", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=3)



window.mainloop()  # Keep window open, has to be at end
