from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
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
my_score = ScoreBoard((100, 190))
com_score = ScoreBoard((-100, 190))

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
    time.sleep(ball.move_speed)
    ball.move_ball()

    # ball bounce back the paddle
    if ball.distance(my_paddle) < 60 and ball.xcor() > 330 or ball.distance(com_paddle) < 60 and ball.xcor() < -330:
        ball.bounce_paddle()

    # ball bounce back from the up and down wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    # Detect out of bound action in right
    if ball.xcor() > 390:
        com_score.add_score()
        ball.goto(0, 0)
        ball.move_speed = 0.05
        ball.bounce_paddle()

    # Detect out of bound action in left
    if ball.xcor() < -390:
        my_score.add_score()
        ball.goto(0, 0)
        ball.bounce_paddle()





screen.exitonclick()