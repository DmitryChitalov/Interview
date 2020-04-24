# 5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента
# в дочерний класс. Выполнить перегрузку методов конструктора дочернего класса (метод init, в который должна
# передаваться переменная — скидка), и перегрузку метода str дочернего класса. В этом методе должна пересчитываться
# цена и возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
# дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).

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


a = ItemDiscount(**data)

r = ItemDiscountReport(**data, discount=15)
r.set_name('Milk')
r.set_price('233')
print(r.get_parent_data())
print(r)
