# from turtle import *

import turtle as t
tim = t.Turtle()
scrn = t.Screen()

tim.shape("turtle")
# tim.color("darkblue")
tim.shapesize(1, 1, 5)
tim.speed(8)
tim.pensize(5)


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


def random_walk():
    angle = [0, 90, 180, 270]
    for _ in range(200):
        change_color()
        direction = random.randint(1,100)
        angle_ = random.choice(angle)
        if 1 <= direction < 25:
            tim.left(angle_)
            tim.forward(20)
        elif 25 <= direction < 50:
            tim.right(angle_)
            tim.forward(20)
        elif 25 <= direction < 75:
            tim.left(angle_)
            tim.forward(20)
        elif 75 <= direction <= 100:
            tim.right(angle_)
            tim.forward(20)



# make_dashed_line()
# shape_maker()
random_walk()

scrn.exitonclick()
scrn.mode("lock")