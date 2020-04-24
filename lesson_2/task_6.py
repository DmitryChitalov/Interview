# 6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport
# на два класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в
# первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.
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
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self):
        return f'label: {self.get_name}\tprice: {self.get_price}'

    def calculate_price(self):
        price, discount = self.get_price, self.discount
        return price - price * discount / 100

    def __str__(self):
        return f'price is {self.calculate_price()}'


class NameShower(ItemDiscountReport):
    def get_info(self):
        print(f'name_info: {self.get_name}')


class PriceShower(ItemDiscountReport):
    def get_info(self):
        print(f'name_info: {self.get_price} and price with discount: {self.calculate_price()}')


a = ItemDiscount(**data)

r = ItemDiscountReport(**data, discount=15)
r.set_name('Milk')
r.set_price('233')
print(r.get_parent_data())
print(r)

info1 = NameShower(**data, discount=25)
info2 = PriceShower(**data, discount=35)
info1.get_info()
info2.get_info()
