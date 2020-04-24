# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.

data = dict(name='Bred', price=12)


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'label: {self.name}\tprice: {self.price}'


a = ItemDiscount(**data)


r = ItemDiscountReport(**a.__dict__)
print(r.get_parent_data())














# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
# на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в
# первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.