class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ("title", "author") and type(value) not in (str,):
            raise TypeError("Неверный тип присваиваемых данных.")

        if key in ("pages", "year") and type(value) not in (int,):
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
print(book.__dict__)
