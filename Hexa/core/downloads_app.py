from tkinter import Listbox, Label, END, Button
import os
import json
from core.window import DraggableWindow


class DownloadsApp:
    def __init__(self, root, player_profile):
        self.root = root
        self.player = player_profile
        self.open()

    def open(self):
        self.win = DraggableWindow(self.root, title="Data Market", size="500x350", taskbar=self.player.taskbar)

        Label(self.win.body, text="Data Market", font=("Consolas", 16)).pack(pady=10)

        self.listbox = Listbox(self.win.body)
        self.listbox.pack(fill="both", expand=True)

        self.folder = self.player.fs.downloads
        self.refresh()

        Button(self.win.body, text="Sell", command=self.sell_file).pack(pady=5)

    def refresh(self):
        self.listbox.delete(0, END)
        files = os.listdir(self.folder)
        for f in files:
            self.listbox.insert(END, f)

    def open_file(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        name = self.listbox.get(sel[0])
        path = os.path.join(self.folder, name)
        data = json.load(open(path))

        view = DraggableWindow(self.root, title=name, size="600x400", taskbar=self.player.taskbar)

        lb = Listbox(view.body)
        lb.pack(fill="both", expand=True)

        for item in data:
            lb.insert(END, f"{item['name']} - {item['type']} - VALUE {item['value']}cr")

    def sell_file(self):
        sel = self.listbox.curselection()
        if not sel:
            return

        name = self.listbox.get(sel[0])
        path = os.path.join(self.folder, name)
        data = json.load(open(path))

        total_value = sum(item["value"] for item in data)
        self.player.data["credits"] += total_value
        self.player.save()

        os.remove(path)
        self.refresh()
