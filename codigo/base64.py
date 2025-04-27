def encode(cadena):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    ascii_values = [ord(char) for char in cadena]
    encoded_string = ""
    i = 0
    while i < len(ascii_values):
        chunk = ascii_values[i : i + 3]
        i += 3
        binary_chunk = "".join(format(value, "08b") for value in chunk)
        if len(chunk) < 3:
            binary_chunk += "0" * (3 - len(chunk)) * 8
        indices = [
            int(binary_chunk[j : j + 6], 2) for j in range(0, len(binary_chunk), 6)
        ]
        encoded_string += "".join(base64_chars[index] for index in indices)
    return encoded_string


def decode(cadena):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64_dict = {char: i for i, char in enumerate(base64_chars)}
    cadena = cadena.rstrip("=")
    decoded_string = ""
    i = 0
    while i < len(cadena):
        chunk = cadena[i : i + 4]
        i += 4
        indices = [base64_dict[char] for char in chunk]
        binary_chunk = "".join(format(index, "06b") for index in indices)
        for j in range(0, len(binary_chunk), 8):
            byte = binary_chunk[j : j + 8]
            if byte != "00000000":
                decoded_string += chr(int(byte, 2))
    return decoded_string


print("Escribe un string y pulsa ENTER")
cadena = input()
print("Codificador Base64")
print("0. Codificar")
print("1. Decodificar")
print("Escribe una opción (0/1) y pulsa ENTER")
option = int(input())

if option == 0:
    print(encode(cadena))
elif option == 1:
    print(decode(cadena))
else:
    print("ERROR")
