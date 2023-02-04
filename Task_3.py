"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# с помощью функции sort()

def my_func(x, y, z):
    nums = [x, y, z]
    nums.sort()
    return nums[1] + nums[2]

# без функции sort()

def my_func(x, y, z):
    if x > y and x > z:
        return x + max(y, z)
    elif y > z and y > x:
        return y + max(x, z)
    else:
        return z + max(x, y)