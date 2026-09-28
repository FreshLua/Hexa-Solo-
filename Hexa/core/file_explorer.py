from tkinter import Frame, Listbox, Button, Label, END
import os
from core.window import DraggableWindow


class FileExplorer:
    def __init__(self, root, player_profile, start_path=None):
        self.root = root
        self.player = player_profile
        self.base = start_path or self.player.fs.root
        self.current = self.base
        self.open()

    def open(self):
        self.win = DraggableWindow(self.root, title="File Explorer", size="800x450",
                                   taskbar=self.player.taskbar)

        Label(self.win.body, text=f"EXPLORER - {self.current}", font=("Consolas", 12)).pack(pady=4)

        top = Frame(self.win.body)
        top.pack(fill="both", expand=True)

        self.dir_list = Listbox(top)
        self.dir_list.pack(side="left", fill="y")

        self.file_list = Listbox(top)
        self.file_list.pack(side="right", fill="both", expand=True)

        btn_bar = Frame(self.win.body)
        btn_bar.pack(fill="x", pady=4)

        Button(btn_bar, text="Up", command=self.go_up).pack(side="left", padx=4)
        Button(btn_bar, text="Open Folder", command=self.open_folder).pack(side="left", padx=4)
        Button(btn_bar, text="Open File", command=self.open_file).pack(side="left", padx=4)
        Button(btn_bar, text="Delete File", command=self.delete_file).pack(side="left", padx=4)

        self.refresh()

    def refresh(self):
        self.dir_list.delete(0, END)
        self.file_list.delete(0, END)

        try:
            entries = os.listdir(self.current)
        except FileNotFoundError:
            entries = []

        dirs = [e for e in entries if os.path.isdir(os.path.join(self.current, e))]
        files = [e for e in entries if os.path.isfile(os.path.join(self.current, e))]

        for d in dirs:
            self.dir_list.insert(END, d)

        for f in files:
            self.file_list.insert(END, f)

    def go_up(self):
        if self.current == self.base:
            return
        self.current = os.path.dirname(self.current)
        self.refresh()

    def open_folder(self):
        sel = self.dir_list.curselection()
        if not sel:
            return
        name = self.dir_list.get(sel[0])
        path = os.path.join(self.current, name)
        if os.path.isdir(path):
            self.current = path
            self.refresh()

    def open_file(self):
        sel = self.file_list.curselection()
        if not sel:
            return
        name = self.file_list.get(sel[0])
        path = os.path.join(self.current, name)

        win = DraggableWindow(self.root, title=name, size="600x400",
                              taskbar=self.player.taskbar)

        from tkinter import Text
        txt = Text(win.body, bg="#111", fg="#00ff00", insertbackground="#00ff00")
        txt.pack(fill="both", expand=True)

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                txt.insert("end", f.read())
        except Exception as e:
            txt.insert("end", f"Cannot open file:\n{e}")

    def delete_file(self):
        sel = self.file_list.curselection()
        if not sel:
            return
        name = self.file_list.get(sel[0])
        path = os.path.join(self.current, name)
        try:
            os.remove(path)
        except Exception:
            pass
        self.refresh()
