import base64

def base16_JorgeG(input_string):
    hexadecimal = ''.join([f'{ord(char):02x}' for char in input_string])
    return hexadecimal

def base64thomas(y):
    return base64.b64encode(y.encode()).decode()

def base64-fede():
   texto base64.b64encode(bytes("hola Buenas tardes soy Federico"))
    base64_str = texto.decode('utf-8')
    print(base64_str)
    
def main():
    entrada = input("Introduce texto a convertir a base64: ")
    print(base64thomas(entrada))

if __name__ == "__main__":
    main()
