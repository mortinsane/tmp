class Car:
    def __init__(self, model) -> None:
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check_value(model):
            self.__model = model

    @classmethod
    def __check_value(cls, model):
        return isinstance(model, str) and 2 <= len(model) <= 100
