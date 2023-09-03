class InputValues:
    def __init__(
        self, render
    ):  # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func, *args, **kwargs):  # ссылка на декорируемую функцию
        def inner(*args, **kwargs):
            return list(map(self.render, func(*args, **kwargs).split()))

        return inner


class RenderDigit:
    def __call__(self, string, *args, **kwargs):
        try:
            return int(string)
        except:
            return None


render = RenderDigit()

input_dg = InputValues(render)(input)
res = input_dg()
print(res)
