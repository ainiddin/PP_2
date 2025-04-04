import pygame
import os

pygame.init()

playlist = []
music_folder = r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab7\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("песня-1")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join( "music-elements", "background.png"))
background = pygame.transform.scale(background, (800, 800))

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 30)

playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))


index = 0
aplay = False

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
aplay = True

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))

    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(bg, (155, 550))
    screen.blit(text2, (365, 570))

    playb_scaled = pygame.transform.scale(playb, (70, 70))
    pausb_scaled = pygame.transform.scale(pausb, (70, 70))
    nextb_scaled = pygame.transform.scale(nextb, (70, 70))
    prevb_scaled = pygame.transform.scale(prevb, (75, 75))

    if aplay:
        screen.blit(pausb_scaled, (370, 650))
    else:
        screen.blit(playb_scaled, (370, 650))

    screen.blit(nextb_scaled, (460, 647))
    screen.blit(prevb_scaled, (273, 645))

    clock.tick(24)
    pygame.display.update()
