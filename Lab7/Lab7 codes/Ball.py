import pygame
pygame.init()

size = weight , height = (700, 600)

screen = pygame.display.set_mode((size))
pygame.display.set_caption("Red Ball")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x = 100
y = 100
dx = 3
dy = 0
speed = 3
do = False

clock = pygame.time.Clock()

while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dx = 0
            dy = -1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dx = 0
            dy = 1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dy = 0
            dx = -1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dy = 0
            dx = 1 * speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if speed >= 40:
                pass
            else:
                speed += 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            if speed == 0:
                pass
            else:
                speed -= 3
                
    screen.fill(WHITE)
    x += dx
    y += dy
    
    if weight < x:
        x = -20
    if -20 > x:
        x = weight
    if height < y:
        y = -20
    if -20 > y:
        y = height
        
    pygame.draw.ellipse(screen, RED, (x, y, 50, 50))
    clock.tick(20)
    pygame.display.flip()
    
    
pygame.quit()