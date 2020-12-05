"""
Задание 4. Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется
процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен
быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и
значения процентной ставки для каждого срока. В функции необходимо
проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает
сумму вклада на конец срока.

Примечание: используем функциональный подход (не ООП)
Вы можете сделать расчет без капитализации и с капитализацией

Пример без капитализации: 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11300

Пример с капитализацией (ежемесячной): 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11384.29
"""


def deposit(begin_sum, month):
    if 100 <= begin_sum < 10000 and month == 6:
        rate = 5
    elif 100 <= begin_sum < 10000 and month == 12:
        rate = 6
    elif 100 <= begin_sum < 10000 and month == 24:
        rate = 5

    elif 10000 <= begin_sum < 100000 and month == 6:
        rate = 6
    elif 10000 <= begin_sum < 100000 and month == 12:
        rate = 7
    elif 10000 <= begin_sum < 100000 and month == 24:
        rate = 6.5

    elif 100000 <= begin_sum < 1000000 and month == 6:
        rate = 7
    elif 100000 <= begin_sum < 1000000 and month == 12:
        rate = 8
    elif 100000 <= begin_sum < 1000000 and month == 24:
        rate = 7.5

    end_sum = begin_sum + begin_sum * rate * month/100/12
    dep = {'begin_sum': begin_sum, 'end_sum': end_sum, 'month': month}
    string = f'Депозит с начальной суммой {begin_sum} на срок {month} месяцев. ' \
             f'К концу срока {end_sum}.'
    return string


print(deposit(10000, 24))


def deposit_with_capitale(begin_sum, month):
    if 100 <= begin_sum < 10000 and month == 6:
        rate = 5
    elif 100 <= begin_sum < 10000 and month == 12:
        rate = 6
    elif 100 <= begin_sum < 10000 and month == 24:
        rate = 5

    elif 10000 <= begin_sum < 100000 and month == 6:
        rate = 6
    elif 10000 <= begin_sum < 100000 and month == 12:
        rate = 7
    elif 10000 <= begin_sum < 100000 and month == 24:
        rate = 6.5

    elif 100000 <= begin_sum < 1000000 and month == 6:
        rate = 7
    elif 100000 <= begin_sum < 1000000 and month == 12:
        rate = 8
    elif 100000 <= begin_sum < 1000000 and month == 24:
        rate = 7.5

    end_sum = round(begin_sum * ((1 + rate/100/12)**month), 2)
    dep = {'begin_sum': begin_sum, 'end_sum': end_sum, 'month': month}
    string = f'Депозит с начальной суммой {begin_sum} на срок {month} месяцев. ' \
             f'К концу срока с ежемесячной капиталлизацией {end_sum}.'
    return string


print(deposit_with_capitale(10000, 24))
