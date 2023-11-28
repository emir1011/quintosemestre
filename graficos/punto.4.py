from turtle import *
from random import randint

setup(450, 200, 0, 0)
screensize(300, 150)
title("PROGRAMACION VISUAL")
hideturtle()
penup()

def punto():
    global randint
    goto(randint(-225, 225), randint(-100,100))
    dot(10,"black")
    ontimer(punto,1000)

ontimer(punto,1000)
exitonclick()
