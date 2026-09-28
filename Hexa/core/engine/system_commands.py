class SystemCommands:
    def __init__(self, player_profile):
        self.player = player_profile

    def run(self, command, args):
        if command == "whoami":
            return self.player.data["name"]
        if command == "sysinfo":
            return "HEXA OS v3 sandbox"
        if command == "clear":
            return ""
        return ""
