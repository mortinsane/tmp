class StringValue:
    MIN_LENGTH = 2
    MAX_LENGTH = 50

    def __init__(self, min_length=0, max_length=0):
        self.min_length = min_length
        self.max_length = max_length

    @classmethod
    def verify(cls, value):
        return type(value) in (str,) and len(value) in range(
            cls.MIN_LENGTH, cls.MAX_LENGTH + 1
        )

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.name, value)


class PriceValue:
    MAX_VALUE = 10000

    def __init__(self, max_value=0):
        self.max_value = max_value

    @classmethod
    def verify(cls, value):
        return type(value) in (int, float) and value in range(0, cls.MAX_VALUE + 1)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
