import random, numpy

color_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

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

#def hex_to_rgb(hex_digits):
#    print()