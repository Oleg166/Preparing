"""
5. Усовершенствовать первую функцию из предыдущего примера.

Необходимо просканировать текстовый файл, созданный на предыдущем задании
и реализовать создание и запись нового текстового файла

В новый текстовый файл обеспечить запись строк вида:

zmsebjvdgi zmsebjvdgi
ychpwljtzn ychpwljtzn
...

Т.е. извлекаются строки из первого текстового файла
а в новый они записываются в виде, где вместо числа ставится строка

Здесь необходимо использовать регулярные выражения.
"""
import random
import os
import re


def generate_string():
    r_string = ''
    for k in range(10):
        r_string = r_string + chr(random.randint(ord('a'), ord('z')))
    return r_string


def function_number_one(file_name):
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


def function_number_three(file_descriptor):
    """Выполнение замен"""
    # файла из которого берем текст
    file_of = open(file_descriptor.name, 'r')
    # файл, в который запишем измененный текст
    file_out = open('testtest.txt', 'w')

    for line in file_of:
        numbers = re.search(r'\d*', line)
        strings = re.search(r'\s\w*', line)
        line = line.replace(numbers.group(0), strings.group(0))
        file_out.write(line)

    file_of.close()
    file_out.close()

    with open('testtest.txt', encoding='UTF-8') as descriptor:
        for l in descriptor:
            print(l)


DESCRIPTOR = function_number_one('test.txt')
function_number_three(DESCRIPTOR)
