from cryptography.fernet import Fernet  # Importa Fernet, una herramienta de cifrado simétrico de la biblioteca cryptography.

# Generar una clave
key = Fernet.generate_key()  # Genera una clave aleatoria única para el cifrado y descifrado.
cipher_suite = Fernet(key)  # Crea un objeto de cifrado utilizando la clave generada.

# Texto a cifrar
Mensaje = b"El espinorojo salio de la jungla"  # Define el mensaje como una cadena de bytes (requisito para Fernet).

# Cifrar el texto
mensajeCipher = cipher_suite.encrypt(Mensaje)  # Cifra el mensaje utilizando el objeto de cifrado.
print(f"Mensaje cifrado: {mensajeCipher}")  # Imprime el mensaje cifrado en formato de bytes.

# Descifrar el texto
mensajeDeCipher = cipher_suite.decrypt(mensajeCipher)  # Descifra el mensaje cifrado utilizando la misma clave.
print(f"Mensaje descifrado: {mensajeDeCipher}")  # Imprime el mensaje descifrado, aún como cadena de bytes.
