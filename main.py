import colorgram
import turtle
import random


def paint_line(start, x_dots, x_dist):
    for i in range(x_dots):
        random_colour = random.choice(colours)
        onyx.pencolor(random_colour.rgb)
        onyx.dot()
        onyx.forward(x_dist)
    onyx.setx(start)


def move_line(y_dist):
    onyx.left(90)
    onyx.forward(y_dist)
    onyx.right(90)


def paint_dots(start, x_dots, x_dist, y_dots, y_dist):
    for i in range(y_dots):
        paint_line(start, x_dots, x_dist)
        move_line(y_dist)


screen = turtle.Screen()
screen.screensize(900, 900)
screen.colormode(255)
colours = colorgram.extract('colour_palette.jpg', 32)
onyx = turtle.Turtle()
onyx.hideturtle()
dots_horizontal = 16
spacing_horizontal = 50
dots_vertical = 16
spacing_vertical = 50
onyx.speed(0)
onyx.penup()
onyx.pensize(20)
onyx.setposition((((dots_horizontal-1)*spacing_horizontal)/2)*-1, (((dots_vertical-1)*spacing_vertical)/2)*-1)
x_start = onyx.xcor()
y_start = onyx.ycor()
paint_dots(x_start, dots_horizontal, spacing_horizontal, dots_vertical, spacing_vertical)
onyx.setposition(x_start, y_start)

screen.exitonclick()
