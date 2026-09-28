from tkinter import Frame, Button
from core.ui.theme import HexaTheme


class Taskbar:
    def __init__(self, root):
        self.theme = HexaTheme()
        self.root = root
        self.frame = Frame(root, bg=self.theme.taskbar_bg, height=36, bd=1,
                           highlightbackground=self.theme.taskbar_border,
                           highlightthickness=1)
        self.frame.pack(side="bottom", fill="x")
        self.windows = {}

    def register(self, win, title):
        btn = Button(
            self.frame,
            text=title,
            bg=self.theme.taskbar_button_bg,
            fg=self.theme.text_inverse,
            bd=0,
            padx=10,
            command=lambda w=win: self.focus(w)
        )
        btn.pack(side="left", padx=4, pady=2)
        self.windows[win] = btn

        # ensure OS close also cleans taskbar
        win.protocol("WM_DELETE_WINDOW", lambda w=win: self.close(w))

    def focus(self, win):
        try:
            win.deiconify()
            win.lift()
        except:
            pass

    def close(self, win):
        try:
            if win in self.windows:
                self.windows[win].destroy()
                del self.windows[win]
        except:
            pass
        try:
            win.destroy()
        except:
            pass
