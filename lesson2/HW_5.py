"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем
же значением должен разместиться после них.
"""


my_list = [7, 5, 3, 3, 2]
n = int(input('Введите кол-во добавляемых значений: '))

for i in range(n):
    a = 0
    rate = int(input('Введите число рейтинга: '))
    for val in my_list:
        if rate > val:
            break
        a += 1
    my_list.insert(a, rate)
    print(my_list)

# a = ''
# while a != "стоп":
#     print('Если захотите оставновится напишите слово ' + 'стоп'.upper())
#     a = input('Введите число рейтинга: ').lower()
#     if a == 'стоп':
#         break
#     else:
#         my_list.append(int(a))
#         my_list.sort()
#         my_list.reverse()
#         print(my_list)


# Мне кажется это неправильно, надо подумать....

