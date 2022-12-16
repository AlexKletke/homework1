# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

Ax = float(input('enter coordinate X of point1:'))
Ay = float(input('enter coordinate Y of point1:'))
Bx = float(input('enter coordinate X of point2:'))
By = float(input('enter coordinate Y of point2:'))
import math
DistanceBetweenPoints = math.sqrt((Ax-Bx)**2+(Ay-By)**2)
print(f'distance between points: {round(DistanceBetweenPoints,3)}')
