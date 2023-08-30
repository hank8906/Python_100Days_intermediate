from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=0, columnspan=2)

# Title Label
title_text = Label(text="Title", bg="white")
title_text.config(padx=5, pady=5, font=(FONT_NAME, 40, "italic"))
title_text.place(x=335, y=150)

# Word Label
word_text = Label(text="word", bg="white")
word_text.config(padx=5, pady=5, font=(FONT_NAME, 60, "bold"))
word_text.place(x=295, y=263)

# right button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

# wrong button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)



window.mainloop()