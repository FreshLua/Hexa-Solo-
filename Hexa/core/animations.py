import random


class DesktopAnimator:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas
        self.particles = []
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            self.tick()

    def tick(self):
        if not self.running:
            return
        w = self.canvas.winfo_width() or 1200
        h = self.canvas.winfo_height() or 700
        x = random.randint(0, w)
        y = random.randint(0, h)
        dot = self.canvas.create_oval(x, y, x + 2, y + 2, fill="#00ff00", outline="")
        self.particles.append(dot)
        if len(self.particles) > 120:
            self.canvas.delete(self.particles.pop(0))
        self.root.after(80, self.tick)
