class Stack:
    def __init__(self) -> None:
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj
            # Если last is not None; у пока что последнего элемента
            # добавляем атрибуту next ссылку на новый объект obj
        self.last = obj  # И перезаписываем значение последнего эленмента на obj

        if self.top is None:
            self.top = obj

    def pop(self):
        head = self.top

        if head is None:
            return
        print(1)
        # Пробегаемся пока не last
        while head.next != self.last:
            head = head.next

        # Предпоследнему элементу меняем ссылку на None
        head.next = None
        last = self.last

        self.last = head

        if self.last is None:
            self.top = None

        return last

    def get_data(self):
        lst = []

        head = self.top

        if head is None:
            return lst

        lst.append(head.data)
        while head.next:
            head = head.next
            lst.append(head.data)

        return lst


class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj
