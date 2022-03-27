"""
draw(){
    draw.line(screen, color, [begin], [end], fatness)
    draw.rect(screen, color, (x, y, wight, height), fatness)
    draw.ellipse(screen, color, (x, y, wight, height), fatness)
    draw.arc()
}
"""
import pygame
pygame.init()

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PI = 3.14

size = (400, 400)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("My example")

do = False
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, [0,0], [100, 100], 2)
    for y in range(0,200, 10):
        pygame.draw.line(screen, BLUE, [0, 10+y], [100, 110 + y], 1)
        
    pygame.draw.rect(screen, RED, (120, 20, 200, 100), 2)
    pygame.draw.ellipse(screen, GREEN, (120, 130, 200, 100), 2)
    
    pygame.draw.arc(screen, BLACK, (120, 240, 200, 100), 0, PI / 2, 50)
    pygame.draw.arc(screen, RED, (120, 240, 200, 100), PI/2, PI, 50)
    pygame.draw.arc(screen, GREEN, (120, 240, 200, 100), PI,  3 * PI / 2, 50)
    pygame.draw.arc(screen, BLUE, (120, 240, 200, 100), 3 * PI / 2, 2 * PI, 50)

    pygame.display.flip()

pygame.quit()            