def temperature_converter():
    primary = str(input('Available scales: K(Kelvin), C(Celsius), F(Fahrenheit). '
                        'Use "!help" to see what i can do :) '))
    if primary.lower() == '!help':
        return print('Simple temperature converter. Input format: PRIMARY_TEMP VALUE SOURCE_TEMP '
                     'Available scales: K(Kelvin), C(Celsius), F(Fahrenheit)')
    value = float(input('Enter value to convert '))
    source = str(input('Available scales: K(Kelvin), C(Celsius), F(Fahrenheit). '))

    if primary[0].lower() == 'f':
        celsius = farr_cell(value, 'c')
        if source[0].lower() == 'c':
            to_print(value, float(celsius), primary[0], source[0])
        else:
            kelvin = kelv_cell(celsius, 'k')
            to_print(value, kelvin, primary[0], source[0])
    else:
        if source[0].lower() == 'f':
            if primary[0].lower() == 'c':
                farr = farr_cell(value, 'f')
                return to_print(value, farr, primary[0], source[0])
            else:
                cell = kelv_cell(value, 'c')
                farr = farr_cell(cell, 'f')
                return to_print(value, farr, primary[0], source[0])
        if primary[0].lower() == 'k':
            celsius = kelv_cell(value, 'c')
            return to_print(value, celsius, primary[0], source[0])
        else:
            kelvin = kelv_cell(value, 'k')
            return to_print(value, kelvin, primary[0], source[0])


def to_print(inpTemp, outTemp, inpStr, outStr):
    return print(str(inpTemp) + "° " + inpStr + " equals " + str(round(outTemp, 3)) + "° " + outStr)


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
