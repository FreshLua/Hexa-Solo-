from tkinter import Listbox, Button, Label, END, messagebox
import json
from core.window import DraggableWindow


class DarkNetMarket:
    def __init__(self, root, player_profile):
        self.root = root
        self.player = player_profile
        self.open()

    def open(self):
        win = DraggableWindow(self.root, title="Tool sMarket", size="500x350", taskbar=self.player.taskbar)

        Label(win.body, text="Tool MARKET", font=("Consolas", 16)).pack(pady=10)
        Label(win.body, text=f"Credits: {self.player.data['credits']}").pack()

        upgrades = json.load(open("data/upgrades.json"))

        listbox = Listbox(win.body)
        listbox.pack(fill="both", expand=True)

        for u in upgrades:
            listbox.insert(END, f"{u['name']} - {u['cost']}cr")

        def buy():
            sel = listbox.curselection()
            if not sel:
                return
            upgrade = upgrades[sel[0]]
            if self.player.data["credits"] < upgrade["cost"]:
                messagebox.showerror("Tool Market", "Not enough credits.")
                return
            self.player.data["credits"] -= upgrade["cost"]
            for k, v in upgrade["bonus"].items():
                self.player.data[k] = self.player.data.get(k, 0) + v
            self.player.save()
            messagebox.showinfo("Tool Market", f"Purchased {upgrade['name']}")

        Button(win.body, text="Buy", command=buy).pack(pady=5)
