class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        # if app.name not in [a.name for a in self.apps]:

        # if len(tuple(filter(lambda x: type(x) == type(app), self.apps))) == 0:
        if type(app) not in map(type, self.apps):
            self.apps.append(app)

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory_max=1024):
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list={}):
        self.name = "Phone"
        self.phone_list = phone_list.copy()


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())


# второй раз добавляться не должно
sm.add_app(AppYouTube(2048))

for a in sm.apps:
    print(a.name)
