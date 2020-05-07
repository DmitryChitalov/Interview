# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.

data = dict(name='Bred', price=12)


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'label: {self.__name}\tprice: {self.__price}'


a = ItemDiscount(**data)

r = ItemDiscountReport(**data)
print(r.get_parent_data())
