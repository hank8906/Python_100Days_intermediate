from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# initialize the screen

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pond")
screen.tracer(0)

# initialize the object

my_paddle = Paddle((350, 0))
com_paddle = Paddle((-350, 0))
ball = Ball()

# listen to the key being press and action with the direction being choosed

screen.listen()
screen.onkey(my_paddle.up, "Up")
screen.onkey(my_paddle.down, "Down")
screen.onkey(com_paddle.up, "w")
screen.onkey(com_paddle.down, "s")

# game start

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.003)
    ball.move_ball()

    if ball.distance(my_paddle) < 50 and ball.xcor() > 320 or ball.distance(com_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if ball.xcor() > 390 or ball.xcor() < -390:
        game_is_on = False





screen.exitonclick()