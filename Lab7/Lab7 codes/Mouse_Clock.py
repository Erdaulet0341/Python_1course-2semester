import pygame, datetime
pygame.init()

clock = pygame.image.load("D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Mouse.jpg")
clock = pygame.transform.scale(clock, (780, 600))
right = pygame.image.load("D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Rigth.png")
left = pygame.image.load("D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Left.png")


right = pygame.transform.scale(right, (130, 90))
left = pygame.transform.scale(left, (160, 90))

angle = 0.5
weigth , heigth = (600, 500)
screen = pygame.display.set_mode((weigth, heigth))

FPS = pygame.time.Clock()
do = False
while not do:
    angle += 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
            
    rot_right = pygame.transform.rotate(right, angle)
    screen.blit(clock, (-90,-50))
    screen.blit(right, (290,170))
    screen.blit(left, (185,180))
    FPS.tick(10)
    pygame.display.update()
    
pygame.quit()