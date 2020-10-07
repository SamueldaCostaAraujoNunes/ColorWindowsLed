from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
from typing import Tuple

class WindowsColor():
    def __init__(self):
        self.color = self.hex_to_rgb(self.color_current()[3])

    def color_current(self) -> list:
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        path_color = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent'
        key = OpenKey(registry, path_color)
        key_value = QueryValueEx(key, 'AccentPalette')
        colors = key_value[0].hex()
        list_color = ['#' + colors[color:color+6] for color in range(0, 64, 8)]
        return list_color

    def to_max(self) -> Tuple[int, int, int]:
        max_color: int = max(self.color)
        n_cor = tuple(int((colors/max_color)*255) for colors in self.color)
        return n_cor

    def hex_to_rgb(self, value: str) -> Tuple[int, int, int]:
        value = value.lstrip('#') if value.startswith("#") else value
        return tuple(int(value[i:i + 2], 16) for i in range(0, 6, 2))

    def rgb_to_hex(self, rgb: Tuple) -> str:
        r, g, b = rgb
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        return hex_color.upper()

    def get_color(self, max=False, rgb=True):
        color = self.to_max() if max else self.color
        return color if rgb else self.rgb_to_hex(color)


if __name__ == "__main__":
    cor = WindowsColor()
    print(cor.get_color(max=False, rgb=True))
