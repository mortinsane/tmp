class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0) -> None:
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__checker(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__checker(value):
            self.__y = value

    @classmethod
    def __checker(cls, value):
        return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)
