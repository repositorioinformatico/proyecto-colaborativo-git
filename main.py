import base64 

print("Funciona") 


def base64_adria(stringToConvert):
        str_b64 = base64.b64encode(bytes(stringToConvert, 'utf-8'))
        return str_b64


def main():
	while True:
		inp = input("Introduce un texto para ponerlo en base64: \n Si quiere salir del programa excribe 0: ")
		
		if inp == "0":
			print("Saliendo del programa.")
			break
		print(base64_adria(inp))


if __name__ == "__main__":
	main()
