from turtle import Turtle

X_POSITION = [0, -20, -40]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    """To illustrate all the attributes and actions about snake"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for index in X_POSITION:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.setx(index)
            self.segments.append(turtle)

    def move(self):
        # let segments move from last to first continually, to success the position and update their index
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
