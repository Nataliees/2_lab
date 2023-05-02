def first():
    psw1 = input('Введите пароль ')
    psw2 = input('Повторите пароль ')
    if(psw1==psw2): print("Пароль принят")
    else: print("Пароль не принят")

def second():
    place = int(input('Введите номер места '))
    if (place <= 0 or place >= 55):
        print('Место введено неверно')
    else:
        if (place > 36 and place < 55):
            if (place % 2 == 0):
                print('Боковое верхнее')
            else:
                print('Боковое нижнее')
        else:
            if (place % 2 == 0):
                print('Верхнее')
            else:
                print('Нижнее')

def third():
    year = int(input('Введите год '))
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print('Год ', year, ' - високосный')
    else:
        print('Год ', year, ' - не високосный')

def fourth():
    r = 'красный'
    y = 'желтый'
    b = 'синий'
    color1 = input('Введите первый цвет ')
    color2 = input('Введите второй цвет ')
    if (color1 != r and color1 != y and color1 != b or color2 != r and color2 != y and color2 != b):
        print('Ошибка. Повторите ввод')
    else:
        if (color1 == r and color2 == y or color2 == r and color1 == y): print('Оранжевый')
        if (color1 == r and color2 == b or color2 == r and color1 == b): print('Фиолетовый')
        if (color1 == b and color2 == y or color2 == b and color1 == y): print('Зеленый')

fourth()
