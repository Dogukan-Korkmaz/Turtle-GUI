# from turtle import *

import turtle as t
tim = t.Turtle()
scrn = t.Screen()

tim.shape("turtle")
# tim.color("darkblue")
tim.shapesize(2, 2, 5)
tim.speed(5)


def make_square():
    tim.forward(200)
    tim.rt(90)
    tim.forward(200)
    tim.rt(90)
    tim.forward(200)
    tim.rt(90)
    tim.forward(200)


def make_dashed_line():
    for _ in range(50):
        tim.forward(10)
        tim.pendown()
        tim.forward(10)
        tim.penup()

import random

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()

    tim.color(r, g, b)

def shape_maker():
    edge = 2
    for y in range(10):
        change_color()
        edge += 1
        outer_angle = 360 / edge
        for _ in range(edge):
            tim.right(outer_angle)
            tim.forward(100)


        # tim.pen(pencolor="white", pensize=1)
        # tim.forward(10)
        # tim.pen(pencolor="black", pensize=1)
        # tim.forward(10)
        # tim.pen(pencolor="white", pensize=1)

# make_dashed_line()
shape_maker()

scrn.exitonclick()
