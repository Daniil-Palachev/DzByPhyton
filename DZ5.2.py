# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
play1= player_1
play2= player_2

def sweets_count():
    while True:
        try:
            n = int(input('Введи число конфет: '))
            return n
        except ValueError:
            print ('Все-таки, введи число')
            continue
    
sweets= sweets_count()

def check_the_game_mode():
    c = int(input('Введи режим игры (1 - против второго игрока, 2- против машины) : '))
    if c==1: 
        print('Ты выбрал игру против человека')
    elif c==2:
        print('Ты выбрал игру против машины')
    else:
        print ('Начни игру заново и все-таки, введи число')
    return c
game_mod=check_the_game_mode()    
            
        

def isint():
    while True:
        try:
            n = int(input('Введи число : '))
            return n
        except ValueError:
            print ('Все-таки, введи число')
            continue
        

def take_sweets(sweets):
    if game_mod==2:
        turn= random.randint(0, 2)
        while sweets>0:
            if turn%2:
                take=0
                while not (0 <take<29 and take<=sweets):
                    take= isint()
                    if not 0<take<29: 
                        print('Введено не верное кол-во конфет')
                    elif take==sweets:
                        print('Human win, machines have to die')
                sweets= sweets- take 
                print('Остаток конфет: ', sweets) 
            if not turn%2:
                turn_ai=sweets%29
                if turn_ai==0:
                    turn_ai= random.randint(1, 28)
                print('Stupid AI take: ', turn_ai)
                sweets-=turn_ai
                print('Остаток конфет: ', sweets) 
                if sweets==0:
                    print('People must die')
            turn+=1
    elif game_mod==1:
        turn= random.randint(0, 2)
        while sweets>0:
            if turn%2:
                take=0
                while not (0 <take<29 and take<=sweets):
                    print(play1)
                    take= isint()
                    if not 0<take<29: 
                        print('Введено не верное кол-во конфет')
                    elif take==sweets:
                        print(play1, ' win')
                sweets= sweets- take
                print('Остаток конфет: ', sweets)  
            if not turn%2:
                take=0
                while not (0 <take<29 and take<=sweets):
                    print(play2)
                    take= isint()
                    if not 0<take<29: 
                        print('Введено не верное кол-во конфет')
                    elif take==sweets:
                        print(play2, 'win')
                sweets= sweets- take
                print('Остаток конфет: ', sweets) 
            turn+=1

take_sweets(sweets)
        

            

         



