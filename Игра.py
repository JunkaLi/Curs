import pdb # загрузка необходимых модулей

import pygame

import random

clock = pygame.time.Clock() # объект для управления временем в программе, часотой кадров
pygame.init() # строка для работы с кодом на pygame
screen = pygame.display.set_mode((1000, 600)) # установление расширения экрана

lvl1 = False # переменные для определения нынешнего уровня
lvl2 = False
lvl3 = False

lvl1_done = False # переменные для обозначения пройденных уровней
lvl2_done = False
lvl3_done = False

bl_grapes = True # переменные для показа объектов во втором уровне
bl_hazelnut = False
bl_icecream = False
bl_jam = False
bl_kiwi = False
bl_lemon = False
bl_mango = False
bl_nectarine = False
bl_onion = False

eat_sp = 8 # скорость объектов во 2 уровне


pygame.display.set_caption('ABC Wonderland: Learn English with Fun!') # название приложения
icon = pygame.image.load('images/icon_girl_cut.png') # загрузка изображения для иконки игры
pygame.display.set_icon(icon) # установка иконки
pygame.mixer.music.load('SOUNDS/opening.mp3') # установка фоновой музыки
pygame.mixer.music.play(-1) # запуск фоновой музыки с бесконечным повтором
win_sound = pygame.mixer.Sound('SOUNDS/win.mp3') # установка звука победы
lab_sound = pygame.mixer.Sound('SOUNDS/lab.mp3') # фоновый звук для уровня с лабиринтом
lvl2_sound = pygame.mixer.Sound('SOUNDS/lvl2.mp3') # фоновый звук для второго уровня


GAME_FONT = pygame.font.Font("fonts/undertale_battle_font.ttf", 66) # загрузка шрифта
GAME_FONT1 = pygame.font.Font("fonts/undertale_battle_font.ttf", 50) # загрузка шрифта в другом размере

alligator = pygame.image.load('images/alligator.png')  # загрузка изображений для первого уровня
bee = pygame.image.load('images/bee.png')
cat = pygame.image.load('images/cat.png')
dog = pygame.image.load('images/dog.png')
elephant = pygame.image.load('images/elephant.png')
frog = pygame.image.load('images/frog.png')

grapes = pygame.image.load('images/grapes.png') # загрузка изображений для второго уровня
hazelnut = pygame.image.load('images/hazelnut.png')
icecream = pygame.image.load('images/ice-cream.png')
jam = pygame.image.load('images/jam.png')
kiwi = pygame.image.load('images/kiwi.png')
lemon = pygame.image.load('images/lemon.png')
mango = pygame.image.load('images/mango.png')
nectarine = pygame.image.load('images/nectarine.png')
onion = pygame.image.load('images/onion.png')

big_alligator = pygame.image.load('big_images/alligator.png') # загрузка изображений в крупном размере для 1 уровня
big_bee = pygame.image.load('big_images/bee.png')
big_cat = pygame.image.load('big_images/cat.png')
big_dog = pygame.image.load('big_images/dog.png')
big_elephant = pygame.image.load('big_images/elephant.png')
big_frog = pygame.image.load('big_images/frog.png')

rectik = pygame.image.load('images/rect.png') # загрузка изображений для возможности выхода в главное меню
back_menu = pygame.image.load('images/back_menu.png')
yes = pygame.image.load('images/yes.png')
no = pygame.image.load('images/no.png')

background_image = pygame.image.load('images/background1.png') # загрузка фона для главного меню
background_image = pygame.transform.scale(background_image, (1000, 600)) # трансформация размера

quit_image =  pygame.image.load('images/quit.png') # загрузка изображения для выхода из главного меню
quit_image = pygame.transform.scale(quit_image,(1000,600)) # трансформация размера

lab1 = pygame.image.load('images/Собрать все буквы.png') # изображение для старта первого уровня
levels = pygame.image.load('images/levels.png') # загрузка изображения для меню с выбором уровней
final_lab = pygame.image.load('images/run.png') # изображение для уровня с лабиринтом
win_lvl2 = pygame.image.load('images/win_lvl2.png') # загрузка изображения для победы во втором уровне
win_lab = pygame.image.load('images/win_lab.png') # загрузка изображения для победы в первом уровне
background_image2 = pygame.image.load('images/лабиринт.png') # фон для первого уровня
background_image2 = pygame.transform.scale(background_image2, (1000, 600)) # трансформация фона для текущего расширения

