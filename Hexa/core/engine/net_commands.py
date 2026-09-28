import random


class NetCommands:
    def __init__(self, player_profile):
        self.player = player_profile
        self.targets = []

    def run(self, command, args):
        if command == "ssh":
            target = args[0] if args else "alpha_server"
            return f"ssh connection to {target} (simulated)"

        if command == "netstat":
            return "tcp 0.0.0.0:22\ntcp 0.0.0.0:80\nudp 0.0.0.0:53"

        if command == "ping":
            host = args[0] if args else "training_node"
            return f"ping {host}: {random.randint(10, 80)}ms"

        if command == "trace":
            return "trace: risk medium (simulated)"

        if command == "spoof":
            return "identity spoofed as admin@corp.local (simulated)"

        if command == "nmap":
            return self.scan_networks()

        return ""

    def scan_networks(self):
        self.targets = []
        count = random.randint(3, 6)
        out = "scanning networks...\n\n"
        for _ in range(count):
            ip = f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
            tag = random.choice(["alpha_server", "research_node", "beta_core"])
            self.targets.append({"ip": ip, "id": tag, "cracked": False})
            out += f"{ip} ({tag})\n"
        return out
