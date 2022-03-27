import pygame
pygame.init()

size = weight, height = ((300, 250))

screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
#clock = pygame.time.Clock()

do = False
BLACK = ((0, 0, 255)) #  RED
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
     
    font = pygame.font.Font(None, 25)
    text = font.render("BLUE DIAMOND", True, ((0,0,0)))
    screen.blit(text, (79, 10))
        
            
    pygame.draw.line(screen, BLACK, (50, 80), (250, 80), 3)
    pygame.draw.line(screen, BLACK, (150, 30), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (50, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (250, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (100, 30), (200, 30), 3)
    pygame.draw.line(screen, BLACK, (50, 80), (100, 30), 3)
    pygame.draw.line(screen, BLACK, (200, 30), (250, 80), 3)
    pygame.draw.line(screen, BLACK, (83, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (116, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (182, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (215, 80), (150, 200), 3)
    pygame.draw.line(screen, BLACK, (100, 30), (83, 80), 3)
    pygame.draw.line(screen, BLACK, (100, 30), (116, 80), 3)
    pygame.draw.line(screen, BLACK, (150, 30), (116, 80), 3)
    pygame.draw.line(screen, BLACK, (150, 30), (182, 80), 3)
    pygame.draw.line(screen, BLACK, (200, 30), (182, 80), 3)
    pygame.draw.line(screen, BLACK, (200, 30), (215, 80), 3)
    
    pygame.display.flip()
    
pygame.quit()