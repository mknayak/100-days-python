from turtle import Turtle, Screen

import colorgram
import turtle as t
import random




def draw_fill_circle(radius,color):
    tut.pendown()
    tut.color(color)
    tut.fillcolor(color)
    tut.begin_fill()
    tut.circle(radius)
    tut.end_fill()
    tut.penup()


my_scr=Screen()
t.colormode(255)
colors= colorgram.extract("image.jpeg",10)
tut=Turtle()
tut.setposition((0,0))

#tut.color("white")
tut.speed("fastest")
tut.hideturtle()
circle_radius=10
width=200
height=200
i=(-1*int(width/2))
j=(-1*int(height/2))
tut.penup()
while i<width and j <height:
    tut.setposition((i, j))
    col=random.choice(colors)
    draw_fill_circle(circle_radius,col.rgb)
    i+= (circle_radius*3)
    print(f"i:{i}, j:{j}")
    if i>=width:
        i=(-1*int(width/2))
        j+= (circle_radius*3)






my_scr.exitonclick()