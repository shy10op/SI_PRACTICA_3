ALFABETO = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cifrar_vigenere(texto, clave):
    resultado = ""
    clave_repetida = (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    for i in range(len(texto)):
        t_idx = ALFABETO.index(texto[i])
        k_idx = ALFABETO.index(clave_repetida[i])
        nuevo_idx = (t_idx + k_idx) % len(ALFABETO)
        resultado += ALFABETO[nuevo_idx]
    return resultado

def descifrar_vigenere(texto, clave):
    resultado = ""
    clave_repetida = (clave * ((len(texto) // len(clave)) + 1))[:len(texto)]
    for i in range(len(texto)):
        t_idx = ALFABETO.index(texto[i])
        k_idx = ALFABETO.index(clave_repetida[i])
        nuevo_idx = (t_idx - k_idx) % len(ALFABETO)
        resultado += ALFABETO[nuevo_idx]
    return resultado

print("Escribe una opción y pulsa ENTER:")
print("0. Cifrar")
print("1. Descifrar")
opcion = int(input())

print("Escribe el texto y pulsa ENTER:")
texto = input()

clave = "URJC"

if opcion == 0:
    cifrado = cifrar_vigenere(texto, clave)
    print("Texto cifrado:")
    print(cifrado)
elif opcion == 1:
    descifrado = descifrar_vigenere(texto, clave)
    print("Texto descifrado:")
    print(descifrado)
else:
    print("ERROR: opción inválida")
