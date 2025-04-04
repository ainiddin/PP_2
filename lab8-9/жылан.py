import pygame
import random as r

pygame.init()

screen=pygame.display.set_mode((500,500)) #даем размер экрана
cell_size=20 #даем размер одной ячейке
pygame.display.set_caption("Жылан ойын") #даем название игре
bg_clr=pygame.Color("white")
snake_color=pygame.Color("green")

snake_pos=[100,100] #стартовая позиция змейки
snake_body=[[160,200],[140,200],[120,200]] #делим змейку на 3 части,каждый субмассив имеет кординаты каждогой части тела змейки
direction="RIGHT"
change_to=direction

food_pos = [r.randint(1, 24) * cell_size, r.randint(1, 24) * cell_size] #даем рандомные кординаты еды
food_spawn = True

food_time=pygame.time.get_ticks() #фиксируем время
clock=pygame.time.Clock()
food_weight=1 #даем начальный вес еды

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #события равны клавишам и привязываем каждую кнопку к нужно стороне и делаем так чтобы змейка не могла повернутся в противополежунную сторону
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to="UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to="DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to="RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to="LEFT"
    direction=change_to
        #даем кординаты змей когда он сдвинулся и каждый шаг равен 20 пикселям или же рамеру клетки
    if direction=="UP":
        snake_pos[1] -=cell_size
    elif direction == "DOWN":
        snake_pos[1] +=cell_size
    elif direction=="LEFT":
        snake_pos[0] -=cell_size
    elif direction == "RIGHT":
        snake_pos[0] +=cell_size
        #когда кординаты змейки равный краям окна переводим змейку к противоположенному краю  
    if snake_pos[0] < 0:
        snake_pos[0] = 500
    elif snake_pos[0] > 500:
        snake_pos[0] = 0
    elif snake_pos[1] < 0:
        snake_pos[1] = 500
    elif snake_pos[1] > 500:
        snake_pos[1] = 0
        
    snake_body.insert(0,list(snake_pos))#добавляем голову змейке
    if snake_pos == food_pos :
        food_spawn = False  # Пища съедена
        for i in range(food_weight):  # Увеличиваем змею на вес еды
            snake_body.insert(0, list(snake_pos))
    else:
        snake_body.pop()  # Убираем хвост
    
    # Генерация новой пищи
    if not food_spawn or pygame.time.get_ticks() - food_time>=5000:#возвращает количество миллисекунд, прошедших с начала работы игры и минусуем появления время еды
        food_pos = [r.randint(1, 24) * cell_size, r.randint(1, 24) * cell_size]
        while food_pos in snake_body:  # Проверяем, не находит ли еда в теле змеи
            food_pos = [r.randint(0, 24) * cell_size, r.randint(0, 24) * cell_size]
        food_weight = r.randint(1, 3)#рандомно даем вес еде
        food_time=pygame.time.get_ticks()#обновляем время еды

    food_spawn = True

    screen.fill(bg_clr)#красим окно белым цветом
    for block in snake_body:
        pygame.draw.rect(screen,snake_color,pygame.Rect(block[0],block[1],cell_size,cell_size))#рисуем каждый блок змейки как квадрат
    
    pygame.draw.rect(screen, "red", pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))#рисуем еду красным цветом

    font = pygame.font.SysFont(None, 28)#даем шрифт и размер шрифта
    weight_text = font.render(str(food_weight), True, pygame.Color("blue"))#делаем надпись веса 
    screen.blit(weight_text, (food_pos[0] + 5, food_pos[1] + 1))#вставляем надпись веса над едой 

    pygame.display.flip()#обновляем экран выводим все работы с памяти как рисунки
    clock.tick(20)#даем fps

pygame.quit()
exit()