import os
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
current_card = {}
word_list = {}

# ---------------------------read data------------------------------------ #
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

# ---------------------------flip the card------------------------------------ #


def flip_card():
    english_word = [dictionary["English"] for dictionary in word_list if dictionary["French"] ==
                    canvas.itemcget(word_text, "text")]
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfigure(title_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=english_word, fill="white")


# ---------------------------random_pick------------------------------------ #


def random_pick():
    """random choose a French word from the dict"""
    global current_card
    current_card = random.choice(word_list)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfigure(title_text, text="French", fill="black")
    canvas.itemconfigure(word_text, text=current_card["French"], fill="black")

    # flip the card 3 seconds after hitting the button
    window.after(3000, flip_card)


def is_known():
    word_list.remove(current_card)
    print(len(word_list))
    data_to_learn = pd.DataFrame(word_list)
    data_to_learn.to_csv("./data/words_to_learn.csv")
    random_pick()


# ---------------------------backward------------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Title Label
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "bold"))

# Word Label
initial_word = random.choice(word_list)['French']
word_text = canvas.create_text(400, 263, text=initial_word, font=(FONT_NAME, 60, "bold"))

# right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_pick)
wrong_button.grid(row=1, column=0)

# start the flash card
random_pick()


window.mainloop()
