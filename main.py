import base64

def base64_Miguel(texto):
  texto_codificado = base64.b64encode(texto.encode('utf-8'))

def base64_Adria(stringToConvert):
        str_b64 = base64.b64encode(bytes(stringToConvert, 'utf-8'))
        return str_b64
    
def base16_Jorge(input_string):
    hexadecimal = ''.join([f'{ord(char):02x}' for char in input_string])
    return hexadecimal

def base64_Thomas(y):
    return base64.b64encode(y.encode()).decode()

def base64_Fede():
    base64.b64encode(bytes("hola Buenas tardes soy Federico"))
    base64_str = texto.decode('utf-8')
    print(base64_str)
    
def main():
    entrada = input("Introduce texto a convertir a base64: ")
    print(base64_Adria(entrada))
    print(base64_Thomas(entrada))
    #print(base64_Fede())
    print(base16_Jorge(entrada))

if __name__ == "__main__":
    main()

