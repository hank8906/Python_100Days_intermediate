from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.penup()
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """refresh the food position"""
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position,y_position)
