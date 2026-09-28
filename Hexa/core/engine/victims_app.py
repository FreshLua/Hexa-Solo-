from tkinter import Toplevel, Listbox, Button, Label, END
from core.engine.remote_desktop import RemoteDesktop


class VictimsApp:
    def __init__(self, root, player_profile, net_targets):
        self.root = root
        self.player = player_profile
        self.targets = net_targets
        self.open()

    def open(self):
        win = Toplevel(self.root)
        win.title("Victims")
        win.geometry("500x350")

        Label(win, text="VICTIMS", font=("Consolas", 16)).pack(pady=10)

        listbox = Listbox(win)
        listbox.pack(fill="both", expand=True)

        for t in self.targets:
            status = "CRACKED" if t.get("cracked") else "LOCKED"
            listbox.insert(END, f"{t['ip']} ({t['id']}) - {status}")

        def connect():
            sel = listbox.curselection()
            if not sel:
                return
            target = self.targets[sel[0]]
            if not target.get("cracked"):
                return
            RemoteDesktop(self.root, target["id"])

        Button(win, text="Connect", command=connect).pack(pady=5)
