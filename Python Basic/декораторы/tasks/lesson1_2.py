def show_menu(func):
    def inner(*args, **kwargs):
        [print(f"{num}. {val}") for num, val in enumerate(func(*args, **kwargs), 1)]

    return inner


@show_menu
def get_menu(s):
    return s.split()


