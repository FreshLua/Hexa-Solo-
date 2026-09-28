from dataclasses import dataclass


@dataclass
class HexaTheme:
    desktop_bg_top: str = "#2b4c7e"
    desktop_bg_bottom: str = "#0f1b2e"
    taskbar_bg: str = "#1b2738"
    taskbar_border: str = "#0a0f18"
    taskbar_button_bg: str = "#30435f"
    taskbar_button_hover: str = "#3c5273"
    taskbar_button_active: str = "#486287"
    window_title_top: str = "#3f6fb0"
    window_title_bottom: str = "#274a7a"
    window_body_bg: str = "#e3e6ea"
    window_border: str = "#1b2738"
    window_shadow: str = "#000000"
    text_primary: str = "#000000"
    text_inverse: str = "#ffffff"
    accent_blue: str = "#3f6fb0"
    accent_red: str = "#c0392b"
    accent_yellow: str = "#f1c40f"
