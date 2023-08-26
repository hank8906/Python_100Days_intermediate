import turtle
import pandas as pd

ALIGN = "center"
FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.title("U.S. States Game")

# initialize another turtle object
state = turtle.Turtle()
state.penup()
state.color("black")
state.hideturtle()

# read the csv inside the project
df = pd.read_csv("50_states.csv")

state_list = df["state"].tolist()
# print(state_list)

guessed_states = []

# check if the input state is really exist


def state_exists(answer):
    if df["state"].str.contains(answer).any():
        x_position = int(df[df.state == f"{answer}"].x)
        y_position = int(df[df.state == f"{answer}"].y)
        state.goto(x_position, y_position)
        state.write(f"{answer}", move=False, align=ALIGN, font=FONT)
        guessed_states.append(answer)
    else:
        pass


# game start

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct",
                                    prompt="What's another states' name?").title()
    if answer_state == "Exit":
        set1 = set(state_list)
        set2 = set(guessed_states)
        difference = set1.symmetric_difference(set2)
        all_differences = list(difference)
        dataframe = pd.DataFrame({"states_not_guessed" : all_differences})
        dataframe.to_csv("States_not_guesses.csv")
        break

    state_exists(answer_state)

screen.exitonclick()
