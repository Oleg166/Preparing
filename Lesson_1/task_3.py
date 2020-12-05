"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16,
'elem_8': 8}
)
"""
import random


def random_number(start, end):
    list_1 = []
    list_for_dict = []
    for i in range(0, 10):
        th = random.randint(start, end)
        list_for_dict.append(('elem_' + str(th), th))
        list_1.append(th)
    dict_1 = dict(list_for_dict)
    return list_1, dict_1


print(random_number(8, 23))
