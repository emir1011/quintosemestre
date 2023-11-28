import math
import turtle
import colorsys as sc
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(15)
turtle.fillcolor("yellow")
phi=137.508*(math.pi/180.0)
for i in range(260+140):
        r=4*math.sqrt(i)
        theta=i*phi
        x=r*math.cos(theta)
        y=r*math.sin(theta)
        turtle.penup()
        turtle.goto(x,y)
        turtle.setheading(i*137.508)
        turtle.pendown()

        if i<260:
            turtle.stamp()
        else:

            turtle.fillcolor("white")


            turtle.begin_fill()
            turtle.right(90)
            turtle.circle(200 - 1 * 2, 90)

            # turtle.circle(200-j*4, extent: 90)
            turtle.left(90)
            turtle.circle(200 - 1 * 2, 90)
            # turtle.circle(200-j*4, extent: 90)
            turtle.right(180)
            turtle.circle(52, 24)
            turtle.end_fill()

turtle.hideturtle()
turtle.done()
