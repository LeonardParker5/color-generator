import random, numpy

color_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

random_string = ""

for i in range(0, 6):
    new_random = random.choice(color_values)
    random_string += new_random
    print(new_random + " appended to string.")

print("\nColor generation complete...")
print("\nHex generated : #" + random_string)