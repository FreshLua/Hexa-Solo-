from tkinter import Text, Entry, END
from core.window import DraggableWindow
from core.engine.command_router import CommandRouter


class TerminalWindow:
    def __init__(self, root, player_profile):
        self.player_profile = player_profile
        self.username = player_profile.data["name"]

        win = DraggableWindow(root, title="Terminal", size="900x550",
                              taskbar=player_profile.taskbar)

        self.output = Text(
            win.body,
            bg="#000000",
            fg="#00ff00",
            insertbackground="#00ff00",
            font=("Consolas", 12),
            wrap="word"
        )
        self.output.pack(fill="both", expand=True)

        self.entry = Entry(
            win.body,
            bg="#1a1a1a",
            fg="#ffffff",
            font=("Consolas", 12)
        )
        self.entry.pack(fill="x")

        self.router = CommandRouter(player_profile)

        self.history = []
        self.history_index = -1

        self.commands = [
            "help", "ls", "cd", "cat", "scanfs",
            "ssh", "netstat", "ping", "trace", "spoof", "nmap",
            "phish", "scamlink", "crack", "hackdesk", "sell",
            "wallet", "bank", "crypto",
            "whoami", "sysinfo", "clear"
        ]

        self.entry.bind("<Return>", self.run_command)
        self.entry.bind("<Up>", self.history_up)
        self.entry.bind("<Down>", self.history_down)
        self.entry.bind("<Tab>", self.autocomplete)

        self.output.insert("end", "TYPE 'help' FOR COMMANDS.\n\n")

    # --------------------------
    # Command Execution
    # --------------------------
    def run_command(self, event=None):
        cmd = self.entry.get().strip()
        if not cmd:
            self.entry.delete(0, END)
            return

        self.history.append(cmd)
        self.history_index = len(self.history)

        prefix = f"[{self.username}\\{cmd}]"
        self.output.insert("end", prefix + "\n", "prefix")

        result = self.router.execute(cmd)

        if result.strip() == "":
            self.output.insert("end", "\n")
        else:
            self.output.insert("end", result + "\n\n", "output")

        self.output.see("end")
        self.entry.delete(0, END)

    # --------------------------
    # Command History
    # --------------------------
    def history_up(self, event=None):
        if not self.history:
            return
        self.history_index = max(0, self.history_index - 1)
        self.entry.delete(0, END)
        self.entry.insert(0, self.history[self.history_index])

    def history_down(self, event=None):
        if not self.history:
            return
        self.history_index = min(len(self.history), self.history_index + 1)
        self.entry.delete(0, END)
        if self.history_index < len(self.history):
            self.entry.insert(0, self.history[self.history_index])

    # --------------------------
    # Auto-complete
    # --------------------------
    def autocomplete(self, event=None):
        text = self.entry.get().strip()
        if not text:
            return "break"

        matches = [c for c in self.commands if c.startswith(text)]
        if len(matches) == 1:
            self.entry.delete(0, END)
            self.entry.insert(0, matches[0])

        return "break"
