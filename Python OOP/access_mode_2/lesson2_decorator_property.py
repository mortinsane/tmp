# Атрибут property


class Person1:
    def __init__(self, name, old) -> None:
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    """
        При обращении к p.old - будет вызван getter(get_old)
        При записи в p.old = 24 - будет вызван setter(set_old)

        При таком обращении не создается локальный атрибут old,
            а меняется свойство класса _Person__old

        Все дело в приоритете, если в классе задан атрибут-property,
        то в первую очередь выбирается именно оно, даже если есть
        локальный атрибут с таким же именем
    """
    old = property(fget=get_old, fset=set_old)


# p = Person("Mort", 30)
# a = p.old
# p.old = 35
# print(p.old, p.__dict__)


"""
    Единый интерфейс взаимодействия с атрибутом.

    property имеет 3 метода:
        getter()
        setter()
        deleter()

    Это ни что иное, как декораторы, их мсжно использовать при создании
    объекта-свойства.
"""


class Person2:
    def __init__(self, name, old) -> None:
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    """
        Перепишем с помощью декораторов
    """

    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)


"""
    Декоратор @property
    Перепишем с помощью синтаксического сахара)

    и избавляемся от функционального дублирования
"""


class Person3:
    def __init__(self, name, old) -> None:
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old


p = Person3("Mort", 2)
p.old = 45

print(p.old)
