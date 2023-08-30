from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

# ---------------------------read data------------------------------------ #
df = pd.read_csv("./data/french_words.csv")
word_list = df.to_dict(orient="records")

# ---------------------------random_pick------------------------------------ #


def random_pick():
    random_word = random.choice(word_list)['French']
    canvas.itemconfigure(title_text, text="French")
    canvas.itemconfigure(word_text, text=random_word)


# ---------------------------backward------------------------------------ #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=0, columnspan=2)

# Title Label
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "bold"))

# Word Label
initial_word = random.choice(word_list)['French']
word_text = canvas.create_text(400, 263, text=initial_word, font=(FONT_NAME, 60, "bold"))

# right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_pick)
right_button.grid(row=1, column=1)

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_pick)
wrong_button.grid(row=1, column=0)

random_pick()

window.mainloop()
