class CryptoCommands:
    def __init__(self, player_profile):
        self.player = player_profile

    def run(self, command, args):
        if command == "wallet":
            return f"Crypto Wallet: {self.player.wallet.balance} CR"
        if command == "bank":
            return f"Bank Balance: {self.player.bank.balance} CR"
        if command == "crypto":
            return "crypto market: simulated prices only"
        return ""
