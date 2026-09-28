from tkinter import Canvas
from core.ui.theme import HexaTheme


class Wallpaper:
    def __init__(self, root, canvas: Canvas):
        self.root = root
        self.canvas = canvas
        self.theme = HexaTheme()

    def draw_gradient(self):
        w = self.canvas.winfo_width() or 1200
        h = self.canvas.winfo_height() or 700
        steps = 64
        r1, g1, b1 = self._hex_to_rgb(self.theme.desktop_bg_top)
        r2, g2, b2 = self._hex_to_rgb(self.theme.desktop_bg_bottom)
        for i in range(steps):
            ratio = i / steps
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            y1 = int(h * (i / steps))
            y2 = int(h * ((i + 1) / steps))
            self.canvas.create_rectangle(0, y1, w, y2, outline="", fill=color)

    def _hex_to_rgb(self, hx):
        hx = hx.lstrip("#")
        return int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
