
import pygame
pygame.init()

size = (600, 400)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("My example")

clock = pygame.time.Clock()
sp = None
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    press = pygame.mouse.get_pressed()
    if press[0]:
        pos = pygame.mouse.get_pos()
        
        if sp is None:
            sp = pos
        
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, ((255, 0, 0)), (sp[0], sp[1], height, width))
        pygame.display.flip()
    clock.tick(60)
    

pygame.quit()            