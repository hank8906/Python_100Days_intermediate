from turtle import Turtle

DISTANCE = 50


class Paddle(Turtle):
    """create paddle and make them move"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(4, 1)
        self.goto(position)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
