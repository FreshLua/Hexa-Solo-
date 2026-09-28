from tkinter import Listbox, Text, Label, END
import json
from core.window import DraggableWindow


class ScamDashboard:
    def __init__(self, root, player_profile):
        self.root = root
        self.player = player_profile
        self.open()

    def open(self):
        win = DraggableWindow(self.root, title="Scam Dashboard", size="700x500", taskbar=self.player.taskbar)

        Label(win.body, text="SCAM DASHBOARD", font=("Consolas", 18)).pack(pady=10)

        victims = json.load(open("data/fake_victims.json"))

        listbox = Listbox(win.body)
        listbox.pack(fill="both", expand=True)

        for v in victims:
            listbox.insert(END, f"{v['name']} - Risk {int(v['risk'] * 100)}%")

        stats = Text(win.body, height=8, bg="#111", fg="#00ff00")
        stats.pack(fill="x")

        stats.insert("end", f"Crypto Wallet: {self.player.wallet.balance} CR\n")
        stats.insert("end", f"Bank Balance: {self.player.bank.balance} CR\n")
        stats.insert("end", f"Successful Scams: {self.player.data.get('scams', 0)}\n")
