"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

new_list = [123, 45.4, True, 'Vasya', 4]
for el in new_list:
    print(el, type(el))
