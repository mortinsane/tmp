class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__checker(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__checker(height):
            self.__height = height
            self.show()

    @classmethod
    def __checker(cls, value):
        return type(value) in (int,) and value in range(0, 10001)
