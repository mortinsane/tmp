def func_show(func):
    def inner(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")

    return inner


@func_show
def get_sq(width, height):
    return width * height


get_sq(8, 11)
