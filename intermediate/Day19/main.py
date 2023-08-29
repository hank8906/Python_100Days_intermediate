from turtle import Turtle, Screen
import random
import threading

screen = Screen()

screen.setup(width=500, height=400)

while True:
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color: ")

    colors = ["red", "blue", "green", "pink", "black", "purple"]
    y_positions = [-100, -60, -20, 20, 60, 100]

    turtle_list = []
    print(screen.window_width())
    for index in range(0, 6):
        turtle = Turtle(shape="turtle")
        turtle.color(colors[index])
        turtle.penup()
        turtle.goto(x=-230, y=y_positions[index])
        turtle_list.append(turtle)


    def move_turtle(turtle, speed):
        """define turtle move function"""
        is_race_on = ""
        if user_bet:
            is_race_on = True
        while is_race_on:
            turtle.forward(speed)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if turtle.color() == user_bet:
                    print(f"You won!The {winning_color} turtle is the winner")
                else:
                    print(f"You lose!The {winning_color} turtle is the winner")


    # use multithreading to start turtles in the same time

    threads = []
    for t in turtle_list:
        speed = random.randint(1, 3)
        # 'target' is the function to run
        # 'args' is a tuple, including the parameters to pass in the target function
        thread = threading.Thread(target=move_turtle, args=(t, speed))
        threads.append(thread)
        thread.start()

    screen.exitonclick()