from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
from color import Color
class WindowsColor(Color):
    def __init__(self):
        #self.color = self.hex_to_rgb(self.color_current()[3])
        super().__init__(self.color_current()[3], "HEX")

    def color_current(self) -> list:
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        path_color = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent'
        key = OpenKey(registry, path_color)
        key_value = QueryValueEx(key, 'AccentPalette')
        colors = key_value[0].hex()
        list_color = ['#' + colors[color:color+6] for color in range(0, 64, 8)]
        return list_color

if __name__ == "__main__":
    cor = WindowsColor()
    print(cor.get_color(max=False, standard='HEX'))
    cor.set_color([240,124,23], "RGB")
    print(cor.get_color(max=True, standard='HEX'))
