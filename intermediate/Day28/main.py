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
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_text.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_min)
        timer_text.config(text="Work")

    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_text.config(text="Short break", fg=PINK)

    elif reps % 8 == 0:
        count_down(long_break_min)
        timer_text.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    # change count to minute and second
    minute = math.floor(count / 60)
    second = count % 60

    # change 0 to 00 and 9 to 09
    if second == 0:
        second = "00"
    elif 0 < second < 10:
        second = "0" + f"{second}"

    # show count down on the canvas
    canvas.itemconfig(time_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count_down()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✅"
        check.config(text=mark)


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
timer_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), highlightthickness=0, bg=YELLOW)
timer_text.grid(row=0, column=1)

# Check Label
check = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"), highlightthickness=0, bg=YELLOW)
check.grid(row=3, column=1)

# Start and Reset button

start_button = Button(text="Start", command=start_count_down)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=time_reset)
reset_button.grid(row=2, column=2)

window.mainloop()
