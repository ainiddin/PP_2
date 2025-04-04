import pygame
import os
pygame.init()
size=((800,800))
screen=pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")

bg=pygame.transform.scale(pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\music-elements\background.png"),(size))
pl = pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\music-elements\play.png")
p = pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\music-elements\pause.png")
n = pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\music-elements\next.png")
b = pygame.image.load(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\music-elements\back.png")
pls=pygame.transform.scale(pl,(50,50))
ps=pygame.transform.scale(pl,(50,50))
ns=pygame.transform.scale(pl,(50,50))
bs=pygame.transform.scale(pl,(50,50))
paths=[]
mf=r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\musics"
mflist=os.listdir(mf)

for i in mflist:
    if i.endswith(".mp3"):
        paths.append(os.path.join(mf,i))

bg1=pygame.Surface((800,200))
bg1.fill("white")

f=pygame.font.SysFont(None,40)

index=0
pygame.mixer.music.load(paths[index])
pygame.mixer.music.play(1)
a=True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(paths)
                pygame.mixer.music.load(paths[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(paths)
                pygame.mixer.music.load(paths[index])
                pygame.mixer.music.play()
    name=f.render(os.path.basename(paths[index]),True,"blue")
    screen.blit(bg,(0,0))
    screen.blit(bg1,(0,600))
    screen.blit(name,(290,620))
    if a:
        screen.blit(pls,(375,680))
    else:
        screen.blit(ps,(375,680))
    screen.blit(ns,(480,680))
    screen.blit(bs,(270,680))
    
    pygame.display.flip()
    pygame.time.Clock().tick(10)
    