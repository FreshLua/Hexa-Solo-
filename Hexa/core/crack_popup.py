from tkinter import Toplevel, Label, Canvas
import random


class CrackPopup:
    def __init__(self, root, target):
        self.root = root
        self.target = target
        self.win = Toplevel(root)
        self.win.title(f"Cracking {target['ip']}")
        self.win.geometry("400x140")
        self.progress = 0

        Label(self.win, text=f"Cracking {target['ip']} ({target['id']})").pack(pady=10)

        self.canvas = Canvas(self.win, width=360, height=24, bg="#111")
        self.canvas.pack(pady=10)
        self.bar = self.canvas.create_rectangle(2, 2, 2, 22, fill="#00ff00")

        self.label = Label(self.win, text="0%")
        self.label.pack()

        self.tick()

    def tick(self):
        if self.progress >= 100:
            self.label.config(text="100% - Crack complete")
            self.target["cracked"] = True
            return
        step = random.randint(3, 12)
        self.progress = min(100, self.progress + step)
        width = int(3.6 * self.progress)
        self.canvas.coords(self.bar, 2, 2, 2 + width, 22)
        self.label.config(text=f"{self.progress}%")
        self.root.after(200, self.tick)
