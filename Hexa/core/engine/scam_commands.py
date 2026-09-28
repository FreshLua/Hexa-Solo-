import random
import json
import os
from core.engine.remote_desktop import RemoteDesktop
from core.crack_popup import CrackPopup


class ScamCommands:
    def __init__(self, player_profile):
        self.player = player_profile
        self.victims = json.load(open("data/fake_victims.json"))
        self.net_targets = []

    def attach_net_targets(self, targets):
        self.net_targets = targets
        self.player.net_targets = targets

    def run(self, command, args):
        if command == "phish":
            victim = random.choice(self.victims)
            base = victim["risk"]
            bonus = self.player.data.get("social_power", 0) * 0.05
            chance = min(0.95, base + bonus)
            if random.random() <= chance:
                amount = random.randint(10, 200)
                self.player.wallet.receive(amount)
                self.player.data["scams"] = self.player.data.get("scams", 0) + 1
                self.player.save()
                return f"{victim['name']} fell for simulated scam. +{amount} CRYPTO"
            return f"{victim['name']} ignored simulated scam."

        if command == "scamlink":
            return "generated fake scam link: https://hexasandbox/fake"

        if command == "hackdesk":
            RemoteDesktop(self.player.root, "alpha_server", self.player)
            return "opened remote desktop (simulated)"

        if command == "crack":
            if not self.net_targets:
                return "no scanned targets. run 'nmap' first."
            target = self.net_targets[0]
            CrackPopup(self.player.root, target)
            return f"started crack on {target['ip']}"

        if command == "sell":
            folder = self.player.fs.downloads
            files = os.listdir(folder)
            if not files:
                return "no files to sell"

            name = files[0]
            path = os.path.join(folder, name)
            data = json.load(open(path))

            total_value = sum(item["value"] for item in data)
            self.player.data["credits"] += total_value
            self.player.save()

            os.remove(path)
            return f"sold {name} for {total_value}cr"

        return ""
