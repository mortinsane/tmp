class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        to_remove = [m_indx for m_indx, _ in enumerate(self.modules) if m_indx == indx]

        for module in to_remove:
            self.modules.pop(module)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        to_remove = [m_indx for m_indx, _ in enumerate(self.lessons) if m_indx == indx]

        for module in to_remove:
            self.lessons.pop(module)


class LessonItem:
    __attrs = {
        "title": lambda value: isinstance(value, str),
        "practices": lambda value: isinstance(value, int) and value > 0,
        "duration": lambda value: isinstance(value, int) and value > 0,
    }

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.__attrs and not self.__attrs[key](value):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(selv, item):
        return False

    def __delattr__(self, item) -> None:
        if item in ("title", "practices", "duration"):
            raise AttributeError(f"Нельзя удалить атрибут {item}")
        object.__delattr__(self, item)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
