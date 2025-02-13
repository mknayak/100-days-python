from turtle import  Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()

    def initialize(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.speed("fastest")
        self.color("orange")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)