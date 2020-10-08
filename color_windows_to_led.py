from windows_color import WindowsColor
from fita_led import FitaLed
from mouse import Mouse

# python -m flake8 color_windows_to_led.py
# python -m mypy color_windows_to_led.py

cor_do_windows = WindowsColor()
fita = FitaLed("V5", "update")
mouse = Mouse(1)

color_for_send = cor_do_windows.get_color(max=True, standard="RGB")
fita.send_color(color_for_send)
mouse.send_color(color_for_send)