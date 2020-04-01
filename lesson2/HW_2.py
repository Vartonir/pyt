"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
использовать функцию input().
"""


my_list = list(input('Заполните список элементами через пробелы: ').split())

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]

print(my_list)

# new_list = []
# type_list = []
# n = int(input('Введите кол-во значений в спике'))
#
# for i in range(n):
#     new_list.append(input())
#
# # lin = ''
# # print('введите любое кол-во значений в список, чтобы остановиться напишите слово stop')
# # while lin != 'stop':
# #     lin = input()
# #     first_list.append(lin)
# #     if lin == 'stop':
# #         first_list.pop(-1)
#
# a = 0
# l_num = ''
# if (len(new_list) % 2) != 0:
#     l_num = new_list[-1]
#     new_list.pop(-1)
#
# for i in range(int(len(new_list) / 2)):
#     new_list[a], new_list[a+1] = new_list[a+1], new_list[a]
#     a += 2
# new_list.append(l_num)
# print(new_list)
