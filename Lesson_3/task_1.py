"""
1. Написать программу, которая будет содержать функцию
для получения имени файла из полного пути до него.

При вызове функции в качестве аргумента должен передаваться путь до файла.
В функции необходимо реализовать «выделение» из этого пути имени файла (без расширения).

Пример:
функция принмает следующую строку - '../mainapp/views.py'

Результат:
views
"""
STR = '../mainapp/views.py'


def namefile(stringone):
    list_1 = stringone.split('/')
    str_1 = list_1[len(list_1)-1]
    list_2 = str_1.split('.')
    return list_2[0]


print(namefile(STR))
