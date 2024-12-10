from cryptography.hazmat.primitives.asymmetric import rsa, padding  # Importa RSA para generar claves y padding para el cifrado.
from cryptography.hazmat.primitives import serialization, hashes  # Importa herramientas para serializar claves y calcular hashes.

# Generar par de claves
llavePrivada = rsa.generate_private_key(  # Genera una clave privada RSA.
    public_exponent=65537,  # Exponente público comúnmente utilizado.
    key_size=1024,  # Tamaño de la clave en bits (1024 es menor seguridad comparada con 2048 o más).
)

llavePublica = llavePrivada.public_key()  # Deriva la clave pública a partir de la clave privada.

# Serializar las claves
private_pem = llavePrivada.private_bytes(  # Serializa la clave privada en formato PEM.
    encoding=serialization.Encoding.PEM,  # Define el formato de codificación.
    format=serialization.PrivateFormat.TraditionalOpenSSL,  # Formato tradicional de clave privada.
    encryption_algorithm=serialization.NoEncryption()  # Sin cifrado en la clave privada serializada.
)

public_pem = llavePublica.public_bytes(  # Serializa la clave pública en formato PEM.
    encoding=serialization.Encoding.PEM,  # Define el formato de codificación.
    format=serialization.PublicFormat.SubjectPublicKeyInfo  # Formato estándar para claves públicas.
)

# Mostrar las claves
print(private_pem.decode('utf-8'))  # Muestra la clave privada en formato legible.
print(public_pem.decode('utf-8'))  # Muestra la clave pública en formato legible.

# Texto a cifrar
mensaje = b"El espinorojo salio de la jungla"  # Define el mensaje como una cadena de bytes.

# Cifrar el mensaje con la clave pública
textoCifrado = llavePublica.encrypt(  # Cifra el mensaje usando la clave pública.
    mensaje,
    padding.OAEP(  # Utiliza el esquema de relleno OAEP (Optical Asymmetric Encryption Padding).
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Generador de máscara basado en SHA-256.
        algorithm=hashes.SHA256(),  # Algoritmo de hash utilizado.
        label=None  # No se utiliza etiqueta.
    )
)
print(f"Mensaje cifrado: {textoCifrado}")  # Muestra el mensaje cifrado.

# Descifrar el mensaje con la clave privada
textoDecifrado = llavePrivada.decrypt(  # Descifra el mensaje usando la clave privada.
    textoCifrado,
    padding.OAEP(  # Debe coincidir con el esquema de relleno utilizado durante el cifrado.
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Generador de máscara basado en SHA-256.
        algorithm=hashes.SHA256(),  # Algoritmo de hash utilizado.
        label=None  # No se utiliza etiqueta.
    )
)
print(f"Mensaje descifrado: {textoDecifrado}")  # Muestra el mensaje descifrado.
