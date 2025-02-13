from turtle import Turtle
Y_POS=50
ALIGNMENT="Center"
FONT= ("Arial",24,"bold")
SCORE_FONT= ("Arial",72,"bold")
BAR_LENGTH=5
class Player(Turtle):
    play_bar:Turtle
    def __init__(self,name,position):
        super().__init__()
        self.name=name
        self.penup()
        self.score=0
        self.play_bar=Turtle()
        self.is_right= (position == "Right")
        if self.is_right:
            self.xpos=500
        else:
            self.xpos=-500
        self.color("white")
        self.goto(self.xpos,325)
        self.hideturtle()
        self.write(self.name, False, align=ALIGNMENT, font=FONT)
        self.initialize()
        self.speed(10)

    def initialize(self):
        self.play_bar.shape("square")
        self.play_bar.color("white")
        self.play_bar.shapesize(stretch_wid=1,stretch_len=5)
        self.play_bar.speed(10)
        self.play_bar.penup()
        self.play_bar.setposition(self.xpos,20)
        self.play_bar.setheading(90)
        self.show_score()

    def move_up(self):
        self.play_bar.setheading(90)
        self.play_bar.forward(20)

    def move_down(self):
        #self.play_bar.setheading(270)
        self.play_bar.backward(20)

    def bar_position(self):

        xcor=self.play_bar.xcor()
        ycor= self.play_bar.ycor()
        if self.is_right:
            xcor-=20
        else:
            xcor+=20
        return (xcor,ycor)

    def hit_ball(self,ball:Turtle):
        if ball.distance(self.play_bar) <20:
            return True
        return False

    def show_score(self):
        score_x=-75
        self.clear()
        if self.is_right:
            score_x=75
        score_y=270
        self.goto(score_x,score_y)
        self.write(f"{self.score:02d}", False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score+=1
        self.show_score()