class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    @classmethod
    def verify(cls, value):
        return isinstance(value, (int, float))

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if not self.verify(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
