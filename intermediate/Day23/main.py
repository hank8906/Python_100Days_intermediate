import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize the object

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# press the key to move forward
screen.listen()
screen.onkey(player.move, "Up")

# Create a new car every 10 seconds

new_car_interval = 0.5
last_creation_time = time.time()

# game start

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Check if it's time to create a new car
    current_time = time.time()
    if current_time - last_creation_time >= new_car_interval:
        car_manager.generate_car()
        last_creation_time = current_time

    for car in car_manager.cars:
        car.forward(20)
        # Detect if player hit a car
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

        # if cars out of range then delete them
        if car.xcor() < -300:
            car.hideturtle()
            car_manager.cars.remove(car)
            del car

        # Detect if player touch the end-line\

        if player.ycor() > 250:
            player.goto(0, -280)
            scoreboard.add_level()
            new_car_interval -= 0.05


screen.exitonclick()



