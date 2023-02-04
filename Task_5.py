"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

import timeit

def my_func(x, y):
   res = 1
   for i in range(abs(y)):
     res *= x
   return 1/res if y < 0 else res

x = float(input('ведите положительное число: '))
y = int(input('введите целое отрицательное число: '))

# профилирование с помощью модуля timeit
t = timeit.timeit('my_func(x, y)', setup='from __main__ import my_func, x, y', number=1000)

print(f'Время выполнения my_func 1000 раз: {t} секунд')
print(f'{x} в степени {y} = {my_func(x, y)}')

# Результат профилирования с помощью модуля timeit для функции my_func составляет t секунд при 1000 запусках кода.