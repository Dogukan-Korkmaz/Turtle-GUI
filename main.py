from turtle import Turtle, Screen

def make_square():
    timmy_the_turtle.forward(200)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.forward(200)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.forward(200)
    timmy_the_turtle.rt(90)
    timmy_the_turtle.forward(200)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkblue")
timmy_the_turtle.shapesize(2, 2, 5)
timmy_the_turtle.speed(4)
make_square()









screen = Screen()
screen.exitonclick()