import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 500))
mouse = pygame.image.load("D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Mouse.jpg")
mouse = pygame.transform.scale(mouse, (780, 600))

def blitRotate(surf, image, pos, originPos, angle):

    # смещение от оси к центру
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # повернутое смещение от оси к центру
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # повернутый центр изображения
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # получить повернутое изображение
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(topleft = rotated_image_center)

    #вращать и блистать изображение
    surf.blit(rotated_image, rotated_image_rect)
  

lhand = pygame.image.load('D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Left.png')
rhand = pygame.image.load('D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\Lecture(26.03.2022)\Rigth.png')
wl, hl = lhand.get_size()
wr, hr = rhand.get_size()


rhand = pygame.transform.scale(rhand, (130, 90))
lhand = pygame.transform.scale(lhand, (160, 90))

angle = 0
done = False
while not done:
    time = datetime.now()
    minutes = time.minute
    seconds = time.second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    
    screen.fill((255, 255, 255))
    screen.blit(mouse, (-90, -50))
    blitRotate(screen, lhand, pos, (wl/2, hl/2), minutes * 6 + 45)
    blitRotate(screen, rhand, pos, (wr/2, hr/2), seconds * 6 + 45)
    #blitRotate2(screen, image, pos, angle)
    angle += 1

    pygame.display.flip()
    
pygame.quit()
exit()