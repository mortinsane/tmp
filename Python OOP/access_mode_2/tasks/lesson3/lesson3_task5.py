class TVProgram:
    def __init__(self, program_name):
        self.name = program_name
        self.items = []

    def add_telecast(self, tl):
        if isinstance(tl, Telecast):
            self.items.append(tl)

    def remove_telecast(self, indx):
        to_remove = [item for item in self.items if item.uid == indx]

        for i in to_remove:
            self.items.remove(i)


# class TelecastValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         if type(value) in (int, str):
#             setattr(instance, self.name, value)


class Telecast:
    def __init__(self, uid, name, duration) -> None:
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__id

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(3, "Новости", 2000))
t = Telecast(2, "Интервью с Балакиревым", 20)
pr.add_telecast(t)

pr.remove_telecast(3)

print(pr.items)
