print("Funciona")

import base64

texto = "buenos dias"
texto_codificado = base64.b64encode(texto.encode('utf-8'))

print ("texto original:", = texto)
print ("texto codificado en base-64:", texto_codificado)

