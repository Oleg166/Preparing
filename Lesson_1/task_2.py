"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""
import os


def print_directory_contents(sPath):
    list_1 = os.listdir(path=sPath)
    list_2 = []
    list_3 = []
    for i in list_1:
        if i.find('.') != -1:
            list_2.append(i)
        else:
            list_3.append(i)
    list_11 = []
    list_11.append(sPath)
    for j in list_2:
        list_11.append(j)
    tuple_1 = tuple(list_11)
    print(tuple_1)
    for q in list_3:
        sPath = sPath + '/' + str(q)
        print_directory_contents(sPath)


print_directory_contents('D:/Repository/00-Django_18_08_2020/Новая папка/dz6_Dementev_Oleg')
