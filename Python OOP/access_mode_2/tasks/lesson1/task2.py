class Money:
    def __init__(self, money) -> None:
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    def __check_money(self, money):
        return type(money) in (int,) and money >= 0


mn_1 = Money(10)
mn_2 = Money(20)

mn_1.set_money(100)
mn_2.add_money(mn_1)

print(mn_1.get_money())
print(mn_2.get_money())
