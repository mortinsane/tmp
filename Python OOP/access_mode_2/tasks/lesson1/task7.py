from string import digits, ascii_letters
from random import choice, randint


class EmailValidator:
    VALID_DATA = ascii_letters + digits + "_.@"

    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        email = (
            "".join([choice(cls.VALID_DATA) for _ in range(randint(7, 15))]).replace(
                "@", ""
            )
            + "@gmail.com"
        )
        return email

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            flag = True
            for letter in email:
                if letter not in cls.VALID_DATA:
                    flag = False

            if email.count("@") > 1 or email[email.find("@") :].count(".") != 1:
                flag = False

            if (
                len(email[: email.find("@")]) > 100
                or len(email[email.find("@") :]) > 50
            ):
                flag = False

            if email.count(".") > 1:
                point_index = email.find(".")

                if email[point_index] == email[point_index + 1]:
                    flag = False

            return flag
        return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


print(EmailValidator.get_random_email())
print(EmailValidator.check_email("sc_lib@list.ru"))  # True
print(EmailValidator.check_email("sc_lib@list_ru"))  # False
print(EmailValidator.check_email("sc.df@g.ru"))  # False
