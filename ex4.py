# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('enter the quarter number from 1 to 4: '))
if number == 1:
    print('x > 0, y > 0')
elif number == 2:
    print('x < 0, y > 0')
elif number == 3:
    print('x < 0, y < 0')
elif number == 4:
    print('x > 0, y < 0')
