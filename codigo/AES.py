from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def cifrar_aes(texto, clave, iv):
    clave_bytes = clave.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    texto_bytes = texto.encode('utf-8')
    texto_padded = pad(texto_bytes, AES.block_size)
    cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    cifrado = cipher.encrypt(texto_padded)
    return cifrado.hex().upper()

def descifrar_aes(hex_cifrado, clave, iv):
    clave_bytes = clave.encode('utf-8')
    iv_bytes = iv.encode('utf-8')
    cifrado_bytes = bytes.fromhex(hex_cifrado)
    cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    descifrado_padded = cipher.decrypt(cifrado_bytes)
    descifrado = unpad(descifrado_padded, AES.block_size)
    return descifrado.decode('utf-8')

clave = "SeguridadInforma"
iv = "SeguridadInforma"

print("Escribe una opción y pulsa ENTER:")
print("0. Cifrar un texto")
print("1. Descifrar un texto en HEX")
opcion = int(input())

if opcion == 0:
    print("Escribe el texto a cifrar y pulsa ENTER:")
    texto = input()
    cifrado_hex = cifrar_aes(texto, clave, iv)
    print("Texto cifrado (hex):")
    print(cifrado_hex)

elif opcion == 1:
    print("Escribe el texto cifrado en HEX y pulsa ENTER:")
    hex_cifrado = input()
    texto_descifrado = descifrar_aes(hex_cifrado, clave, iv)
    print("Texto descifrado:")
    print(texto_descifrado)

else:
    print("ERROR")
