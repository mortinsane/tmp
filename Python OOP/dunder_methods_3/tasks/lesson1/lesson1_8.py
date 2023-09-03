import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    slots = dict([[1, None], [2, None], [3, None]])

    def add_filter(self, slot_num, filter):
        if self.slots[slot_num] is None:
            if slot_num == 1 and isinstance(filter, Mechanical):
                self.slots[slot_num] = filter

            if slot_num == 2 and isinstance(filter, Aragon):
                self.slots[slot_num] = filter

            if slot_num == 3 and isinstance(filter, Calcium):
                self.slots[slot_num] = filter

    def remove_filter(self, slot_num):
        if self.slots[slot_num] is not None:
            self.slots[slot_num] = None

    def get_filters(self):
        return tuple(self.slots.values())

    def water_on(self):
        flag = False
        if all(self.get_filters()) and all(
            0 <= (time.time() - v.date) <= self.MAX_DATE_FILTER
            for _, v in self.slots.items()
        ):
            flag = True

        return flag


class Mechanical:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if self.__date is None:
            self.__date = value


class Aragon:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if self.__date is None:
            self.__date = value


class Calcium:
    def __init__(self, date):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if self.__date is None:
            self.__date = value
