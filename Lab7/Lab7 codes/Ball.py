import pygame
pygame.init()

size = weight , height = (500, 500)

screen = pygame.display.set_mode((size))
pygame.display.set_caption("Red Ball")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

x = 220
y = 200
speed = 25
do = False

clock = pygame.time.Clock()

while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if y <= 0:
                y = y
            else:
                y += (-1 * speed)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if y >= height - 60:
                y = y
            else:
                y += speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dy = 0
            dx = -1 * speed
            if x <= 0:
                x = x
            else:
                x += (-1 * speed)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if x >= weight - 50:
                x = x
            else:
                x += speed
                
    screen.fill(WHITE)
        
    pygame.draw.ellipse(screen, RED, (x, y, 50, 50))
    clock.tick(20)
    pygame.display.flip()
    
    
pygame.quit()