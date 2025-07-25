#Conversión entre Bytes y ASCII

"""
La codificación ASCII (American Standard Code for Information Interchange)
es un estándar que asigna un número (del 0 al 127) a 128 caracteres,
incluyendo letras, números, signos de puntuación y caracteres de control.

En Python, la conversión entre cadenas de texto (str)
y cadenas de bytes (bytes) se hace principalmente usando el método .encode()
y .decode().

Para ASCII, usamos la codificación 'ascii'.

1. Pasar de un Número Decimal a su Representación ASCII en Bytes (y viceversa)
Número Decimal a ASCII (Byte)
Para un solo número decimal que represente un carácter ASCII:
"""

# Convertir el número decimal 65 (que es 'A' en ASCII) a su byte correspondiente
numero_decimal_A = 65
# numero decimal a bytes
byte_A = numero_decimal_A.to_bytes(1, 'big')
# '1' porque es un solo byte, 'big' es irrelevante para 1 byte
print(f"El número 65 en byte ASCII es: {byte_A}")
# Salida: El número 65 en byte ASCII es: b'A'

# numero decimal a bytes segundo ejemplo
numero_decimal_9 = 57 # 57 es el valor ASCII para el carácter '9'
byte_9 = numero_decimal_9.to_bytes(1, 'big')
print(f"El número 57 en byte ASCII es: {byte_9}")
# Salida: El número 57 en byte ASCII es: b'9'

# numero decimal con chr a  Representación ASCII en Bytes
# O usando chr() y encode()
caracter_a_byte = chr(65).encode('ascii')
print(f"El carácter 'A' a byte ASCII es: {caracter_a_byte}")
# Salida: El carácter 'A' a byte ASCII es: b'A' ASCII (Byte) a Número Decimal


# CONOCIENDO LA LONGITUD DE CUANTOS BYTES TIENE un byte ASCII
# EN ESTE CASO TIENES 1
#Para obtener el valor decimal de un byte ASCII:
# osease
# Representación ASCII en Bytes a numero decimal
byte_A = b'A'
# Accedemos al primer (y único) byte y obtenemos su valor entero
numero_decimal_A_obtenido = byte_A[0]
print(f"El byte b'A' en decimal es: {numero_decimal_A_obtenido}")
# Salida: El byte b'A' en decimal es: 65

# LO MISMO  SABIENDO EL NUMERO DE BYTES QUE TIENE un byte ASCII
byte_9 = b'9'
numero_decimal_9_obtenido = byte_9[0]
print(f"El byte b'9' en decimal es: {numero_decimal_9_obtenido}") # Salida: El byte b'9' en decimal es: 57



#AHORA SI NO CONOCES LA LONGITUD DEL un byte ASCII
 # convertir un numero entero en Representacion ASCII en bytes
numero_entero = 543# Nuestro número entero
#Convertir el entero a una cadena de texto (string)
cadena_de_texto = str(numero_entero)
print(f"Paso 1: Entero {numero_entero} convertido a cadena de texto: '{cadena_de_texto}'")
print(f"Tipo después del Paso 1: {type(cadena_de_texto)}")
# Codificar esa cadena de texto a bytes usando la codificación ASCII
# Python determinará automáticamente cuántos bytes se necesitan para '543'
secuencia_ascii_en_bytes = cadena_de_texto.encode('ascii')
print(f"Cadena '{cadena_de_texto}' codificada a bytes ASCII: {secuencia_ascii_en_bytes}")
print(f"Tipo : {type(secuencia_ascii_en_bytes)}")
print(f"Longitud de la secuencia de bytes: {len(secuencia_ascii_en_bytes)} bytes")


# Ejemplo con otro número
# SI NO CONOCES LA LONGITUD DEL un byte ASCII
# convertir un numero entero en Representacion ASCII en bytes
otro_numero = 12345
otra_cadena = str(otro_numero)
otra_secuencia_bytes = otra_cadena.encode('ascii')
print(f"\nNúmero {otro_numero} a bytes ASCII: {otra_secuencia_bytes}")
print(f"Longitud de la secuencia de bytes: {len(otra_secuencia_bytes)} bytes")







#Pasar de un String (Texto) a Bytes ASCII (y viceversa)
#String (Texto) a Bytes ASCII
# el método .encode() de las cadenas de texto:
cadena_texto = "Hola Mundo"
cadena_bytes_ascii = cadena_texto.encode('ascii')
print(f"'{cadena_texto}' a bytes ASCII: {cadena_bytes_ascii}")
# Salida: 'Hola Mundo' a bytes ASCII: b'Hola Mundo'


# otro ejemplo de #String (Texto) a Bytes ASCII
cadena_texto_con_simbolos = "AB9@"
cadena_bytes_simbolos = cadena_texto_con_simbolos.encode('ascii')
print(f"'{cadena_texto_con_simbolos}' a bytes ASCII: {cadena_bytes_simbolos}")
# Salida: 'AB9@' a bytes ASCII: b'AB9@'


# SIN CARACTERES ASCII
# Importante: Si la cadena de texto contiene caracteres que NO son ASCII (ej. 'ñ', 'á'),
# 'encode('ascii')' fallará o los reemplazará (dependiendo del parámetro 'errors').
try:
    "Niño".encode('ascii')
except UnicodeEncodeError as e:
    print(f"Error al codificar 'Niño' a ASCII: {e}")
# Salida: Error al codificar 'Niño' a ASCII: 'ascii' codec can't encode character '\xd1' in position 1: ordinal not in range(128)



#String (Texto) a Bytes utf-8
# Para manejar esto, usarías otras codificaciones como 'utf-8'
cadena_utf8 = "Niño".encode('utf-8')
print(f"'Niño' a bytes UTF-8: {cadena_utf8}") # Salida: 'Niño' a bytes UTF-8: b'Ni\xc3\xb1o'



#Bytes ASCII a String (Texto)
#el método .decode() de los objetos bytes:
bytes_a_texto = b'Python es genial'
cadena_texto_recuperada = bytes_a_texto.decode('ascii')
print(f"{bytes_a_texto} a String ASCII: '{cadena_texto_recuperada}'")
# Salida: b'Python es genial' a String ASCII: 'Python es genial'

bytes_con_numeros_simbolos = b'\x41\x42\x39\x40' # b'AB9@'
texto_recuperado_numeros_simbolos = bytes_con_numeros_simbolos.decode('ascii')
print(f"{bytes_con_numeros_simbolos} a String ASCII: '{texto_recuperado_numeros_simbolos}'")
# Salida: b'AB9@' a String ASCII: 'AB9@'


# Importante: Si los bytes no son una secuencia ASCII válida (ej. son bytes de UTF-8),
# 'decode('ascii')' fallará.
bytes_ascii_n = b'Ni\xc3\xb1o'
try:
    bytes_ascii_n.decode('ascii')
except UnicodeDecodeError as e:
    print(f"Error al decodificar bytes UTF-8 con ASCII: {e}")
# Salida: Error al decodificar bytes UTF-8 con ASCII: 'ascii' codec can't decode byte 0xc3 in position 2: ordinal not in range(128)

bytes_utf8_n = b'Ni\xc3\xb1o'
#Bytes utf-8 a String (Texto)
# Para decodificar correctamente bytes UTF-8, usarías 'utf-8'
texto_desde_utf8 = bytes_utf8_n.decode('utf-8')
print(f"Bytes UTF-8 a String UTF-8: '{texto_desde_utf8}'")
# Salida: Bytes UTF-8 a String UTF-8: 'Niño'
