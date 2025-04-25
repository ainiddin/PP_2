import pygame
import sys
from pygame.locals import *
import random
import time
import os

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 400
screen_height = 600

# Частота обновления экрана
fps = 60

# Начальная скорость врага
enemy_speed = 5

# Очки и монеты
score = 0
coins_total = 0

# Порог монет для увеличения скорости
coin_threshold = 5

# Скорость падения монет
coin_fall_speed = 3

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GOLD = (255, 215, 0)

# Шрифты
font_large = pygame.font.SysFont("Verdana", 45)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_large.render("YOU CRASHED!", True, BLACK)

# Окно игры
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Original Drive")

# Фон
background = pygame.Surface((screen_width, screen_height))
background.fill(WHITE)

# Таймер
clock = pygame.time.Clock()

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lab8-9", "images", "Enemy.png")), (50, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(25, screen_width - 40), random.randint(-100, 0))

    def move(self):
        global score
        self.rect.move_ip(0, enemy_speed)
        if self.rect.top > screen_height:
            score += 1
            self.rect.top = random.randint(-100, 0)
            self.rect.center = (random.randint(25, screen_width - 40), self.rect.top)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join("lab8-9", "images", "car.png")), (50, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < screen_width:
            self.rect.move_ip(5, 0)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = random.randint(10, 20)  # радиус задаёт размер и вес
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GOLD, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_width - 40), 0)
        self.points = 1 if self.radius <= 15 else 2  # малые монеты = 1 очко, большие = 2 очка

    def move(self):
        self.rect.move_ip(0, coin_fall_speed)
        if self.rect.top > screen_height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_width - 40), 0)

# Создаём объекты
player_car = Player()
enemy_car = Enemy()

# Группы монет и врагов
coins_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(enemy_car)

# Генерируем начальные 3 монеты
for _ in range(3):
    coins_group.add(Coin())

# Все спрайты
all_sprites = pygame.sprite.Group()
all_sprites.add(player_car, enemy_car, *coins_group)

# Событие для увеличения скорости врагов со временем
inc_speed=pygame.time.get_ticks()

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #увеличение скорости врага каждые 1000 милисекунды
    if pygame.time.get_ticks()-inc_speed>=1000:
            enemy_speed += 0.5
            inc_speed=pygame.time.get_ticks()

    # Отображение фона
    screen.blit(background, (0, 0))

    # Тексты очков и монет
    score_text = font_small.render(f"Score: {score}", True, BLACK)
    coins_text = font_small.render(f"Coins: {coins_total}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (screen_width - 110, 10))

    # Обновление и отрисовка всех объектов
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(player_car, enemies):
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for sprite in all_sprites:
            sprite.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Обработка сбора монет
    for coin in pygame.sprite.spritecollide(player_car, coins_group, True):
        coins_total += coin.points  # добавляем очки за монету
        new_coin = Coin()
        coins_group.add(new_coin)
        all_sprites.add(new_coin)

        # Увеличиваем скорость врагов, если собрано кратное N монет
        if coins_total % coin_threshold == 0:
            enemy_speed += 1

    pygame.display.update()
    clock.tick(fps)
