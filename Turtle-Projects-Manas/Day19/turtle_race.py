from turtle import Turtle,Screen
import random

toto=Turtle()
scr=Screen()
scr.setup(500,400)

def initialize_game(turtles:[]):
    x=-200
    y=-100
    for t in turtles:
        y= y+30
        t_ins=t["obj"]
        t_ins.penup()
        t_ins.goto(x,y)
        t_ins.pendown()


user_input = scr.textinput("Make your bet", "which turtle will win the race? Enter a color")


t_colors=["violet","indigo","blue","green","yellow","orange","red"]
turtle_list= []

for tot in t_colors:
    t_instance=Turtle("turtle")
    t_instance.color(tot)
    turtle_list.append({"key":tot,"obj":t_instance})

initialize_game(turtle_list)
is_race_on=False
if user_input:
    is_race_on=True
winner=""
while is_race_on:

    for t_obj in turtle_list:
        if is_race_on:
            tur=t_obj["obj"]
            dist=random.randint(2,10)
            tur.penup()
            tur.forward(dist)
            if tur.xcor() >= 220:
                winner = tur.pencolor()
                is_race_on = False
                if user_input==winner:
                    print("You win !!")
                else:
                    print(f"You Loose :(. Winning Turtle: {winner}")










scr.exitonclick()