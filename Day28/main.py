from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():

    count_down(5)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    count_down(5*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # change count to minute and second
    minute = math.floor(count / 60)
    second = count % 60

    canvas.itemconfig(time_text, text=f"{minute}:{second}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# Timer Label
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), highlightthickness=0, bg=YELLOW)
timer.grid(row=0, column=1)

# Check Label
check = Label(text="✅", fg=GREEN, font=(FONT_NAME, 12, "bold"), highlightthickness=0, bg=YELLOW)
check.grid(row=3, column=1)

# Start and Reset button

start_button = Button(text="Start", command=start_count_down)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",command=time_reset)
reset_button.grid(row=2, column=2)

window.mainloop()
