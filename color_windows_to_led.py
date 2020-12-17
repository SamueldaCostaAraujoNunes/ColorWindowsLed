from windows_color import WindowsColor
from fita_led import FitaLed
from mouse import Mouse

# python -m flake8 color_windows_to_led.py
# python -m mypy color_windows_to_led.py

cor_do_windows = WindowsColor()
fita = FitaLed("V5", "update")
mouse = Mouse(1)

devices = [fita, mouse]

color_for_send = cor_do_windows.get_color(max=True, standard="RGB")

# color_for_send = [255,63,0]

for device in devices:
    device.send_color(color_for_send)