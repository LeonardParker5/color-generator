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

#Generation of random color image
im = Image.new("RGB", (500, 500), "#" + random_string)
im.show()

#List containing all color values processed from colors_raw.txt
colorlist = colorparser.parse_color()

best_name = ""
best_val = 1000
best_hex = ""
red_rgb = hextorgb.hex_to_rgb(red_hex)
green_rgb = hextorgb.hex_to_rgb(green_hex)
blue_rgb = hextorgb.hex_to_rgb(blue_hex)

#Iterate through colorlist and compare all euclidean distances
for i in range(len(colorlist)):
    euclidian_value = (abs(red_rgb - colorlist[i].get_x()) + abs(green_rgb - colorlist[i].get_y()) + abs(blue_rgb - colorlist[i].get_z()))
    if euclidian_value < best_val:
        best_val = euclidian_value
        best_name = str(colorlist[i].get_name())
        best_hex = str(colorlist[i].get_hex())

#Final values stored in best_name and best_val
print("Best color's name is " + best_name)
print("Best color's hex is " + best_hex)
print("Euclidean value is " + str(best_val))

#Generate comparison image
im_comp = Image.new("RGB", (500, 500), "#" + best_hex)
im_comp.show()