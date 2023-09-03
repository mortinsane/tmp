class Shop:
    """
    Класс для управления магазином
    """

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    __ID_START = 1
    attrs = {"id": int, "name": str, "weight": int, "price": int}

    def __init__(self, name, weight, price):
        self.id = Product.__ID_START
        Product.__ID_START += 1

        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.attrs and self.attrs[key] == type(value):
            if type(value) is int and value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.attrs:
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id} {p.name}, {p.weight}, {p.price}")
