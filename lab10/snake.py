import pygame
import sys
import random as r
import psycopg2

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname="snake",
    user="postgres",
    password="ainiddin31",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Создание таблицы, если она не существует
cur.execute('''
    CREATE TABLE IF NOT EXISTS snake_scores (
        id SERIAL PRIMARY KEY,
        player_name TEXT UNIQUE,
        score INT,
        length INT,
        level INT DEFAULT 1
    )
''')
conn.commit()

# Определение стен для уровней
walls = {
    2: [[240, 240], [260, 240], [280, 240], [300, 240], [320, 240], [340, 240]],
    3: [[240, 240], [260, 240], [280, 240], [300, 240], [300, 260], [300, 280], [300, 300], [280, 300]]
}

# Ввод имени игрока
player_name = ""
while not player_name:
    player_name = input("Введите имя игрока: ").strip()

# Инициализация игры
pygame.init()
width, height = 600, 600
cell_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Жылан ойын")

bg_clr = pygame.Color("white")
snake_color = pygame.Color("green")

snake_pos = [160, 200]
snake_body = [[140, 200], [120, 200], [100, 200]]
direction = "RIGHT"
change_to = direction



food_pos = [r.randint(0, (width // cell_size) - 1) * cell_size,
            r.randint(0, (height // cell_size) - 1) * cell_size]
food_spawn = True
food_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
food_weight = 1
score = 0
lvl = 1
lvlup = 6
clock_speed = 8
running = True
pause=False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_p:
                pause=True
                final_length=len(snake_body)
                cur.execute("""
                    INSERT INTO snake_scores (player_name, score, length, level)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (player_name)
                    DO UPDATE SET 
                        score = GREATEST(snake_scores.score, EXCLUDED.score),
                        length = GREATEST(snake_scores.length, EXCLUDED.length),
                        level = GREATEST(snake_scores.level, EXCLUDED.level);
                """, (player_name, score, final_length, lvl))

                conn.commit()
        if pause and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pause=False
    if pause:
        pause_font = pygame.font.SysFont(None, 40)
        pause_text = pause_font.render("ПАУЗА – Игра сохранена", True, pygame.Color("blue"))
        screen.blit(pause_text, (width // 2 - 140, height // 2 - 20))
        pygame.display.flip()
        continue
    direction = change_to

    if direction == "UP":
        snake_pos[1] -= cell_size
    elif direction == "DOWN":
        snake_pos[1] += cell_size
    elif direction == "LEFT":
        snake_pos[0] -= cell_size
    elif direction == "RIGHT":
        snake_pos[0] += cell_size

    # Проверка на выход за границы
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
        score += food_weight
        for i in range(food_weight):
            snake_body.insert(0, list(snake_pos))
    else:
        snake_body.pop()
        for body in snake_body[1:]:
            if body == snake_body[0]:
                running=False
                pygame.quit()
                exit()

    # Проверка на столкновение со стеной
    for wall in walls.get(lvl, []):
        if snake_pos[0] == wall[0] and snake_pos[1] == wall[1]:
            running = False

    # Переход на следующий уровень
    if score >= lvl * lvlup:
        lvl += 1
        clock_speed = 8 + 2 * (lvl - 1)

    # Спавн новой еды
    if not food_spawn or pygame.time.get_ticks() - food_time>=5000:#возвращает количество миллисекунд, прошедших с начала работы игры и минусуем появления время еды
        food_pos = [r.randint(1, 24) * cell_size, r.randint(1, 24) * cell_size]
        while food_pos in snake_body or food_pos in walls.get(lvl,[]):  # Проверяем, не находит ли еда в теле змеи
            food_pos = [r.randint(0, 24) * cell_size, r.randint(0, 24) * cell_size]
        food_weight = r.randint(1, 3)#рандомно даем вес еде
        food_time=pygame.time.get_ticks()#обновляем время еды
    food_spawn = True

    # Отрисовка
    screen.fill(bg_clr)

    # Отрисовка змейки
    for block in snake_body:
        pygame.draw.rect(screen, snake_color, pygame.Rect(block[0], block[1], cell_size, cell_size))

    # Отрисовка стен
    for wall in walls.get(lvl, []):
        pygame.draw.rect(screen, "black", pygame.Rect(wall[0], wall[1], cell_size, cell_size))

    # Отрисовка еды
    pygame.draw.rect(screen, "red", pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
    font = pygame.font.SysFont(None, 28)
    weight_text = font.render(str(food_weight), True, pygame.Color("blue"))
    screen.blit(weight_text, (food_pos[0] + 5, food_pos[1] + 1))

    pygame.display.flip()
    clock.tick(clock_speed)

# Конец игры
final_length = len(snake_body)

# Сохраняем результат в базу данных
cur.execute("""
    INSERT INTO snake_scores (player_name, score, length, level)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (player_name)
    DO UPDATE SET 
        score = GREATEST(snake_scores.score, EXCLUDED.score),
        length = GREATEST(snake_scores.length, EXCLUDED.length),
        level = GREATEST(snake_scores.level, EXCLUDED.level);
""", (player_name, score, final_length, lvl))

conn.commit()
cur.close()
conn.close()

pygame.quit()
print(f"Игра окончена. Очки: {score}, Длина: {final_length}, Уровень: {lvl}")
sys.exit()
