from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.speed("fastest")
        self.color("purple")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

