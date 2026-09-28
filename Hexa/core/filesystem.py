import os
import json


class FileSystem:
    def __init__(self, player_name):
        self.root = f"player_fs/{player_name}"
        self.downloads = os.path.join(self.root, "downloads")
        os.makedirs(self.downloads, exist_ok=True)

    def download_from_target(self, target_id):
        data = json.load(open("data/fake_files.json")).get(target_id, [])
        path = os.path.join(self.downloads, f"{target_id}_loot.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return path
