def temperature_converter():
    switchOfKelvin = 273.15
    inp = input('Ready to listen. ').split()
    if inp[0].lower() == 'k':
        celsius = float(inp[1]) - switchOfKelvin
        print(inp[1] + " in Kelvin equals " + str(celsius) + " in Celsius")
    else:
        kelvin = float(inp[1]) + switchOfKelvin
        print(inp[1] + " in Celsius equals " + str(kelvin) + " in Kelvins")


if __name__ == '__main__':
    temperature_converter()
