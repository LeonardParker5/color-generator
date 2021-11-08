#Object Class for representing data stripped from colors_raw.txt
class Colors:
    def __init__(self, name, rgb_val, hex_val):
        self.name = name
        self.rgb_val = rgb_val
        self.hex_val = hex_val
        
    def get_x(self):
        colorsplit = self.rgb_val.split(", ")
        return int(colorsplit[0])

    def get_y(self):
        colorsplit = self.rgb_val.split(", ")
        return int(colorsplit[1])

    def get_z(self):
        colorsplit = self.rgb_val.split(", ")
        return int(colorsplit[2])

    def get_name(self):
        return self.name

    def get_hex(self):
        return self.hex_val
