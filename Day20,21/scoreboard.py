from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial', 20, 'normal')

with open("Data.txt", mode="r") as file:
    high_score = file.read()
    file.close()


class ScoreBoard(Turtle):
    """count the score and show it in final result"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = int(high_score)
        self.penup()
        self.color("white")
        self.setposition(0, 250)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highScore} ", move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("Data.txt", mode="w") as file:
                file.write(str(self.highScore))
                file.close()

        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()



