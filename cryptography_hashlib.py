import hashlib  # Importa la biblioteca hashlib, que proporciona algoritmos de hash seguros como SHA-256.

# Mensaje a encriptar
message = b"El espinorojo salio de la jungla"  # Define un mensaje como una cadena de bytes (necesario para la función hashlib).

# Mensaje encriptado con hashlib
hashObject = hashlib.sha256(message)  # Crea un objeto hash utilizando el algoritmo SHA-256.
hashDigest = hashObject.hexdigest()  # Convierte el resultado del hash en una representación hexadecimal legible.

# Imprime el mensaje encriptado en formato hexadecimal
print(f"Mensaje: {message}")
print(f"Mensaje encriptado con Hash: {hashDigest}")
