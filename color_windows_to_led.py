from windows_color import WindowsColor
from fita_led import FitaLed

# python -m flake8 color_windows_to_led.py
# python -m mypy color_windows_to_led.py

cor_do_windows = WindowsColor()
fita = FitaLed("V5", "update")
fita.send_color(cor_do_windows.get_color(max=True, rgb=True))