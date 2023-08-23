from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 12, 'normal')


class ScoreBoard(Turtle):
    """count the score and show it in final result"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(0, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()



