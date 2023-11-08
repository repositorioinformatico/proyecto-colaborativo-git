print("Funciona")
def base16_JorgeG(input_string):
    hexadecimal = ''.join([f'{ord(char):02x}' for char in input_string])
    return hexadecimal

input_string = "Jorge Gadea Gómez"
print("String original:", input_string)
print("Representación hexadecimal:", base16_JorgeG(input_string))

