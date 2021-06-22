# Implementation program to convert RGB color code to Hex color code

# Function to convert decimal to hexadecimal
def decimalToHexa(n):
    # char array to store hexadecimal number
    hexaDecimalNumber = ['0'] * 100

    # hexadecimal's counter number array
    i = 0

    while (n != 0):

        #  remainder is stored in a temporary variable named __temp
        _temp = 0

        # Storing remainder in _temp variable.
        _temp = n % 16

        # Check if _temp < 10
        if (_temp < 10):
            hexaDecimalNumber[i] = chr(_temp + 48)
            i = i + 1

        else:
            hexaDecimalNumber[i] = chr(_temp + 55)
            i = i + 1

        n = int(n / 16)

    hexadecimalCode = ""
    if (i == 2):
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[1]

    elif (i == 1):
        hexadecimalCode = "0"
        hexadecimalCode = hexadecimalCode + hexaDecimalNumber[0]

    elif (i == 0):
        hexadecimalCode = "00"

    # Return the equivalent of hexadecimal color code
    return hexadecimalCode


# Function to convert the RGB to Hexadecimal color code
def RGBtoHexConverion(R, G, B):
    if ((R >= 0 and R <= 255) and
            (G >= 0 and G <= 255) and
            (B >= 0 and B <= 255)):

        hexadecimalCode = "#"
        hexadecimalCode = hexadecimalCode + decimalToHexa(R)
        hexadecimalCode = hexadecimalCode + decimalToHexa(G)
        hexadecimalCode = hexadecimalCode + decimalToHexa(B)
        return hexadecimalCode

    # If the hexadecimal color code does not exist, return -1
    else:
        return "-1"


# main method to test the program code
if __name__=='__main__':
    R = 255
    G = 255
    B = 256
    print(RGBtoHexConverion(R, G, B))

    R = 0
    G = 0
    B = 0
    print(RGBtoHexConverion(R, G, B))

    R = 255
    G = 255
    B = 255
    print(RGBtoHexConverion(R, G, B))

    R = 25
    G = 56
    B = 123
    print(RGBtoHexConverion(R, G, B))

    R = 2
    G = 3
    B = 4
    print(RGBtoHexConverion(R, G, B))
