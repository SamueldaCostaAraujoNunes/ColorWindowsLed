from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
from typing import Tuple
from windows_color import WindowsColor
import json
import requests

try:
    from credential import MY_AUTH_USER
except ImportError:
    print("Declare sua Key Auth na variavel MY_AUTH_USER")
    MY_AUTH_USER = 'AAAAA_-BBBBBB_CCCCCCC-DDDDDDDDDD'


class FitaLed():
    def __init__(self, gpio, method):
        self.gpio = gpio
        self.method = method
        self.url: str = f"http://blynk-cloud.com/{MY_AUTH_USER}/{method}/{gpio}"

    def send_color(self, color: Tuple):
        print("Send color for Led Strip:", color)
        headers: dict = {'Content-type': 'application/json'}
        r = requests.put(self.url, data=json.dumps(color), headers=headers)
        return r.status_code == 200

if __name__ == "__main__":
    fita = FitaLed("V5", "update")
    r = fita.send_color((255,255,0))