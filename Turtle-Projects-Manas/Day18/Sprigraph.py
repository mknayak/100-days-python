
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    r_color= (r,g,b)
    #tuple (item list). e.g. (2,54,6) . Tuples are immutable
    return r_color

tut=Turtle()
tut.speed("fastest")
tilt_angle=0
while tilt_angle<360:
    tut.color(random_color())
    tut.circle(100)
    current_heading=tut.heading()
    tut.setheading(current_heading+5)
    #tut.left(2)
    tilt_angle+=5







my_scr= Screen()
my_scr.exitonclick()