from turtle import Turtle
import random
class Pong(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(2)
        self.setposition(position)

    def move(self):
        self.forward(10)

    def begin_move(self,is_right):
        random_angele = random.randint(15,45)
        if is_right:
            random_angele+=90
        self.setheading(random_angele)

    def reflect_x(self,is_top):
        heading=self.heading()
        if is_top:
            self.setheading(180+(180-heading))
        else:
            self.setheading(180-(heading-180))

    def reflect_y(self,is_right):
        heading=self.heading()
        if is_right:
            self.setheading(180+(360-heading))
        else:
            self.setheading(360-(heading-180))
        self.forward(15)