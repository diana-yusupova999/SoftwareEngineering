def temperature_converter():
    inp = input('Ready to listen. Use "!help" to see what i can do :) ').split()

    if inp[0].lower() == 'f':
        celsius = farr_cell(inp[1], 'c')
        if inp[2].lower() == 'c':
            to_print(inp[1], celsius, inp[0], inp[2])
        else:
            kelvin = kelv_cell(celsius, 'k')
            to_print(inp[1], kelvin, inp[0], inp[2])
    else:
        if inp[2].lower() == 'f':
            if inp[0].lower() == 'c':
                farr = farr_cell(inp[1], 'f')
                to_print(inp[1], farr, inp[0], inp[2])
            else:
                cell = kelv_cell(inp[1], 'c')
                farr = farr_cell(cell, 'f')
                to_print(inp[1], farr, inp[0], inp[2])
        if inp[0].lower() == 'k':
            celsius = kelv_cell(inp[1], 'c')
            to_print(inp[1], celsius, inp[0], inp[2])
        else:
            kelvin = kelv_cell(inp[1], 'k')
            to_print(inp[1], kelvin, inp[0], inp[2])


def to_print(inpTemp, outTemp, inpStr, outStr):
    return print(inpTemp + "° " + inpStr + " equals " + str(round(outTemp, 3)) + "° " + outStr)


def kelv_cell(temp, dest):
    if dest.lower() == 'c':
        result = float(temp) - 273.15
    else:
        result = float(temp) + 273.15
    return result


def farr_cell(temp, dest):
    if dest.lower() == 'c':
        result = 5 / 9 * (float(temp) - 32)
    else:
        result = 9 / 5 * float(temp) + 32
    return result


if __name__ == '__main__':
    temperature_converter()
