from tkinter import Canvas, Button
import json
from core.window import DraggableWindow


class RemoteDesktop:
    def __init__(self, root, target_id, player_profile=None):
        win = DraggableWindow(root, title=f"Remote Desktop - {target_id}", size="600x420",
                              taskbar=player_profile.taskbar if player_profile else None)

        files = json.load(open("data/fake_files.json")).get(target_id, [])

        canvas = Canvas(win.body, bg="#222")
        canvas.pack(fill="both", expand=True)

        y = 40
        for f in files:
            canvas.create_text(20, y, anchor="w", fill="white",
                               text=f"{f['name']} - {f['type']} - VALUE: {f['value']}cr")
            y += 30

        if player_profile is not None:
            def download():
                path = player_profile.fs.download_from_target(target_id)
                print("downloaded to", path)

            Button(win.body, text="Download to /downloads", command=download).pack(pady=5)
