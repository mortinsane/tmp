class Bag:
    def __init__(self, max_weght=0):
        self.max_weght = max_weght
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        adding = self.get_total_weight() + thing.weight

        if adding <= self.max_weght:
            self.things.append(thing)

    def remove_thing(self, thing):
        if thing in self.things:
            self.things.remove(thing)

    def get_total_weight(self):
        return sum(thing.weight for thing in self.things)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
