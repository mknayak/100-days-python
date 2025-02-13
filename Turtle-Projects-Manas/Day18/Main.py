import turtle
from random import random
from turtle import Turtle, Screen
import random
toto = Turtle()

#for _ in range(1,5):
 #   toto.forward(100)
  #  toto.left(90)

# for _ in range(1,10):
#     toto.forward(10)
#     toto.penup()
#     toto.forward(10)
#     toto.pendown()
colors=["cornflower blue","teal","lime","yellow","sienna","maroon","orange","pink","purple","dark violet"]
def draw_shape(no_of_sides,color):
    toto.color(color)
    angle= 360/no_of_sides
    for _ in range(no_of_sides):
        toto.forward(100)
        toto.left(angle)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    r_color= (r,g,b)
    #tuple (item list). e.g. (2,54,6) . Tuples are immutable
    return r_color

# for poly in range(3,11):
#     color=random.choice(colors)
#     draw_shape(poly,color)
turtle.colormode(255)

toto.pensize(10)
toto.speed("fastest")
while True:
    #toto.color(random.choice(colors))
    my_color= random_color()
    toto.color(my_color)
    toto.forward(20)
 #   toto.right(random.choice([0,90,180,270]))
    toto.setheading(random.choice([0,90,180,270]))




















screen= Screen()
screen.exitonclick()