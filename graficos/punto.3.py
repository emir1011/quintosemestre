from turtle import *

setup(450, 200, 0, 0)
screensize(300, 150)
title("PROGRAMACION VISUAL")
hideturtle()
penup()

def punto(x,y):
    goto(x, y)
    dot(10, "black")

def cuadro(x, y):
    goto(x - 5, y - 5)
    pendown()
    goto(x + 5, y- 5)
    goto(x + 5, y + 5)
    goto(x - 5, y + 5)
    goto(x - 5, y - 5)
    penup()

onscreenclick(punto)
onscreenclick(cuadro, 3)
onscreenclick(punto, 2)
onscreenclick(cuadro, 2,True)
mainloop()
