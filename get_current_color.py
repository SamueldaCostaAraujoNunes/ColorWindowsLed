from winreg import HKEY_CURRENT_USER, ConnectRegistry, OpenKey, QueryValueEx
from typing import Tuple
import json
import requests
try:
    from credential import MY_AUTH_USER
except ImportError:
    print("Declare sua Key Auth na variavel auth_user")
    MY_AUTH_USER = 'AAAAA_-BBBBBB_CCCCCCC-DDDDDDDDDD'


# -------------------------Programa principal-----------------------------
gpio: str = "V5"  # A porta que deve mandar a cor RGB
method: str = "get"  # Metodo RESTful

url: str = f"http://blynk-cloud.com/{MY_AUTH_USER}/{method}/{gpio}"
r = requests.get(url)
cores = r.text
cores = json.loads(cores)
cores = [int(cor) for cor in cores]
print(cores)
