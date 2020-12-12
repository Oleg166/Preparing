"""
4. Реализовать возможность переустановки значения цены товара.

Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name):
        self.__name = name
        self.__price = 55

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'Товар - {self.get_name()}, с ценой - {self.get_price()} руб.')


ob_1 = ItemDiscountReport('макароны')
ob_1.set_price(70)
ob_1.get_parent_data()
