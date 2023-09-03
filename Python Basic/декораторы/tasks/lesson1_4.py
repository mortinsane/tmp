def decorator(func):
    def inner(*args, **kwargs):
        a, b = func(*args, **kwargs)
        return dict(zip(a, b))

    return inner


@decorator
def to_list(s, s2):
    return s.split(), s2.split()


print(to_list(input(), input()))
