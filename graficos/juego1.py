import pygame
#inicializacion de pygame
pygame.init()
#inicializacion de la superficie de dibujo
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 1")
#Bucle principal del juego
jugando = True
while jugando:
    #compromabos los eventos
    #comprobamos si se ha pulsado el boton de cierra de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    #se punta la ventana con un color
    # Esto borra los posibles elementos que teniams anteriormente
    ventana.fill((252, 243, 207))
    # todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    #controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)
pygame.quit()
