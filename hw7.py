"""

Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen(). Функция
отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел. По факту надо через for
el in fibo_gen() вывести первые 15 чисел.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""
from functools import reduce


def fibo_gen(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


list_a = [i for i in fibo_gen(18)]

for idx, el in enumerate(list_a, 1):
    if idx > 15:
        break
    print(idx, el)

    
# def factorial(n):
#     return reduce(lambda x, y: x * y, [1] + range(1, n + 1))
#
#
# def factorial(n):
#     f = 1
#     list_a = []
#     for i in range(2, n + 1):
#         f *= i
#         list_a.append(f)
#     yield list_a
#
#
# fibo_gen = factorial(19)
# c = 0
# for el in fibo_gen:
#     print(el)
# fibo_gen = factorials(15)
#
#
# for el in fibo_gen(15):
#     print(el)
