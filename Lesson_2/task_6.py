"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        return print(f'Товар - {self.name}.')


class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        return print(f'Цена -  {self.price} руб.')


ob_1 = ItemDiscountReportOne('макароны', 70)
ob_1.get_info()


ob_2 = ItemDiscountReportTwo('макароны', 70)
ob_2.get_info()
