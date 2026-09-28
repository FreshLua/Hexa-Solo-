COMMAND_LIST = [
    "help",
    "ls", "cd", "cat", "scanfs",
    "ssh", "netstat", "ping", "trace", "spoof", "nmap",
    "phish", "scamlink", "crack", "hackdesk", "sell",
    "wallet", "bank", "crypto",
    "whoami", "sysinfo", "clear"
]


def help_text():
    out = "AVAILABLE COMMANDS:\n\n"
    for cmd in COMMAND_LIST:
        out += f" - {cmd}\n"
    return out
