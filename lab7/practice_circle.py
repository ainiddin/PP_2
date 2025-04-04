import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("movable ball")
b_p=[500,400]
r=40
s=25
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            pygame.quit()
            exit()

    key=pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        b_p[1]=max(40,b_p[1]-s)
    elif key[pygame.K_s] or key[pygame.K_DOWN]:
        b_p[1]=min(760,b_p[1]+s)
    elif key[pygame.K_a] or key[pygame.K_LEFT]:
        b_p[0]=max(40,b_p[0]-s)
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        b_p[0]=min(960,b_p[0]+s)
    screen.fill("white")  # Заливка экрана белым
    pygame.draw.circle(screen,"red",b_p,r)
    pygame.display.flip()
    pygame.time.Clock().tick(40)