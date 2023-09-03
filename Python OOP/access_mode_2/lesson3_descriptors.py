# Проблема функционального дублирования
class Point3D1:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int,):
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


# p = Point3D1(1,2,3)

# print(p.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}


class Integer1:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int,):
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        """
        owner - ссылка на класс из которого вызывается
        name - имя локальной переменной
        """

        self.name = "_" + name

    def __get__(self, instance, owner):
        """
        instance - ссылка на экземпляр класса
        owner - ссылка на класс из которого вызывается
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        instance - ссылка на экземпляр класса
        value - значение для присваивания
        """
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class Point3D2:
    x = Integer1()
    y = Integer1()
    z = Integer1()

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


# p = Point3D2(1, 2, 3)
# print(p.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}


class Integer2:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int,):
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        """
        owner - ссылка на класс из которого вызывается
        name - имя локальной переменной
        """

        self.name = "_" + name

    def __get__(self, instance, owner):
        """
        instance - ссылка на экземпляр класса
        owner - ссылка на класс из которого вызывается
        """
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """
        instance - ссылка на экземпляр класса
        value - значение для присваивания
        """
        self.verify_coord(value)
        setattr(instance, self.name, value)


class Point3D3:
    x = Integer2()
    y = Integer2()
    z = Integer2()

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


p = Point3D3(1, 2, 3)
print(p.__dict__)


def foo(name: str) -> None:
    print(name)


print(foo(123))
