# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
from random import randint
import math
r2D = [randint(-9, 10) for i in range(4)]
A = (r2D[2] - r2D[0])**2
B = (r2D[3] - r2D[1])**2
AB = round(math.sqrt(A + B),2)
print(AB)