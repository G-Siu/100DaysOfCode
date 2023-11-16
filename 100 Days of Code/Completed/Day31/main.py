from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/german_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ----------------------------------Next Word------------------------------------#
def next_word():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_display, text="German", fill="black")
    canvas.itemconfig(word_display, text=current_card["German"], fill="black")
    canvas.itemconfig(card, image=card_before)
    timer = window.after(3000, reveal_answer)


def reveal_answer():
    canvas.itemconfig(card, image=card_after)
    canvas.itemconfig(title_display, text="English", fill="white")
    canvas.itemconfig(word_display, text=current_card["English"], fill="white")


def known_words():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)

    next_word()


# --------------------------------------UI----------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_before = PhotoImage(file="images/card_front.png")
card_after = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_before)
canvas.grid(row=0, column=0, columnspan=2)

title_display = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_display = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=known_words)
right_button.grid(row=1, column=1)
right_button.config(borderwidth=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)
wrong_button.config(borderwidth=0)

timer = window.after(3000, reveal_answer)
next_word()


window.mainloop()
