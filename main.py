# from turtle import *

import turtle as t
tim = t.Turtle()
scrn = t.Screen()

tim.shape("classic")
# tim.color("darkblue")
tim.shapesize(1, 1, 3)
tim.speed("fastest")
tim.pensize(3)


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


def make_circle():
    angle = 10
    for x in range(220):
        change_color()
        tim.left(angle)
        tim.circle(110)
        angle +=10

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


# make_circle()
# draw_spirograph(3)
# tim.forward(100)
# make_dashed_line()
# shape_maker()
# random_walk()

scrn.exitonclick()
