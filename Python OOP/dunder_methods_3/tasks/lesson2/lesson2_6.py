class HandlerGET:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, request, *args, **kwargs):

        if request.get("method", "GET") == "GET":
            return self.get(self.__fn, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


# print(contact("wqe"))
res = contact({"method": "GET", "url": "contact.html"})

print(res)
