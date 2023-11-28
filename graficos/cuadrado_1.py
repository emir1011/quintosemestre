import turtle

turtle.color('purple')
#turtle.fillcolor('purple')
turtle.shape('turtle')

#turtle.begin_fill()
turtle.forward (0)

turtle.color('black', 'green')
turtle.begin_fill()
grados = 0#la distancia entre cada cuadro
turtle.speed(15)   #metodo speed que permite definir la velocidad del lapiz
for x in range (1 , 38):
        for x in range (0 , 4): #numero de veces que se repetira el proceso para formar el cuadrado
            turtle.forward (100)  #movimiento de los pixeles hacia delante
            turtle.left(90) #el grado de giro para formar cuadrados
        turtle.left (grados + 10)
turtle.end_fill()
turtle.done()