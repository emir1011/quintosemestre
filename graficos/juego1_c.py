import pygame

pygame.init()
ventana = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("ejemplo 3")
ball = pygame.image.load("tennis_1f3be.png")
ballrect = ball.get_rect()
speed = [4, 4]
ballrect.move_ip(0, 0)
#crea el objeto bae y obtengo su rectangulo
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
#pongo el bate en la parte inferior de la pantalla
baterect.move_ip(240, 450)
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                jugando = False
    #compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3, 0)
    #compruebo si hay colision
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = baterect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
         speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_width():
        speed[1] = -speed[1]
    ventana.fill((252, 243, 207))
    ventana.blit(ball, ballrect)
    #dibujo el bate
    ventana.blit(ball, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()


