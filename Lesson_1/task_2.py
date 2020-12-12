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


def print_directory_contents(path):
    list_1 = []
    for i in os.listdir(path):
        name_way = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(name_way):
            list_1.append((os.path.abspath(path), i))
        else:
            list_1.extend(print_directory_contents(name_way))
    return list_1


result = print_directory_contents('D:/Repository/00-Django_18_08_2020/Новая папка/dz6_Dementev_Oleg')
print(result)
