import turtle
import prettytable




tur1 = turtle.Turtle()
print(tur1)
tur1.shape('turtle')
tur1.color('green')
tur1.forward(100)
tur1.left(120)
tur1.forward(100)
tur1.left(120)
tur1.forward(100)


for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tur1.color(c)
        tur1.forward(steps)
        tur1.right(30)
my_scr= turtle.Screen()
print(my_scr.canvwidth)
my_scr.exitonclick()