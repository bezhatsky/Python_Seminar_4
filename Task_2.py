"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_data(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname} {birth_year} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}')

user_data(name="Иван", surname="Иванов", birth_year=1846, city="Москва", email="jackie@gmail.com", phone="01005321456")
