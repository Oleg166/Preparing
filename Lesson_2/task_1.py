"""
Проверить механизм наследования в Python.

Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.

Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую
за отображение информации о товаре в одной строке.

Проверить работу программы.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'Товар - {self.name}, с ценой -  {self.price} руб.')


ob_1 = ItemDiscountReport('макароны', 70)
ob_1.get_parent_data()
