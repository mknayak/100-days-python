from turtle import Turtle
TOP_POSITION=375
class Divider(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.color("white")
        self.penup()
        self.setposition(0, TOP_POSITION)
        self.setheading(270)
        self.pensize(20)
        self.shape("square")

    def drawline(self,ycor):
        draw_centerline = True
        while draw_centerline:
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(30)

            if self.ycor() < ycor:
                draw_centerline = False