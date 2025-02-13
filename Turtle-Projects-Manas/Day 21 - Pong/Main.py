import time
from turtle import Turtle,Screen
from divider import  Divider
from player import Player
from pong import Pong

BOUNDARY=50
SCREENWIDTH=1200
SCREENHEIGHT=700

scr=Screen()
scr.bgcolor("black")
scr.setup(SCREENWIDTH,SCREENHEIGHT)
scr.tracer(0)
scr.listen()
divider=Divider()
divider.drawline(-330)

game_text=Turtle()
game_text.color("yellow")
game_text.hideturtle()
player1=Player("Manas","Right")
player2=Player("Happy","Left")
pong= Pong(player1.bar_position())
pong.begin_move(player1.is_right)
scr.update()

scr.onkey(player1.move_up,"Up")
scr.onkey(player1.move_down,"Down")
scr.onkey(player2.move_up,"w")
scr.onkey(player2.move_down,"s")

game_on=True
def check_collision_and_move():
    p_x = pong.xcor()
    p_y = pong.ycor()
    s_top = (SCREENHEIGHT/2) - BOUNDARY
    s_bottom = -1 * ((SCREENHEIGHT/2) - BOUNDARY)
    s_left= -1 * ((SCREENWIDTH/2) - BOUNDARY)
    s_right= (SCREENWIDTH/2) - BOUNDARY

    #collision with top and bottom
    if s_top-p_y < 5:
        pong.reflect_x(True)
    elif p_y - s_bottom < 5:
        pong.reflect_x(False)
    elif player1.hit_ball(pong):
        pong.reflect_y(True)
        player1.increase_score()
    elif player2.hit_ball(pong):
        pong.reflect_y(False)
        player2.increase_score()
    elif p_x > s_right or p_x <s_left:
            return False

    pong.move()
    return True

while game_on:
    scr.update()
    if not check_collision_and_move():
        game_on=False
        game_text.write("GAME OVER...",align="center", font=("Arial",64,"bold"))
    time.sleep(0.1)


scr.exitonclick()