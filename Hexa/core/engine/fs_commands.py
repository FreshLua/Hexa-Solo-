class FSCommands:
    def __init__(self, player_profile):
        self.player = player_profile
        self.cwd = "/"

    def run(self, command, args):
        if command == "ls":
            return "desktop documents downloads"
        if command == "cd":
            if args:
                self.cwd = args[0]
            return f"cwd: {self.cwd}"
        if command == "cat":
            if not args:
                return "file?"
            return f"reading {args[0]} (simulated)"
        if command == "scanfs":
            return "filesystem scan complete (simulated)"
        return ""
