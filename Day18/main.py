from turtle import Turtle, Screen
import random
turtle = Turtle()

turtle.shape("turtle")
turtle.color("DarkOrchid1")


def draw_square():
    """draw a square"""
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

# draw_square()


def draw_dash():
    """draw a dash line"""
    i = 0
    while i < 25:
        for c in ('black', 'white'):
            turtle.color(c)
            turtle.forward(10)
            i += 1


# draw_dash()

def draw_different_shapes():
    """draw different type of shapes, and each shape is outside the last shape"""
    for angle in range(3,10):
        inside_angle = (180 * (angle - 2)) / angle
        turn_angle = 180 - inside_angle

        c1,c2,c3 = random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)
        tup = (c1, c2, c3)
        turtle.pencolor(tup)

        i = 1
        while i <= angle:
            turtle.right(turn_angle)
            turtle.forward(100)
            i += 1


# draw_different_shapes()

def random_walk():
    """walk random direction for same steps but change color each steps"""
    direction = [0, 90, 180, 270]

    for i in range(100):
        dir_choose = int(random.choice(direction))
        turtle.right(dir_choose)
        turtle.forward(20)
        c1, c2, c3 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        tup = (c1, c2, c3)
        turtle.pencolor(tup)


random_walk()


screen = Screen()
screen.exitonclick()
