# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random
sweets= 100

def take_sweets(sweets):
    turn= random.randint(0, 2)
    while sweets>0:
        print(sweets)
        if turn%2:
            take=0
            while not (0 <take<29 and take<=sweets):
                take= int(input('Количетсво конфет к изъятию человеком: '))
                if not 0<take<29: 
                    print('Введено не верное кол-во конфет')
                elif take==sweets:
                    print('Human win, machines have to die')
            sweets= sweets- take 
        if not turn%2:
            turn_ai=sweets%29
            if turn_ai==0:
                turn_ai= random.randint(0, 28)
            print('Stupid AI take: ', turn_ai)
            sweets-=turn_ai
            if sweets==0:
                print('People must die')
        turn+=1
take_sweets(sweets)
        

            

         



