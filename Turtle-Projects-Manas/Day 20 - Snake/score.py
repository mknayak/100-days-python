from turtle import Turtle
ALIGNMENT="Center"
FONT= ("Arial",16,"normal")
STARTFONT= ("Arial",32,"normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("history.txt","r") as file:
            self.highscore= int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()

    def start_score(self):
        self.goto(0, 0)
        self.write("Press Enter to start the game.", False, align=ALIGNMENT, font=STARTFONT)
        self.sety(270)

    def show_score(self):
        self.clear()
        if self.highscore< self.score:
            self.highscore=self.score
        self.write(f"Your Score : {self.score}, High Score:{self.highscore}",False,align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.\nPress Enter to start new game.",False,align=ALIGNMENT,font=FONT)
        with open("history.txt","w") as file:
            file.write(str(self.highscore))
        self.sety(270)
        self.score=0
