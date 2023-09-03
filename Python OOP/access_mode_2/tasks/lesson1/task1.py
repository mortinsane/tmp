class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm):
        if type(tm) in (int,) and 0 <= tm < 100000:
            return True
        return False

    def get_time(self):
        return self.__time


clock = Clock()
clock.set_time(4530)
print(clock.get_time())

print(clock)


def foo(name: str) -> None:
    pass


foo(123)  # dsdsfsdfdsf

my_lst = [1, 2, 2, 3, 5]
