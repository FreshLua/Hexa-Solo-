from tkinter import Toplevel, Frame, Button
from core.ui.theme import HexaTheme


class StartMenu:
    def __init__(self, root, launchers):
        self.root = root
        self.launchers = launchers
        self.theme = HexaTheme()
        self.win = None

    def toggle(self, x, y):
        if self.win and self.win.winfo_exists():
            self.win.destroy()
            self.win = None
            return
        self.win = Toplevel(self.root)
        self.win.overrideredirect(True)
        self.win.geometry(f"220x320+{x}+{y-320}")
        frame = Frame(self.win, bg=self.theme.window_body_bg, bd=1,
                      highlightbackground=self.theme.window_border,
                      highlightthickness=1)
        frame.pack(fill="both", expand=True)
        for label, fn in self.launchers:
            btn = Button(frame, text=label, anchor="w",
                         bg="#d5d8dd", fg=self.theme.text_primary,
                         bd=0, padx=10, command=fn)
            btn.pack(fill="x", pady=2)
