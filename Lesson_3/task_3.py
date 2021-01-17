"""
3. Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения,
в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.

Например, ф-ция принимает два объекта [3, 4, 5, 6], [44, 66, 56]
и возвращает {3: 44, 4: 66, 5: 56, 6: None}
"""
list_key = [3, 4, 5, 6]
list_value = [44, 66, 56]


if len(list_value) > len(list_key):
    list_value = list_value[0:len(list_key)]
elif len(list_key) > len(list_value):
    for i in range(0, len(list_key) - len(list_value)):
        list_value.append(None)

dict_1 = {list_key[j]: list_value[j] for j in range(0, len(list_key))}
print(dict_1)
