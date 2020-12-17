import os
class Mouse:
    def __init__(self, M_Profile):
        self.profile = M_Profile

    def send_color(self, color):
        print("Send color for Mouse Redragon Cobra:", color)
        os.system(f'MouseColor\\MouseColor.exe {color[0]} {color[1]} {color[2]}')