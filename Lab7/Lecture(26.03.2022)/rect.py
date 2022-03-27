import pygame
pygame.init()

size = weight, height = (400, 400)

screen = pygame.display.set_mode(size)

screen.fill((255, 0, 0)) #red

pygame.draw.rect(screen, (0, 100, 10), (150, 150, 100, 100), 5)

do = False

while not do:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            do = True
    pygame.display.flip()
    
pygame.quit()