print("Funciona")

def base16_JorgeG(input_string):
    hexadecimal = ''.join([f'{ord(char):02x}' for char in input_string])
    return hexadecimal

input_string = "Jorge Gadea Gómez"
print("String original:", input_string)
print("Representación hexadecimal:", base16_JorgeG(input_string))

import base64

def base64thomas(y):
    return base64.b64encode(y.encode()).decode()

def main():
    entrada = input("Introduce texto a convertir a base64: ")
    print(base64thomas(entrada))

if __name__ == "__main__":
    main()
