print("Funciona")

import base64

def base64thomas(y):
    return base64.b64encode(y.encode()).decode()

def main():
    entrada = input("Introduce texto a convertir a base64: ")
    print(base64thomas(entrada))

if __name__ == "__main__":
    main()
