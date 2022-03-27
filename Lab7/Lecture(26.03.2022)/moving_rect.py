import re
import pygame
import random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

size = (800, 600)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Moving rectangle")
clock = pygame.time.Clock()
colors = [WHITE, GREEN, BLUE, RED]

rect_x = 50
rect_y = 50
rect_x_change = 20
rect_y_change = 20

color = WHITE
do = False

while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = colors[random.randint(0,3)]
    rect_y += rect_y_change
    rect_x += rect_x_change
    
    if rect_x > 700 or rect_x < 0:
        rect_x_change = rect_x_change * -1
    if rect_y > 500 or rect_y < 0:
        rect_y_change = rect_y_change * -1
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, color, (rect_x, rect_y, 100, 100))
    pygame.draw.rect(screen, (100, 100, 250), (rect_x + 25, rect_y + 25, 50, 50))
    clock.tick(30)
    pygame.display.update()
    
pygame.quit()            