def xor_cipher(texto, clave):
    resultado = ""
    for i in range(len(texto)):
        caracter = texto[i]
        clave_caracter = clave[i % len(clave)]
        xor_resultado = ord(caracter) ^ ord(clave_caracter)
        resultado += chr(xor_resultado)
    return resultado

print("Escribe una opción y pulsa ENTER:")
print("0. Cifrar un texto")
print("1. Descifrar un texto")
opcion = int(input())

print("Escribe el texto y pulsa ENTER:")
texto = input()

clave = "XOR"

if opcion == 0:
    texto_cifrado = xor_cipher(texto, clave)
    print("Texto cifrado:")
    print(texto_cifrado)
elif opcion == 1:
    texto_descifrado = xor_cipher(texto, clave)
    print("Texto descifrado:")
    print(texto_descifrado)
else:
    print("ERROR")
