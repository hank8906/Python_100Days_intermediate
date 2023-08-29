from turtle import Turtle, Screen
import random
import colorgram
import re
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
        turtle.pensize(15)
        dir_choose = int(random.choice(direction))
        turtle.right(dir_choose)
        turtle.forward(20)
        c1, c2, c3 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        tup = (c1, c2, c3)
        turtle.pencolor(tup)


# random_walk()

def draw_circle():
    """draw loop circles that spin 360 degree"""
    for time in range(36):
        c1, c2, c3 = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
        tup = (c1, c2, c3)
        turtle.pencolor(tup)
        turtle.circle(50)
        turtle.right(10)


# draw_circle()


def hirs_spot():
    """draw the dot in random color, which extract from hirs spot painting"""
    colors = colorgram.extract('image.jpg', 35)

    rgb_colors = []
    for color in range(len(colors)):
        rgb_colors.append(colors[color].rgb)

    formatted_rgb = []
    for rgb in rgb_colors:
        rgb_value = f"({rgb.r},{rgb.g},{rgb.b})"
        # 將字串中的數字切割並轉換成整數，然後用 tuple 函數來創建元組
        rgb_color_tuple = tuple(map(int, rgb_value[1:-1].split(',')))
        formatted_rgb.append(rgb_color_tuple)

    turtle.penup()
    turtle.speed("fastest")
    turtle.setheading(225)
    turtle.forward(350)
    turtle.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        # 將 numeric color tuple 轉換成 Turtle 模組接受的顏色字串格式
        turtle.dot(20, "#%02x%02x%02x" % random.choice(formatted_rgb))
        turtle.fd(50)

        if dot_count % 10 == 0:
            turtle.setheading(90)
            turtle.fd(50)
            turtle.setheading(180)
            turtle.fd(500)
            turtle.setheading(0)


# hirs_spot()

screen = Screen()
screen.exitonclick()
