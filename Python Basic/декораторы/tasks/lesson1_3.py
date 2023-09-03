def decorator(func):
    def inner(*args, **kwargs):
        return sorted(func(*args, **kwargs))

    return inner


@decorator
def get_list(s):
    return list(map(int, s.split()))


lst = get_list('8 11 -5 4 3 10')
print(*lst)