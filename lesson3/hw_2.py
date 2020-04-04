"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.

"""


# def func_data(name, surname, date_of_birth, city, email, tel_number):
#     return print(f'{name.title()} {surname.title()} родился в {date_of_birth} в городе {city.title()} \n'
#                  f'Контактные данные: \n'
#                  f'Электронная почта {email} \n'
#                  f'Номер телефона: {tel_number}')


# def func_data(name, surname, date_of_birth, city, email, tel_number):
#     return print(f'{name.title()} {surname.title()} родился в {date_of_birth} в городе {city.title()}'
#                  f' Контактные данные:'
#                  f' Электронная почта {email}'
#                  f' Номер телефона: {tel_number}')
#
#
# func_data('василий', 'рязанцев', 1978, 'воронеж', 'v.ryazancev@mail.ru', 9507511)

def pers_info(**kwargs):
    return kwargs


print(pers_info(name=input("Введите свое имя: "), surname=input("Введите свою фамилию: "),
                birthday=input("Введите свою дату рождения: "), city=input("Введите свой город проживания: "),
                email=input("Введите свой email: "), phone_number=input("Введите свой номер телефона: ")))
