import hashlib 

# Obtener texto a hashear
texto = input("Ingrese el texto a hashear: ")

# Convertir el texto a bytes
texto_encoded = texto.encode()


# Hashear el texto usando SHA-256
hash_object = hashlib.sha256(texto_encoded)


# Obtener el hash en formato hexadecimal
hash_hex = hash_object.hexdigest()
print("El hash SHA-256 del texto ingresado es:", hash_hex)