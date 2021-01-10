"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'Товар - {self.get_name()}, с ценой - {self.get_price()} руб.')


ob_1 = ItemDiscountReport('макароны', 70)
ob_1.get_parent_data()
print(f'Товар - {ob_1.get_name()}, с ценой - {ob_1.get_price()} руб.')
