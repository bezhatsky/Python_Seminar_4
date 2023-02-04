"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
"""

def my_func(x, y):
   res = 1
   for i in range(abs(y)):
     res *= x
   return 1/res if y < 0 else res

x = float(input('ведите положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x, y))
