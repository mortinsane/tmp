class RenderList:
    def __init__(self, type_list=None):
        if type_list not in ("ul", "ol"):
            self.type_list = "ul"
        else:
            self.type_list = type_list

    def __call__(self, lst, *args, **kwarags):
        s = f"<{self.type_list}>\n"
        for row in lst:
            s += f"<li>{row}</li>\n"
        s += f"</{self.type_list}>"
        return s


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList()
html = render(lst)

print(html)
