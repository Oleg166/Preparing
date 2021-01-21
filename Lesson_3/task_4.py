"""
4. Написать программу, в которой реализовать две функции.

В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.

Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Например:
[91, 42, 47, 64, 60, 23, 82, 78, 22, 15]
и
['zmsebjvdgi', 'ychpwljtzn', 'zqywoopbwf', 'nkxdnnqyhe', 'eqpbrjwjdp',
'sllbegvgmh', 'kzrmrozeco', 'jbppumpypu', 'jjsmronkvm', 'qtnspcleqd']


Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Например:
91 zmsebjvdgi

42 ychpwljtzn

...

Первая функция должна возвращать ссылку на файловый дескриптор


После вызова первой функции возвращаемый файловый дескриптор нужно передавать во вторую функцию
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
"""
import random
import os


def generate_string():
    """Генерация строки и з 10 символов"""
    r_string = ''
    for k in range(10):
        r_string = r_string + chr(random.randint(ord('a'), ord('z')))
    return r_string


def function_number_one(file_name):
    """Открытие и запись файла"""
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file_descriptor:
            print("Файл с таким именем уже существует")
            return file_descriptor
    list_1 = [random.randint(0, 100) for x in range(10)]
    list_2 = [generate_string() for z in range(10)]
    tuple_1 = list(zip(list_1, list_2))

    with open(file_name, 'w', encoding='UTF-8') as file_descriptor:
        for i in range(10):
            file_descriptor.write(f"{tuple_1[i][0]} {tuple_1[i][1]}\n")
        return file_descriptor


def function_number_two(file_descriptor):
    """Чтение файла"""
    with open(file_descriptor.name, 'r', encoding='UTF-8') as descriptor:
        for line in descriptor:  # считываем файл построчно
            print(line)


DESCRIPTOR = function_number_one('test.txt')
function_number_two(DESCRIPTOR)
