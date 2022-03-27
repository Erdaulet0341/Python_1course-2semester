import pygame
pygame.init()

size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Texts")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

do = False

while not do:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        
    #Text create
    font = pygame.font.Font(None, 50)
    text1 = font.render("My text", True, RED)
    text2 = font.render("My text", False, RED)
    screen.blit(text1, (0,0))
    screen.blit(text2, (0, 40))
    
    #Text rorate
    font2 = pygame.font.SysFont("Calibri", 25, True, False)
    text3 = font.render("Almaty", True, GREEN)
    text3 = pygame.transform.rotate(text3, 50)
    screen.blit(text3, (100, 80))
    pygame.display.flip()
    
pygame.quit()