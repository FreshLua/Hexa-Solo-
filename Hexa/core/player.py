from core.bank import BankAccount, CryptoWallet
from core.filesystem import FileSystem


class PlayerProfile:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.bank = BankAccount(data["name"], data.get("bank_balance", 0))
        self.wallet = CryptoWallet(data["name"], data.get("crypto_balance", 0))
        self.fs = FileSystem(data["name"])
        self.taskbar = None
        self.net_targets = []

    def save(self):
        import json
        SAVE_FOLDER = "saves"
        path = f"{SAVE_FOLDER}/{self.data['name']}.json"
        self.data["bank_balance"] = self.bank.balance
        self.data["crypto_balance"] = self.wallet.balance
        with open(path, "w") as f:
            json.dump(self.data, f, indent=4)
