#parses lines of colors_raw.txt and creates Colors objects
import hextorgb

def parse_color():
    lines = []
    with open('color_data/colors_raw.txt') as file:
        lines = file.readlines()
    
    for line in lines[:5]:
        print(line)