from turtle import Turtle

ALIGN = "left"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over",move=False, align="center", font=FONT)
