import pygame 
import random
pygame.init()

l = [
    r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Музыка\Ирина Кайратовна, Shiza - Kõk tu.mp3",
    r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Музыка\Мирас Жугунусов & 2RAR - Ойлай берем_muztok.com.mp3",
    r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Музыка\auka-dastan-orazbekov-belgsz-zhan_(muzzonas.ru).mp3",
    r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Музыка\miyagi-skriptonit-feat-104-ne-zhal.mp3"]

colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255), (200, 0, 100), (70, 70, 70), (0, 0, 0)]
im = pygame.image.load(r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\imgonline-com-ua-Resize-LPTlfW8k2XLMBz.jpg")
fm = pygame.image.load(r"D:\Educational materials\Programming principles 2\Python\PP2_21B030956\Lab7\flag.jpg")
screen = pygame.display.set_mode((330, 450))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

do = False
val = 0.1
print(l[0])
pos = 0
pygame.mixer.music.load(l[pos])
pygame.mixer.music.play()
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if pos <= 2:
                pos+=1
            else:
                pos = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if pos >= 1:
                pos-=1
            else:
                pos = 3
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            val+=0.1
            pygame.mixer.music.set_volume(val)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            val-=0.1
            pygame.mixer.music.set_volume(val)
  
    screen.blit(im, (0, 0))
    screen.blit(fm, (0, 0))
    
    pygame.display.flip()
pygame.quit()