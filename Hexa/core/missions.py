from tkinter import Listbox, Button, Label, END, messagebox
import json
from core.window import DraggableWindow


class MissionHub:
    def __init__(self, root, player_profile):
        self.root = root
        self.player = player_profile
        self.open()

    def open(self):
        win = DraggableWindow(self.root, title="Mission Hub", size="500x350", taskbar=self.player.taskbar)

        Label(win.body, text="MISSIONS", font=("Consolas", 16)).pack(pady=10)

        missions = json.load(open("data/missions.json"))

        listbox = Listbox(win.body)
        listbox.pack(fill="both", expand=True)

        for m in missions:
            listbox.insert(END, f"{m['name']} [{m['difficulty']}]")

        def launch():
            sel = listbox.curselection()
            if not sel:
                return
            mission = missions[sel[0]]
            self.run_mission(mission)

        Button(win.body, text="Launch", command=launch).pack(pady=5)

    def run_mission(self, mission):
        base = {"Easy": 75, "Medium": 55, "Hard": 40}.get(mission["difficulty"], 50)
        bonus = self.player.data.get("hack_power", 0) * 10 + self.player.data.get("stealth", 0) * 5
        import random
        chance = min(95, base + bonus)
        roll = random.randint(1, 100)
        if roll <= chance:
            self.player.data["credits"] += mission["reward_credits"]
            self.player.data["xp"] += mission["reward_xp"]
            messagebox.showinfo("Mission", f"{mission['name']} SUCCESS\n+{mission['reward_credits']} cr\n+{mission['reward_xp']} xp")
            self.player.save()
        else:
            messagebox.showwarning("Mission", f"{mission['name']} FAILED\nNo rewards.")
