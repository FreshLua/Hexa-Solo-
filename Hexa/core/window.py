from tkinter import Toplevel, Frame, Button
from core.ui.theme import HexaTheme


class DraggableWindow(Toplevel):
    def __init__(self, root, title="Window", size="600x400", taskbar=None):
        super().__init__(root)
        self.theme = HexaTheme()
        self.title(title)
        self.geometry(size)
        self.overrideredirect(True)

        self._offset_x = 0
        self._offset_y = 0
        self._fullscreen = False
        self._normal_geometry = size
        self._taskbar = taskbar

        self.configure(bg=self.theme.window_shadow)
        self.frame = Frame(self, bg=self.theme.window_border, bd=1)
        self.frame.pack(fill="both", expand=True, padx=3, pady=3)

        self.titlebar = Frame(
            self.frame,
            bg=self.theme.window_title_top,
            height=26
        )
        self.titlebar.pack(fill="x")

        self.titlebar.bind("<ButtonPress-1>", self.start_move)
        self.titlebar.bind("<B1-Motion>", self.do_move)

        self.btn_close = Button(
            self.titlebar,
            text="✕",
            bg=self.theme.accent_red,
            fg=self.theme.text_inverse,
            bd=0,
            width=3,
            command=self.close
        )
        self.btn_close.pack(side="right", padx=(0, 2))

        self.btn_max = Button(
            self.titlebar,
            text="⬜",
            bg=self.theme.window_title_bottom,
            fg=self.theme.text_inverse,
            bd=0,
            width=3,
            command=self.toggle_fullscreen
        )
        self.btn_max.pack(side="right")

        self.btn_min = Button(
            self.titlebar,
            text="—",
            bg=self.theme.window_title_bottom,
            fg=self.theme.text_inverse,
            bd=0,
            width=3,
            command=self.minimize
        )
        self.btn_min.pack(side="right")

        self.body = Frame(self.frame, bg=self.theme.window_body_bg)
        self.body.pack(fill="both", expand=True)

        if taskbar:
            taskbar.register(self, title)

    def start_move(self, event):
        if self._fullscreen:
            return
        self._offset_x = event.x_root - self.winfo_x()
        self._offset_y = event.y_root - self.winfo_y()

    def do_move(self, event):
        if self._fullscreen:
            return
        x = event.x_root - self._offset_x
        y = event.y_root - self._offset_y
        self.geometry(f"+{x}+{y}")

    def close(self):
        # ensure taskbar entry is removed too
        if self._taskbar is not None:
            try:
                self._taskbar.close(self)
                return
            except:
                pass
        try:
            self.destroy()
        except:
            pass

    def minimize(self):
        self.withdraw()

    def toggle_fullscreen(self):
        if not self._fullscreen:
            self._normal_geometry = self.geometry()
            w = self.master.winfo_width()
            h = self.master.winfo_height()
            self.geometry(f"{w}x{h}+0+0")
            self._fullscreen = True
        else:
            self.geometry(self._normal_geometry)
            self._fullscreen = False
