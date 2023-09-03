class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError(f"недопустимое имя атрибута: {key}")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__")


p = Point(1, 1)
p.t = 15

del p.t
