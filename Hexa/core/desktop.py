from tkinter import Canvas, Label, Button
from core.icons import IconSet
from core.animations import DesktopAnimator
from core.taskbar import Taskbar
from core.terminal import TerminalWindow
from core.missions import MissionHub
from core.market import DarkNetMarket
from core.scam_dashboard import ScamDashboard
from core.victims_app import VictimsApp
from core.downloads_app import DownloadsApp
from core.player import PlayerProfile
from core.ui.wallpaper import Wallpaper
from core.log_viewer import LogViewer
from core.file_explorer import FileExplorer
from core.ui.start_menu import StartMenu
from core.ui.theme import HexaTheme


class HexaDesktop:
    def __init__(self, root, player_data):
        self.root = root
        self.player_profile = PlayerProfile(root, player_data)

        for w in root.winfo_children():
            w.destroy()

        self.theme = HexaTheme()
        root.configure(bg=self.theme.desktop_bg_bottom)
        self.iconset = IconSet()
        self.build()

    def build(self):
        self.desktop = Canvas(self.root, highlightthickness=0)
        self.desktop.pack(fill="both", expand=True)

        self.wallpaper = Wallpaper(self.root, self.desktop)
        self.root.after(50, self.wallpaper.draw_gradient)

        self.taskbar = Taskbar(self.root)
        self.player_profile.taskbar = self.taskbar

        Label(self.root, text=f"HEXA OS - {self.player_profile.data['name']}",
              fg=self.theme.text_inverse, bg=self.theme.desktop_bg_top,
              font=("Consolas", 14, "bold")).place(x=12, y=8)

        self.start_menu = StartMenu(
    self.root,
    [
        ("Terminal", lambda: TerminalWindow(self.root, self.player_profile)),
        ("Mission Hub", lambda: MissionHub(self.root, self.player_profile)),
        ("Tool Market", lambda: DarkNetMarket(self.root, self.player_profile)),
        ("Scam Dashboard", lambda: ScamDashboard(self.root, self.player_profile)),
        ("Victims", lambda: VictimsApp(self.root, self.player_profile, self.player_profile.net_targets)),
        ("Data Market", lambda: DownloadsApp(self.root, self.player_profile)),
        ("File Explorer", lambda: FileExplorer(self.root, self.player_profile)),
        ("Log Viewer", lambda: LogViewer(self.root, self.player_profile)),
    ]
)


        start_btn = Button(
            self.taskbar.frame,
            text="Start",
            bg="#34527c",
            fg=self.theme.text_inverse,
            bd=0,
            padx=12,
            command=lambda: self.start_menu.toggle(
                self.taskbar.frame.winfo_rootx(),
                self.taskbar.frame.winfo_rooty()
            )
        )
        start_btn.pack(side="left", padx=(4, 8), pady=2)

        term_img = self.iconset.load("assets/icons/terminal.png")
        mission_img = self.iconset.load("assets/icons/mission.png")
        market_img = self.iconset.load("assets/icons/market.png")
        scam_img = self.iconset.load("assets/icons/scam.png")
        victims_img = self.iconset.load("assets/icons/victims.png")
        downloads_img = self.iconset.load("assets/icons/downloads.png")

        self._icons_refs = []

        self.draw_icon(80, 120, term_img, "icon_terminal", "Terminal", self.draw_terminal_svg)
        self.draw_icon(80, 220, mission_img, "icon_mission", "Mission Hub", self.draw_mission_svg)
        self.draw_icon(80, 320, market_img, "icon_market", "Market", self.draw_market_svg)
        self.draw_icon(80, 420, scam_img, "icon_scam", "Scam Dashboard", self.draw_scam_svg)

        self.draw_icon(200, 120, victims_img, "icon_victims", "Victims", self.draw_victims_svg)
        self.draw_icon(200, 220, downloads_img, "icon_downloads", "Downloads", self.draw_downloads_svg)

        self.desktop.bind("<Button-1>", self.on_click)

        self.animator = DesktopAnimator(self.root, self.desktop)
        self.animator.start()

    def draw_icon(self, x, y, img, tag, label, svg_draw_fn):
        if img is not None:
            self.desktop.create_image(x, y, image=img, anchor="center", tags=(tag,))
            self._icons_refs.append(img)
        else:
            svg_draw_fn(x, y, tag)
        self.desktop.create_text(x, y + 40, text=label,
                                 fill=self.theme.text_inverse,
                                 font=("Consolas", 10))

    def draw_terminal_svg(self, x, y, tag):
        r = 26
        self.desktop.create_rectangle(x - r, y - r, x + r, y + r,
                                      outline=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x - 10, y, x, y + 8,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x, y + 8, x + 12, y - 6,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))

    def draw_mission_svg(self, x, y, tag):
        r = 26
        self.desktop.create_rectangle(x - r, y - r, x + r, y + r,
                                      outline=self.theme.accent_yellow, width=2, tags=(tag,))
        self.desktop.create_line(x - 8, y, x, y + 10,
                                 fill=self.theme.accent_yellow, width=2, tags=(tag,))
        self.desktop.create_line(x, y + 10, x + 12, y - 12,
                                 fill=self.theme.accent_yellow, width=2, tags=(tag,))

    def draw_market_svg(self, x, y, tag):
        r = 26
        self.desktop.create_rectangle(x - r, y - r, x + r, y + r,
                                      outline=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x - 12, y + 8, x - 4, y - 4,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x - 4, y - 4, x + 6, y + 6,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x + 6, y + 6, x + 12, y - 10,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))

    def draw_scam_svg(self, x, y, tag):
        r = 26
        self.desktop.create_oval(x - r, y - r, x + r, y + r,
                                 outline=self.theme.accent_red, width=2, tags=(tag,))
        self.desktop.create_polygon(
            x - 8, y + 6,
            x, y - 10,
            x + 8, y + 6,
            outline=self.theme.accent_red, fill="", width=2, tags=(tag,)
        )

    def draw_victims_svg(self, x, y, tag):
        r = 26
        self.desktop.create_oval(x - r, y - r, x + r, y + r,
                                 outline=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x - 10, y, x + 10, y,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_line(x, y - 10, x, y + 10,
                                 fill=self.theme.accent_blue, width=2, tags=(tag,))

    def draw_downloads_svg(self, x, y, tag):
        r = 26
        self.desktop.create_rectangle(x - r, y - r, x + r, y + r,
                                      outline=self.theme.accent_blue, width=2, tags=(tag,))
        self.desktop.create_polygon(
            x - 10, y - 5,
            x + 10, y - 5,
            x, y + 12,
            outline=self.theme.accent_blue, fill="", width=2, tags=(tag,)
        )

    def on_click(self, event):
        item = self.desktop.find_closest(event.x, event.y)
        tags = self.desktop.gettags(item)

        if "icon_terminal" in tags:
            TerminalWindow(self.root, self.player_profile)
        elif "icon_mission" in tags:
            MissionHub(self.root, self.player_profile)
        elif "icon_market" in tags:
            DarkNetMarket(self.root, self.player_profile)
        elif "icon_scam" in tags:
            ScamDashboard(self.root, self.player_profile)
        elif "icon_victims" in tags:
            VictimsApp(self.root, self.player_profile, self.player_profile.net_targets)
        elif "icon_downloads" in tags:
            DownloadsApp(self.root, self.player_profile)
