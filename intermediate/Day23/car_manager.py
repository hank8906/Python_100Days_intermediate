import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.generate_car()

    def generate_car(self):
        """create new car randomly"""
        car = Turtle(shape="square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(300, random.randint(-240, 240))
        self.cars.append(car)