rightS = pygame.image.load('images/rightS.png')
cursorp = pygame.image.load('images/paw.png').convert_alpha() # загрузка изображения для дополнительного курсора
cursorp = pygame.transform.scale(cursorp, (50, 50)) # трансформация разера курсора

lvl2_bg = pygame.image.load('images/2lvl.png') # фон для 2 уровня
telezhka = pygame.image.load('images/telezhka.png') # персонаж для 2 уровня
sweets = pygame.image.load('images/Лови вкусняшки.png') # стартовое изображение для 2 уровня
lvl3_bg = pygame.image.load('images/space.png') # фон для 3 уровня
lvl3_bg = pygame.transform.scale(lvl3_bg, (1000,600)) # трансформация размера
rocket = pygame.image.load('images/rocket.png') # персонаж для 3 уровня

alligator_sound = pygame.mixer.Sound('SOUNDS/alligator.mp3') # звуки произношения слов для 1 уровня
bee_sound = pygame.mixer.Sound('SOUNDS/bee.mp3')
cat_sound = pygame.mixer.Sound('SOUNDS/cat.mp3')
dog_sound = pygame.mixer.Sound('SOUNDS/dog.mp3')
elephant_sound = pygame.mixer.Sound('SOUNDS/elephant.mp3')
frog_sound = pygame.mixer.Sound('SOUNDS/frog.mp3')

bgx = 0  # величина для передвижения фона на 3 уровне

walk_right=[
pygame.image.load('images/rightG1.png'),
 pygame.image.load('images/rightG.png'),
pygame.image.load('images/rightS.png')] # набор изображений для передвижения персонажа вправо на 1 уровне

walk_left=[
pygame.image.load('images/leftG1.png'),
 pygame.image.load('images/leftG.png'),
pygame.image.load('images/leftS.png')] # набор изображений для передвижения персонажа влево на 1 уровне

walk_forward=[
pygame.image.load('images/forwardG1.png'),
 pygame.image.load('images/forwardG.png'),
 pygame.image.load('images/forwardS.png')] # набор изображений для передвижения персонажа вперед на 1 уровне

walk_back=[
pygame.image.load('images/backG1.png'),
pygame.image.load('images/backG.png'),
pygame.image.load('images/backS.png')] # набор изображений для передвижения персонажа назад на 1 уровне

show_elephant = 0 # величины для показа картинок со словами и демонстрации произношения этих слов на 1 уровне
show_alligator = 0
show_bee = 0
show_cat = 0
show_dog = 0
show_frog = 0

gy = 0 # координаты для обозначения позиции предметов на 2 уровне
hy = 0
iy = 0
jy = 0
ky = 0
ly = 0
may = 0
ny = 0
oy = 0

player_speed = 10 # начальная скорость игрока

x = 500 # координаты игрока
y = 455
c = 2 # величина для определения направления персонажа на 1 уровне

mn = 0

tx = 5 # положение персонажа на 2 уровне
ty = 400

rocket_x = 100 # положение персонажа на 3 уровне
rocket_y = 200

found = 0 # величины обозначения найденных букв на 1 уровне
found1 = 0
found2 = 0
found3 = 0
found4 = 0
found5 = 0
final = 8
fruits = 0

anim_count = 0

done = False # обозначение для игрового процесса

start = 0 # обозначение стартового меню

