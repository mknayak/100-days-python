from turtle import Turtle,Screen

toto=Turtle()
scr=Screen()
toto.shape("turtle")

def move_forward():
    toto.forward(10)

def move_backward():
    toto.backward(10)

def turn_right():
    toto.right(10)

def turn_left():
    toto.left(10)

def clear():
    toto.clear()
    toto.penup()
    toto.setposition((0,0))
    toto.pendown()


scr.listen()
scr.onkeypress(key="a",fun=move_backward)
scr.onkeypress(key="w",fun=turn_right)
scr.onkeypress(key="d",fun=move_forward)
scr.onkeypress(key="s",fun=turn_left)
scr.onkeypress(key="c",fun=clear)

scr.exitonclick()