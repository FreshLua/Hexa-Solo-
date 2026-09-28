from core.engine.help import help_text
from core.engine.fs_commands import FSCommands
from core.engine.net_commands import NetCommands
from core.engine.scam_commands import ScamCommands
from core.engine.crypto_commands import CryptoCommands
from core.engine.system_commands import SystemCommands


class CommandRouter:
    def __init__(self, player_profile):
        self.fs = FSCommands(player_profile)
        self.net = NetCommands(player_profile)
        self.scam = ScamCommands(player_profile)
        self.crypto = CryptoCommands(player_profile)
        self.sys = SystemCommands(player_profile)

    def execute(self, cmd):
        parts = cmd.split()
        if not parts:
            return ""
        command = parts[0].lower()
        args = parts[1:]

        if command == "help":
            return help_text()

        if command in ["ls", "cd", "cat", "scanfs"]:
            return self.fs.run(command, args)

        if command in ["ssh", "netstat", "ping", "trace", "spoof", "nmap"]:
            result = self.net.run(command, args)
            if command == "nmap":
                self.scam.attach_net_targets(self.net.targets)
            return result

        if command in ["phish", "scamlink", "hackdesk", "sell", "crack"]:
            return self.scam.run(command, args)

        if command in ["wallet", "bank", "crypto"]:
            return self.crypto.run(command, args)

        if command in ["whoami", "sysinfo", "clear"]:
            return self.sys.run(command, args)

        return "UNKNOWN COMMAND"
