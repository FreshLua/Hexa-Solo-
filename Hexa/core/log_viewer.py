from tkinter import Text, Label
import os
from core.window import DraggableWindow


LOG_PATH = "logs/hexa.log"


class LogViewer:
    def __init__(self, root, player_profile):
        self.root = root
        self.player = player_profile
        self.open()

    def open(self):
        win = DraggableWindow(self.root, title="Log Viewer", size="700x400",
                              taskbar=self.player.taskbar)

        Label(win.body, text="SYSTEM LOGS", font=("Consolas", 16)).pack(pady=8)

        txt = Text(win.body, bg="#111", fg="#00ff00", insertbackground="#00ff00")
        txt.pack(fill="both", expand=True)

        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                txt.insert("end", f.read())
        else:
            txt.insert("end", "No logs found.\n\nExpected at: " + LOG_PATH)
