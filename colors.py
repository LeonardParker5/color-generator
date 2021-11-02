#Object Class for representing data stripped from colors_raw.txt
class Colors:
    def __init__(self, name, rgb_val):
        self.name = name
        self.rgb_val = rgb_val