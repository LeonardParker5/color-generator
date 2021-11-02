#parses lines of colors_raw.txt and creates Colors objects
from colors import Colors
import hextorgb

def parse_color():
    lines = []
    with open('color_data/colors_raw.txt') as file:
        lines = file.readlines()
    
    color_list = []

    for line in lines:
        colorstring = line.rstrip()
        colorsplit = colorstring.split("#")
        
        colorname = str(colorsplit[0])
        final_colorname = colorname.replace("\t","")

        rgbstring = str(colorsplit[1])
        isolated_rgbstring = rgbstring[0:6]
        
        red_hex = str(isolated_rgbstring[0:2])
        green_hex = str(isolated_rgbstring[2:4])
        blue_hex = str(isolated_rgbstring[4:6])

        final_rgbstring = str(hextorgb.hex_to_rgb(red_hex)) + ", " + str(hextorgb.hex_to_rgb(green_hex)) + ", " + str(hextorgb.hex_to_rgb(blue_hex))

        newcolor = Colors(final_colorname, final_rgbstring)
        color_list.append(newcolor)
        
    return color_list