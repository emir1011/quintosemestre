import pygame
from random import randint
pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ejemplo 4")
ball = pygame.image.load("tennis_1f3be.png")
ballrect = ball.get_rect()
# la velocidad se calcula con un valor pseudialeatorio entre 3,6
speed = [randint(3,6), randint(3,6)]
ballrect.move_ip(0,0)
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect.move_ip(240, 450)
# esta es la fuente q usaremos para texto que aparecera en pantalla (tamaño 36)
fuente = pygame.font.Font(None, 36)
# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            baterect = baterect.move(-3,0)
        if keys[pygame.K_RIGHT]:
            baterect = baterect.move(3,0)
        if baterect.colliderect(ballrect):
            speed[1] = -speed[1]
        if ballrect.left < 0 or ballrect.right > ventana.get_width():
            speed[0] = -speed[0]

        if ballrect.top < 0:
            speed[1] = -speed[1]
        # si la pelota toca el borde inferior, has perdido ("Game over")
        if ballrect.bottom > ventana.get_height():
            texto = fuente.render("game over", True, (125 ,125, 125))
            texto_rect = texto.get_rect()
            texto_x = ventana.get_width() / 2 - texto_rect.width / 2
            texto_y = ventana.get_height() / 2 - texto_rect.height / 2
            ventana.blit(texto, [texto_x, texto_y])
        else:
            ventana.fill((252, 243, 207))
            ventana.blit(ball, ballrect)
            #dibuja el bate
            ventana.blit(bate, baterect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()