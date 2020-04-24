# 4.Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский, и дочерний
# классы получили новое значение цены. Следует проверить это, вызвав соответствующий метод родительского класса
# и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).
data = dict(name='Bred', price=42)


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        try:
            if int(new_price) > 0:
                old = self.__price
                self.__price = int(new_price)
                print(f'{self.get_name} price was changed from {old} to {self.get_price}')
        except ValueError:
            print(f'Wrong format of price: {new_price}\ttype: {type(new_price)}')


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_parent_data(self):
        return f'label: {self.get_name}\tprice: {self.get_price}'


a = ItemDiscount(**data)

r = ItemDiscountReport(**data)
r.set_name('Milk')
r.set_price('232a')
print(r.get_parent_data())
