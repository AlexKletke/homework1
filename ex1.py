# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

n = int(input('enter a number from 0 to 7: '))
if n == 6 or n == 7:
    print("этот день является выходным")
else:
    print("Ура! этот день является рабочим и можно еще поработать!")