while not done: # старт игры
    pos = pygame.mouse.get_pos() # получение координат курсора
    px, py = pygame.mouse.get_pos()
    if start == 0: # цикл для изменения курсора при наведении на кнопки в главном меню
        screen.blit(background_image, (0, 0)) # показ экрана главного меню
        if px > 702 and px < 917 and py > 336 and py < 422:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px > 702 and px < 918 and py > 140 and py < 222:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px > 23 and px < 176 and py > 528 and py < 570:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        else:
            pygame.mouse.set_visible(True)

    elif start == 2: # цикл для показа курсора при показе экрана с возможностью выйти из игры из главного меню
        screen.blit(quit_image,(0,0))
        if px>653 and px<849 and py>358 and py<449:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px>214 and px<405 and py>359 and py<447:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        else:
            pygame.mouse.set_visible(True)

    elif start == 3: # оставляем курсор видимым в самом начале 1 уровня
        pygame.mouse.set_visible(True)

    elif start == 7: # цикл для показа нового курсора при наведении мыши на кнопки для выбора уровня
        if px>21 and px<115 and py>13 and py<44:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px > 169 and px < 299 and py > 167 and py < 299:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px > 435 and px < 565 and py > 167 and py < 299:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px>264 and px<440 and py>368 and py<498:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        else:
            pygame.mouse.set_visible(True)
    elif start == 6:
            pygame.mouse.set_visible(True)

    elif start == 8: # возможность выхода из уровня (любого). смена курсора при наведении на кнопки
        if px > 60 and px < 300 and py > 350 and py < 500:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        elif px > 640 and px < 940 and py > 350 and py < 500:
            pygame.mouse.set_visible(False)
            screen.blit(cursorp, pos)
        else:
            pygame.mouse.set_visible(True)

    elif start == 9 and lvl2 == True: # цикл для второго уровня
        screen.blit(lvl2_bg, (0, 0)) # показ фона
        screen.blit(telezhka, (tx, ty)) # показ игрока на заданных координатах
        if gy + 100 >= ty and (tx < gx < gtx) and bl_grapes == True: # далее идет показ объектов, их падение,
            # исчезновение при совпадении с координатами игрока
            fruits += 1
            bl_hazelnut = True
            bl_grapes = False
        elif gy + 100 >= ty and bl_grapes == False:
            bl_grapes = False
        elif bl_grapes == True:
            screen.blit(grapes, (gx, gy))
            gy += eat_sp

        if hy + 100 >= ty and (tx<hx<gtx) and bl_hazelnut == True:
            fruits += 1
            bl_icecream = True
            bl_hazelnut = False
        elif hy+100 >= ty and bl_hazelnut == False:
            bl_hazelnut = False
        elif bl_hazelnut == True:
            screen.blit(hazelnut, (hx, hy))
            hy += eat_sp+1

        if iy+80 >= ty and (tx<ix<gtx) and bl_icecream == True:
            fruits += 1
            bl_jam = True
            bl_icecream = False
        elif iy+80 >= ty and bl_icecream == False:
            bl_icecream= False
        elif bl_icecream == True:
            screen.blit(icecream, (ix, iy))
            iy+=eat_sp+2

        if jy+80 >= ty and (tx<jx<gtx) and bl_jam == True:
            fruits +=1
            bl_kiwi = True
            bl_jam = False
        elif jy+80 >= ty and bl_jam == False:
            bl_jam= False
        elif bl_jam == True:
            screen.blit(jam, (jx, jy))
            jy+=eat_sp+3

        if ky+80 >= ty and (tx<kx<gtx) and bl_kiwi == True:
            fruits +=1
            bl_lemon = True
            bl_kiwi = False
        elif ky+80 >= ty and bl_kiwi == False:
            bl_kiwi = False
        elif bl_kiwi == True:
            screen.blit(kiwi, (kx, ky))
            ky+=eat_sp+4

        if ly+80 >= ty and (tx<lx<gtx) and bl_lemon == True:
            fruits +=1
            bl_mango = True
            bl_lemon = False
        elif ly+80 >= ty and bl_lemon == False:
            bl_lemon = False
        elif bl_lemon == True:
            screen.blit(lemon, (lx, ly))
            ly+=eat_sp+6

        if may+80 >= ty and (tx<max<gtx) and bl_mango == True:
            fruits += 1
            bl_nectarine = True
            bl_mango = False
        elif may+80 >= ty and bl_mango == False:
            bl_mango = False
        elif bl_mango == True:
            screen.blit(mango, (max, may))
            may+=eat_sp+7

        if ny+80 >= ty and (tx<nx<gtx) and bl_nectarine == True:
            fruits += 1
            bl_onion = True
            bl_nectarine = False
        elif ny+80 >= ty and bl_nectarine == False:
            bl_nectarine = False
        elif bl_nectarine == True:
            screen.blit(nectarine, (nx, ny))
            ny+=eat_sp+8

        if oy + 80 >= ty and (tx<ox<gtx) and bl_onion == True:
            fruits += 1
            bl_onion = False
        elif ky + 80 >= ty and bl_onion == False:
            bl_onion = False
        elif bl_onion == True:
            screen.blit(onion, (ox, oy))
            oy += eat_sp+9

        if fruits == 9: # если все вкусняшки собраны...
            screen.blit(win_lvl2, (75,40)) # показать экран победы
            text_surface = GAME_FONT1.render("Меню", 1, (153, 0, 0))
            screen.blit(text_surface, (50, 5)) # показать возможность выхода в меню
            lvl2_done = True
        pygame.mouse.set_visible(True)
        pressed = pygame.key.get_pressed() # отслеживание нажатия кнопки на клавиатуре

        if pressed[pygame.K_LEFT] and tx>0: # передвижение влево
            tx -= player_speed*3
            gtx = tx + 120
        elif pressed[pygame.K_RIGHT] and tx <836: # передвижение вправо
            tx += player_speed*3
            gtx = tx + 120
        elif pressed[pygame.K_n]: # отслеживание координат персонажа
            print(tx, ty)

    elif start == 11 and lvl3 == True: # если мы на 3 уровне...
        pressed = pygame.key.get_pressed()
        bgx -= 5 # уменьшение координаты фона для того, чтобы он двигался
        if bgx == -1000: # если координата фона меньше чем ширина экрана...
            bgx = 0 # координата фона обнуляется
            screen.blit(lvl3_bg, (bgx, 0))
            screen.blit(lvl3_bg, (bgx + 1000, 0))
        screen.blit(lvl3_bg, (bgx, 0)) # показ фона
        screen.blit(lvl3_bg, (bgx + 1000, 0)) # второй показ фона в координатах за пределами экрана
        screen.blit(rocket, (rocket_x, rocket_y)) # показ персонажа на 3 уровне
        pygame.mouse.set_visible(True)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and rocket_y>100: # движение вверх
            rocket_y -= player_speed
            if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение
                rocket_y -= 5
        elif pressed[pygame.K_DOWN] and rocket_y<400: # движение вниз
            rocket_y +=player_speed
            if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение
                rocket_y += 5
        elif pressed[pygame.K_RIGHT] and rocket_x<800: # движение вправо
            rocket_x += player_speed
            if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение
                rocket_x += 5
        elif pressed[pygame.K_LEFT] and rocket_x>50: # движение влево
            rocket_x -= player_speed
            if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение
                rocket_x -= 5
    else:
        pygame.mouse.set_visible(True) # в противном случае оставляем курсорр обычным
    pygame.display.update() # обновление экрана

    for event in pygame.event.get(): # цикл для реализации выхода из игры
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            pdb.set_trace()
            break

        if start == 3 and event.type == pygame.KEYUP: # цикл для начала игрового процесса 1 уровня
            if event.key == pygame.K_SPACE:
                start = 1

        elif event.type == pygame.KEYDOWN and start == 10: # цикл для начала игрового процесса 2 уровня
            if event.key == pygame.K_SPACE:
                lx = random.randint(50, 500) # случайный выбор координаты по горизонтали для объектов 2 уровня
                hx = random.randint(50, 500)
                ix = random.randint(50, 500)
                jx = random.randint(50, 500)
                kx = random.randint(50, 500)
                gx = random.randint(50, 500)
                max = random.randint(50, 500)
                nx = random.randint(50, 500)
                ox = random.randint(50, 500)
                start = 9

        elif ((start == 3 or start == 1 or start == 9 or start == 11)
              and event.type == pygame.KEYUP): # возможность выхода в главное меню из любого уровня
            if event.key == pygame.K_ESCAPE:
                start = 8

        elif ((start == 13 or start == 14 or start == 15 or start ==16 or start == 17 or start == 12)
            and event.type == pygame.KEYUP): # возвращение к уровню после демонстрации картинок
                if event.key == pygame.K_SPACE:
                    start = 1

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1: # отслеживание нажатия левой кнопки мыши
           mx,my = pygame.mouse.get_pos() # координаты курсора
           print(mx,my)
           if (mx>702 and mx<918 and my>140 and my<222
                   and event.button == 1 and start == 0): # переход к выбору уровней
               start = 7
           elif (mx>23 and mx<176 and my>528 and my<570
                 and event.button == 1 and start == 0): # выход из игры
               start = 2
           elif  (mx > 435 and mx < 565 and my > 167 and my < 299
                  and event.button == 1 and start == 7): # выбор 2 уровня
               start = 10
               lvl2 = True
               pygame.mixer.music.pause() # остановка фоновой музыки главного меню
           elif mx>264 and mx<440 and my>368 and my<498 and start == 7: # выбор 3 уровня
               start = 11
               lvl3 = True
               pygame.mixer.music.pause() # остановка фоновой музыки
           elif (mx > 653 and mx < 849 and my > 358 and my < 449
                 and event.button == 1 and start == 2): # отказ от выхода из игры из главного меню
               start = 0
           elif (mx>214 and mx<405 and my>359 and my<447 and start ==2
                 and event.button == 1): # выход из игры из главного меню
               pygame.quit()
           elif start == 7:  # если мы в меню с выбором уровней...
               if px > 21 and px < 115 and py > 13 and py < 44: # возвращение в главное меню
                 start = 0
               if px>169 and px<299 and py>167 and py<299: # старт 1 уровня
                 start = 3
                 lvl1 = True
                 #ch = lab_sound.play(-1)
                 #pygame.mixer.music.pause()
           elif start == 6: # выход из игрового процесса в меню выбора уровней, обнуление уже найденного
               if px > 49 and px < 200 and py > 20 and py < 30:
                   start = 7
                   lvl1 = False
                   lvl2 = False
                   found = 0
                   found1 = 0
                   found2 = 0
                   found3 = 0
                   found4 = 0
                   found5 = 0
                   final = 0

           elif start == 8: # если мы находимся в экране возможности выхода в меню из любого уровня...
               if px > 60 and px < 300 and py > 350 and py < 500: # попадаем в меню
                   start = 7
                   lvl1 = False
                   lvl2 = False
                   lvl3 = False
               elif px > 640 and px < 940 and py > 350 and py < 500: # остаемся в уровне
                   if lvl1 == True:
                       start = 1
                   elif lvl2 == True:
                       # установка случайной координаты по горизонтали для предметов 2 уровня,
                       # первая буква -- первая бука названия объекта
                       lx = random.randint(50, 500)
                       hx = random.randint(50, 500)
                       ix = random.randint(50, 500)
                       jx = random.randint(50, 500)
                       kx = random.randint(50, 500)
                       gx = random.randint(50, 500)
                       max = random.randint(50, 500)
                       nx = random.randint(50, 500)
                       ox = random.randint(50, 500)
                       start = 9
                   elif lvl3 == True:
                       start = 11 # начало 3 уровня
           elif px>346 and px<416 and py>424 and py<486: # повторное воспроизведение звука с произношением слова
               if start == 12:
                   alligator_sound.play(0)
               elif start == 13:
                   elephant_sound.play(0)
               elif start == 14:
                   frog_sound.play(0)
               elif start == 15:
                   dog_sound.play(0)
               elif start == 16:
                   cat_sound.play(0)
               elif start == 17:
                   bee_sound.play(0)
           elif start == 9: # выход в меню после победы во 2 уровне
              if 160 > px > 46 and 52 > py > 11:
                 fruits = 0
                 start = 7
                 lvl2 = False
                 pygame.mixer.music.unpause() # продолжение проигрыша основной фоновой музыки

    if start == 7: # показ изображения для меню с выбором уровней
        screen.blit(levels, (0,0))
    if start == 2: # показ изображеняи для возможности выхода из игры из главного меню
        screen.blit(quit_image,(0,0))
    if start == 8: # показ изображения для возможности выхода в меню из любого уровня
        screen.blit(rectik, (0,0))
        screen.blit(back_menu, (60, 100))
        screen.blit(yes, (60, 350))
        screen.blit(no, (640, 350))
    if start == 10: # показ персонажа и фона во 2 уровне, начало уровня
        screen.blit(lvl2_bg, (0,0))
        screen.blit(telezhka, (tx, ty))
        screen.blit(sweets, (60,11))

    if start == 1 or start == 3: # показ букв в 1 уровне

        pygame.mouse.set_visible(True)

        screen.blit(background_image2,(0,0)) # показ фона для 1 уровня
        text_surface = GAME_FONT.render("A", 1, (128,0,0))
        screen.blit(text_surface, (133, 470))

        text_surface= GAME_FONT.render("B", 1, (255,125,0))
        screen.blit(text_surface, (224, 265))

        text_surface = GAME_FONT.render("C", 1, (255,255,0))
        screen.blit(text_surface, (129, 51))

        text_surface = GAME_FONT.render("D", 1, (0,255,0))
        screen.blit(text_surface, (835, 62))

        text_surface = GAME_FONT.render("E", 1, (0,125,255))
        screen.blit(text_surface, (630, 375))

        text_surface = GAME_FONT.render("F", 1, (125,0,55))
        screen.blit(text_surface, (835, 463))

        if start == 3: # старт 1 уровня
            screen.blit(lab1, (60,11))
            screen.blit(walk_forward[2], (x, y))
        if start == 1: # если мы в 1 уровне, то показывает изображения при нахождении какой-либо буквы
            if found == 1:
              screen.blit(alligator, (127, 480))
              show_alligator = 1
            if found1 == 2:
              screen.blit(bee, (224,275))
              show_bee = 1
            if found2 == 1:
              screen.blit(cat, (121, 60))
              show_cat = 1
            if found3 == 2:
              screen.blit(dog, (827,73))
              show_dog = 1
            if found4 == 1:
              screen.blit(elephant, (623, 385))
            if found5 == 2:
              screen.blit(frog, (829,475))
              show_frog = 1

            pressed = pygame.key.get_pressed() # отслеживание нажатия кнопки клавиатуры

            if pressed[pygame.K_UP] and (y > 20 or 22 < x and x < 28) and not ((x < 284 and y < 404 and y > 362)
               or (x<319 and x>119 and y>294 and y<306) or (y<183 and y>171 and x>318 and x<584) or
                   (y<183 and y>171 and x>183 and x<279) or (y<183 and y>171 and x>694) or
                   (x>625 and x<690 and y<322 and y>310) or (x>689 and y<189 and y>177) or
                   (x>527 and x<627 and y<72 and y>60) or (x<384 and y<74 and y>62) or
                   (x<689 and x>626 and y<392 and y>380) or (y<392 and y>380 and ((x>514 and x<591) or
                   (x<493 and x>416)) or (x<798 and x>698 and y<72) or (x>590 and x<625 and y<303 and y>291))):
                y -= player_speed # установка ограничений и передвижение персонажа вперед...
                screen.blit(walk_back[anim_count], (x, y))
                c = 1
                if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение персонажа
                    y -= 3

            elif pressed[pygame.K_DOWN] and y < 450 and not ((x<284 and y<373 and y>371) or
                 (x<319 and x>278 and y>263 and y<275) or (y<140 and y>128 and x>318 and x<584) or
                 (y<140 and y>128 and x>183 and x<279) or (y<140 and y>128 and x>694) or
                 (x>625 and x<690 and y<291 and y>279) or (x>689 and y<158 and y>146) or
                 (x>527 and x<627 and y<41 and y>29) or (x<384 and y<43 and y>31) or
                 (x>527 and x<627 and y<237 and y>225) or (x>725 and x<783 and y>178 and y<239) or
                 (x<283 and y>333 and y<345) or (y>237 and y<249 and x<386 and x>197)):
                screen.blit(walk_forward[anim_count], (x, y))
                y += player_speed # установка ограничений и передвижение персонажа назад...
                c = 2
                if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение персонажа
                    y += 3

            elif pressed[pygame.K_LEFT] and x > 95 and not (x<498 and y > 460) and not((y>246 and x<398 and x>386)
                 or (y>137 and x<208 and x> 204 and y<184) or (x<700 and x>675 and y>28 and y<445) or
                 (x<598 and x>588 and y>239 and y<406) or (x<505 and x>490 and y<444) or
                 (x<800 and (y>245 or y<75) and x>790) or (x<590 and x>580 and y<200 and y>145) or
                 (x<300 and x>288 and y<208 and y>127) or (x<350 and x>300 and y<448 and y>350) or
                 (x>390 and x<416 and y>26 and y<117) or (x>185 and x<197 and y>156 and y<246) ):
                x -= player_speed # установка ограничений и передвижение персонажа налево...
                screen.blit(walk_left[anim_count], (x, y))
                c = 3
                if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение персонажа
                    x -= 3

            elif pressed[pygame.K_RIGHT] and x < 810 and not((y>455)or (x<520 and x>470 and y<410 and y>250) or
                (x<720 and x>710 and (y<82 or y>240)) or (x>695 and x<702 and (y>245 or y<70)) or
                (y>285 and x<340 and x>310) or (y<410 and x>420 and x<450) or
                (x<310 and x>300 and y>127 and y<225) or (y<404 and y>24 and x>620 and x<690) or
                (x<526 and x>503 and y>24 and y<75) or (x>116 and x<151 and y>156 and y<246) or
                (x>117 and x<105 and y>133 and y<294)): # движение направо
                c = 0
                x += player_speed # установка ограничений и передвижение персонажа направо...
                screen.blit(walk_right[anim_count], (x, y))
                if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: # ускорение персонажа
                    x += 3

            elif pressed[pygame.K_m]: # нужно для того, чтобы узнать позицию игрока в данный момент нажатием
                # на клавишу m
                print(x,y)

            else: # при остановке движения данный цикл показывает персонажа в правильном направлении
                if c == 0:
                    screen.blit(walk_right[2], (x, y))
                if c == 1:
                    screen.blit(walk_back[2], (x, y))
                if c == 2:
                    screen.blit(walk_forward[2], (x, y))
                if c == 3:
                    screen.blit(walk_left[2], (x, y))
            if anim_count == 1: # показ кадров при передвижении персонажа (счет кадров для показа нового)
                anim_count = 0
            else:
                anim_count += 1

            if x < 125 and y > 439 and show_alligator == 0: # показ изображений и воспроизведение аудио с корректным
                # произношением слова при нахождении буквы
                found = 1
                alligator_sound.play(0)
                start = 12
                show_alligator = 1

            elif 212 < x < 224 and 181 < y < 246 and show_bee == 0:
                found1 = 2
                bee_sound.play(0)
                start = 17
                show_bee = 1

            elif x < 149 and y <30 and show_cat == 0:
                found2 = 1
                cat_sound.play(0)
                start = 16
                show_cat = 1

            elif  x>794 and y<62 and show_dog == 0:
                found3 = 2
                dog_sound.play(0)
                start = 15
                show_dog = 1

            elif x < 627 and x>590 and y <374 and y>362 and show_elephant == 0:
                found4 = 1
                elephant_sound.play(0)
                start = 13
                show_elephant = 1

            elif x>783 and y>371 and show_frog == 0:
                found5 = 2
                frog_sound.play(0)
                start = 14
                show_frog = 1

            if (found == 1 and found1 == 2 and found2 == 1 and found3 == 2 and found4 == 1 and found5 ==2 and
                    not (final==0) and start!=12 and start !=13 and start != 14 and start != 15 and start != 16
                    and start != 17):
                screen.blit(final_lab, (60,11)) # подсказка бежать к выходку при сборке всех букв
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        final = 0

            if x>393 and x<425 and y<20 and final == 0: # воспроизведение звука при победе в первом уровне
                start = 6
                win_sound.play()

            if start == 6: # показ изображения при победе в первом уровне
                screen.blit((win_lab), (75, 40))
                text_surface = GAME_FONT1.render("Меню", 1, (153, 0, 0))
                screen.blit(text_surface, (50, 5))
                lvl1_done = True

        if start == 12: # циклы для показа изображений в первом уровне при находе букв
            screen.blit(big_alligator, (336,109))
        if start == 13:
            screen.blit(big_elephant, (336,109))
        if start == 14:
            screen.blit(big_frog, (336,109))
        if start == 15:
            screen.blit(big_dog, (336,109))
        if start == 16:
            screen.blit(big_cat, (336,109))
        if start == 17:
            screen.blit(big_bee, (336,109))

        pygame.display.update() # обновление экрана

    clock.tick(10) # частота кадров