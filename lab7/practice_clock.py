import pygame
import datetime
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Mickey clock")

bodyclock=pygame.transform.scale(pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\images\clock.png"),(800,600))
secarm=pygame.transform.scale(pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\images\leftarm.png"),(40.95, 682.5))
minarm=pygame.transform.scale(pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\images\rightarm.png"),(800,600))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    min=datetime.datetime.now().minute
    sec=datetime.datetime.now().second
    min_ang=min*6 + (sec/60)*6
    sec_ang=sec*6

    screen.blit(bodyclock, (0, 0))

    r_secarm=pygame.transform.rotate(secarm,-sec_ang)
    rsecrec=r_secarm.get_rect(center=(400, 312))
    screen.blit(r_secarm,rsecrec)

    r_minarm=pygame.transform.rotate(minarm,-min_ang)
    rminrec=r_minarm.get_rect(center=(400, 310))
    screen.blit(r_minarm,rminrec)

    pygame.display.flip()
