class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        ext = args[0].split(".")[-1]
        return ext in self.extensions


filenames = [
    "boat.jpg",
    "web.png",
    "text.txt",
    "python.doc",
    "ava.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.png",
]

# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

fs = [
    "boat.jpg",
    "web.png",
    "text.txt",
    "python.doc",
    "ava.8.jpg",
    "forest.jpeg",
    "eq_1.png",
    "eq_2.png",
    "my.html",
    "data.shtml",
    "qwehtml.html",
]
acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
print(set(res))
