def hex_to_rgb(hex_digits):
    hex_digit1 = str(hex_digits[0])
    #print("Hex Digit 1: " + hex_digit1)
    hex_digit2 = str(hex_digits[1])
    #print("Hex Digit 2: " + hex_digit2)

    #Conversion of hex_digit1 and hex_digit2
    hex_digit1 = int(hex_digit1, 16)
    #print("Hex Digit 1 converted to decimal is: " , hex_digit1)
    hex_digit2 = int(hex_digit2, 16)
    #print("Hex Digit 2 converted to decimal is: " , hex_digit2)

    return ((hex_digit1 * 16) + (hex_digit2 * 1))
