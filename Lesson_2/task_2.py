"""
2. Инкапсулировать оба параметра (название и цену)
товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы
будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'Товар - {self._name}, с ценой -  {self._price} руб.')


ob_1 = ItemDiscountReport('макароны', 70)
ob_1.get_parent_data()
