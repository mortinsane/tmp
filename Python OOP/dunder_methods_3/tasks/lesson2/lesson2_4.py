class DigitRetrive:
    DIGITS = "0123456789"

    @classmethod
    def is_valid(cls, value):
        if "-" in value:
            for digit in value[1:]:
                if digit not in cls.DIGITS:
                    return None
        else:
            for digit in value:
                if digit not in cls.DIGITS:
                    return None
        return int(value)

    def __call__(self, string, *args, **kwargs):
        return self.is_valid(string)


dg = DigitRetrive()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]

print(digits)
