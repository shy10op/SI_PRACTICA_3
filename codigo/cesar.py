ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar_cesar(texto, desplazar):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            indice = ALFABETO.find(caracter.upper())
            nuevo_indice = (indice + desplazar) % len(ALFABETO)
            resultado += ALFABETO[nuevo_indice]
        else:
            resultado += caracter
    return resultado


def descifrar_cesar(texto, desplazar):
    return cifrar_cesar(texto, -desplazar)


print("Escribe una opción y pulsa ENTER:")
print("0. Cifrar un texto")
print("1. Ataque de fuerza bruta para descifrar")
opcion = int(input())

if opcion == 0:
    print("Escribe el texto a cifrar y pulsa ENTER:")
    texto = input()
    print("Escribe el desplazamiento (1-25) y pulsa ENTER:")
    desplazamiento = int(input())
    texto_cifrado = cifrar_cesar(texto, desplazamiento)
    print(f"Texto cifrado: {texto_cifrado}")

elif opcion == 1:
    print("Escribe el texto cifrado y pulsa ENTER:")
    texto_cifrado = input()
    print("\nAtaque por fuerza bruta:")
    for d in range(1, 26):
        posible_texto = descifrar_cesar(texto_cifrado, d)
        print(f"ROT_{d}: {posible_texto}")

else:
    print("ERROR")
