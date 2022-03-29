import pygame 
import random
pygame.init()

l = [
    r"D:\Music\Ирина Кайратовна, Shiza - Kõk tu.mp3",
    r"D:\Music\Мирас Жугунусов & 2RAR - Ойлай берем_muztok.com.mp3",
    r"D:\Music\auka-dastan-orazbekov-belgsz-zhan_(muzzonas.ru).mp3",
    r"D:\Music\miyagi-skriptonit-feat-104-ne-zhal.mp3",
    r"D:\Music\ali-otenov-sonda-da-zhasy-krem_(muzzonas.ru).mp3",
    r"D:\Music\diar-aktrisa-yz_(muzzonas.ru).mp3",
    r"D:\Music\kamazz_-_kak_ty_tam_muzati.net.mp3",
    r"D:\Music\Melisa, Tommo - I'm Alone.mp3",
    r"D:\Music\QARAKESEK - Көбелек (solo).mp3"
    ]

colors = [(255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255), (200, 0, 100), (70, 70, 70), (0, 0, 255)]
im = pygame.image.load(r"C:\Users\007\msplayer.jpg")
fm = pygame.image.load(r"C:\Users\007\flag.jpg")
screen = pygame.display.set_mode((330, 450))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

do = False
val = 0.05
print(l[0])
pos = 0
pygame.mixer.music.load(l[pos])
pygame.mixer.music.play()
pygame.mixer.music.queue(l[random.randrange(0, 8)])
while not do:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RCTRL:
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if pos <= 7:
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
                pos = 8
            pygame.mixer.music.stop()
            pygame.mixer.music.load(l[pos])
            pygame.mixer.music.play()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            val+=0.05
            pygame.mixer.music.set_volume(val)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            val-=0.05
            pygame.mixer.music.set_volume(val)
  
    screen.blit(im, (0, 0))
    screen.blit(fm, (0, 0))
    pygame.draw.ellipse(screen, colors[random.randrange(0, 7)], (71, 273, 112, 112))
    pygame.draw.ellipse(screen, ((255, 255, 255)), (104, 305, 45, 45))
    clock.tick(10)
    
    pygame.display.flip()
pygame.quit()