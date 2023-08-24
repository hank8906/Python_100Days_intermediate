from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 80, 'normal')


class ScoreBoard(Turtle):
    """count the score for each side"""
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}",move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_end(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGN, font=FONT)