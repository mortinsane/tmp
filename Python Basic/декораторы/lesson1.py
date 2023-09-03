# def func_decorator(func):
#     def wrapper():
#         print("------что то делаем перед вызовом функции------")
#         func()
#         print("------что то делаем после вызовом функции------")

#     return wrapper


# def some_func():
#     print('Вызов функции some_func')


# f = func_decorator(some_func)


# def some_func(title):
#     print(f"title={title}")


# some_func = func_decorator(some_func)
# some_func("Python forever")


# def func_decorator(func):
#     def wrapper(title):
#         print("------что то делаем перед вызовом функции------")
#         func(title)
#         print("------что то делаем после вызовом функции------")

#     return wrapper


# def some_func(title):
#     print(f"title={title}")


# some_func = func_decorator(some_func)
# some_func("Python forever")


# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("------что то делаем перед вызовом функции------")
#         func(*args, **kwargs)
#         print("------что то делаем после вызовом функции------")

#     return wrapper


# def some_func(title, tag):
#     print(f"title={title}, tag={tag}")


# some_func = func_decorator(some_func)
# some_func('Python forever', 'h1')

# def some_func(title, tag):
#     print(f"title={title}, tag={tag}")
#     return f'<{tag}>{title}</{tag}>'


# some_func = func_decorator(some_func)
# print(some_func('Python forever', 'h1'))


def some_func(title, tag):
    print(f"title={title}, tag={tag}")
    return f"<{tag}>{title}</{tag}>"


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("------ что-то делаем перед вызовом функции ------")
        res = func(*args, **kwargs)
        print("------ что-то делаем после вызова функции ------")
        return res

    return wrapper


some_func = func_decorator(some_func)
print(some_func("Python forever", "h1"))
