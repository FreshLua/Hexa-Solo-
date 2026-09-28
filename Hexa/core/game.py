import os
import json
from tkinter import Toplevel, Listbox, Button, Label, END, messagebox, simpledialog
from core.desktop import HexaDesktop

SAVE_FOLDER = "saves"
os.makedirs(SAVE_FOLDER, exist_ok=True)


class HexaGame:
    def __init__(self, root):
        self.root = root
        root.title("HEXA v3")
        root.geometry("1200x700")
        root.configure(bg="#0a0a0a")
        self.build()

    def build(self):
        Label(self.root, text="HEXA", font=("Consolas", 36, "bold"),
              bg="#0a0a0a", fg="#00ff00").place(x=60, y=50)

        Button(self.root, text="NEW SAVE", width=20, command=self.new_save).place(x=60, y=200)
        Button(self.root, text="LOAD SAVE", width=20, command=self.load_save).place(x=60, y=250)
        Button(self.root, text="EXIT", width=20, command=self.root.destroy).place(x=60, y=300)

    def new_save(self):
        name = simpledialog.askstring("New Save", "Operator Name")
        if not name:
            return

        data = {
            "name": name,
            "xp": 0,
            "credits": 250,
            "rank": "Novice",
            "hack_power": 0,
            "social_power": 0,
            "stealth": 0,
            "bank_balance": 0,
            "crypto_balance": 0,
            "scams": 0
        }

        with open(f"{SAVE_FOLDER}/{name}.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("HEXA", "Save Created")

    def load_save(self):
        saves = [f.replace(".json", "") for f in os.listdir(SAVE_FOLDER) if f.endswith(".json")]
        if not saves:
            messagebox.showerror("HEXA", "No saves found")
            return

        win = Toplevel(self.root)
        win.title("Load Save")

        listbox = Listbox(win)
        listbox.pack(fill="both", expand=True)

        for s in saves:
            listbox.insert(END, s)

        def load_player():
            sel = listbox.curselection()
            if not sel:
                return
            name = listbox.get(sel[0])

            with open(f"{SAVE_FOLDER}/{name}.json") as f:
                player = json.load(f)

            win.destroy()
            HexaDesktop(self.root, player)

        Button(win, text="Load", command=load_player).pack()
