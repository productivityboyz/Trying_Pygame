# Following this video https://www.youtube.com/watch?v=i6xMBig-pP4

import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("First_Game")

x = 50
y = 50
width = 10
height = 10
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = FALSE

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y -= vel

    win.fil((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()