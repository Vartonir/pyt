"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Делеить на ноль нельзя'


while True:
    try:
        entry_1 = int(input('Введите первое число: '))
        entry_2 = int(input('Введите второе число: '))
        break
    except ValueError:
        print('Введите число ещё раз')

print(my_func(entry_1, entry_2))

# def my_func(a, b):
#     pass
#     return a/b

# def my_func(**kwargs):
#     pass
#
# @complex
# def my_func2(__init__):
#     pass

# def mu_func(*args, **kwargs):
#     def mu_under_function(name, sex):
#         pass
#
#
# def s_calc():
#     """
#
#     :return:
#     """
#
#     try:
#         r_val = float(input("Укажите радиус: "))
#         h_val = float(input("Укажите высоту: "))
#     except ValueError:
#         return
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_full
#
#
# entry_func()
