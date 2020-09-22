from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
from typing import Tuple
import json
import requests
try:
    from credential import MY_AUTH_USER
except ImportError:
    print("Declare sua Key Auth na variavel auth_user")
    MY_AUTH_USER = 'AAAAA_-BBBBBB_CCCCCCC-DDDDDDDDDD'
# python -m flake8 color_windows_to_led.py
# python -m mypy color_windows_to_led.py


def windows_palette_color_current() -> list:
    registry = ConnectRegistry(None, HKEY_CURRENT_USER)
    path_color = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent'
    key = OpenKey(registry, path_color)
    key_value = QueryValueEx(key, 'AccentPalette')
    colors = key_value[0].hex()
    list_color = ['#' + colors[color:color+6] for color in range(0, 64, 8)]
    return list_color


def hex_to_rgb(value: str) -> Tuple[int, int, int]:
    value = value.lstrip('#') if value.startswith("#") else value
    return tuple(int(value[i:i + 2], 16) for i in range(0, 6, 2))

# -------------------------Programa principal-----------------------------
gpio: str = "V5"  # A porta que deve receber a cor RGB
method: str = "update"
# A URL de acesso a API da blynk
url: str = f"http://blynk-cloud.com/{MY_AUTH_USER}/{method}/{gpio}"
print(url)

list_hex_color: list = windows_palette_color_current()
primary_color: str = list_hex_color[3]
rgbColor: list = list(hex_to_rgb(primary_color))
print(rgbColor)
max_color: int = max(rgbColor)
rgbColor = [int((colors/max_color)*255) for colors in rgbColor]
headers: dict = {'Content-type': 'application/json'}
r = requests.put(url, data=json.dumps(rgbColor), headers=headers)
print(rgbColor)
