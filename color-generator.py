import random, hextorgb, colorparser
from PIL import Image

color_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

random_string = ""

for i in range(0, 6):
    new_random = random.choice(color_values)
    random_string += new_random
    print(new_random + " appended to string.")

print("\nColor generation complete...")
print("\nHex generated : #" + random_string)

red_hex = random_string[0:2]
print("Red Hex Value: " + red_hex)
green_hex = random_string[2:4]
print("Green Hex Value: " + green_hex)
blue_hex = random_string[4:6]
print("Blue Hex Value: " + blue_hex)

print("\nRed Hex Value converted to RGB value is: " , hextorgb.hex_to_rgb(red_hex))
print("\nGreen Hex Value converted to RGB value is: " , hextorgb.hex_to_rgb(green_hex))
print("\nBlue Hex Value converted to RGB value is: " , hextorgb.hex_to_rgb(blue_hex))

im = Image.new("RGB", (500, 500), "#" + random_string)
im.show()

colorlist = colorparser.parse_color()