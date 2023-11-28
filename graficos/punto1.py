from turtle import *
setup(450, 200, 0, 0)
screensize(300, 150)
title("PROGRAMA VISUAL")
hideturtle()
penup()

def punto(x, y):
    goto(x, y)
    dot(10, "black")

onscreenclick(punto)
mainloop()