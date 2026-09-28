from PIL import Image, ImageTk


class IconSet:
    def __init__(self):
        self.cache = {}

    def load(self, path, size=(64, 64)):
        key = (path, size)
        if key in self.cache:
            return self.cache[key]
        try:
            img = Image.open(path).resize(size)
            tk_img = ImageTk.PhotoImage(img)
            self.cache[key] = tk_img
            return tk_img
        except Exception:
            return None
