class InputDigits:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, *args, **kwargs):
        return list(map(int, self.__fn().split()))


input_dg = InputDigits(input)
res = input_dg()  # 12 -5 10 83

print(res)
