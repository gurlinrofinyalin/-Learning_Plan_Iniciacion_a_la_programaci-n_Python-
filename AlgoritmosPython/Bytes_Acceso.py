cadena_bytes = b'\x20\x19\x61\x62\x39\x40'

# Acceso al último elemento
# RESPECTA LOS PRINCIPIOS DE Indexing slicing y stride

entero = cadena_bytes[-1] # devuelve un entero no un objeto bytes
#  Cuando accedes a un elemento individual de un objeto 'bytes'
# usando indexación (como cadena_bytes[-1] o cadena_bytes[0]),
### PRECULIARIDAD  Python te devuelve directamente el valor DECIMAL de ese byte.

print(type(entero)) # Salida: <class 'int'>
#   Esto confirma que el valor devuelto es un entero (int),
# no un objeto de tipo 'bytes' con un solo byte.

print(entero) # Salida: 64
#   El último byte de b'\x20\x19\x61\x62\x39\x40' es '\x40'.
# '\x40' en hexadecimal es 64 en decimal.

# Recorrido de elementos
# Lo que planteaste es muy cercano a la sintaxis de un bucle for-in de Python.
# En Python, para iterar sobre una cadena de bytes (o cualquier secuencia),
# simplemente usas un bucle 'for... in...'. No necesitas llamar a '__iter__()'
# explícitamente ni usar una sintaxis como 'for(ele: ...)' que es más de otros lenguajes.

print("\nRecorriendo la cadena de bytes:")
for ele in cadena_bytes:
    # Comentario: En cada iteración del bucle, 'ele' tomará el valor DECIMAL
    # de cada byte en la secuencia.
    print(f"Tipo: {str(type(ele))}, Valor: {ele}")

# Salida del bucle:
# Tipo: <class 'int'>, Valor: 32
# Tipo: <class 'int'>, Valor: 25
# Tipo: <class 'int'>, Valor: 97
# Tipo: <class 'int'>, Valor: 98
# Tipo: <class 'int'>, Valor: 57
# Tipo: <class 'int'>, Valor: 64




# indexing
mi_cadena = b'Python'
print(mi_cadena[0])  # Output: 80 (Valor ASCII de 'P')
print(mi_cadena[1])  # Output: 121 (Valor ASCII de 'y')
print(mi_cadena[-1]) # Output: 110 (Valor ASCII de 'n')


# slicing
#Slicing (Rebanado) es la operación de tomar una parte de una secuencia. Es el "cómo" extraes una sub-secuencia.
mi_cadena = b'abcdefgh'
print(mi_cadena[1:5])   # Output: b'bcde' (Elementos desde el índice 1 hasta el 4, excluyendo el 5)
print(mi_cadena[:3])    # Output: b'abc' (Desde el principio hasta el índice 2, excluyendo el 3)
print(mi_cadena[4:])    # Output: b'efgh' (Desde el índice 4 hasta el final)
print(mi_cadena[:])     # Output: b'abcdefgh' (Una copia completa de la secuencia)

# stride
#La sintaxis de slicing es [inicio:fin:paso].
#El Stride (Paso) es el parámetro final dentro de esa operación de slicing.
# Es el paso en [inicio:fin:paso]. Te dice cómo o con qué frecuencia seleccionas
# elementos dentro de esa rebanada.
mi_cadena = b'0123456789'
print(mi_cadena[::2])   # Output: b'02468' (Desde el principio hasta el final, saltando de 2 en 2)
print(mi_cadena[1::3])  # Output: b'147' (Desde el índice 1 hasta el final, saltando de 3 en 3)
print(mi_cadena[::-1])  # Output: b'9876543210' (Invertir la secuencia)



# INterpretar el entero que devuelve cadena_bytes[-1]
# como un valor hexagesimal con la Función hex()
print(hex(cadena_bytes[-1]))# '0x40'    devuelve una representacion de hexagesimal
print(type(hex(cadena_bytes[-1])))# <class 'str'>

# usando slicing y stride  devuelve un tipo de dato bytes
cadena_bytes = b'\x20\x19\x61\x62\x39\x40'
print(cadena_bytes[-1:])#b'@'
print(cadena_bytes[0::2])#b' a9'
print(type(cadena_bytes[-1:]))# <class 'bytes'>
print(type(cadena_bytes[0::2]))#<class 'bytes'>

try:
    cadena_bytes[0] = b'4'
except TypeError:
    print("'bytes' object does not support item assignment")
    print(" bytes son inmutables  no se permite la modificacion")

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/AlgoritmosPython/Bytes_Acceso.py", line 82, in <module>
    cadena_bytes[0] = b'4'
    ~~~~~~~~~~~~^^^
TypeError: 'bytes' object does not support item assignment
"""

cad1 = b'\x20\x19\x61'
# Comentario: Define una cadena de bytes:
# '\x20': Espacio (ASCII 32)
# '\x19': Símbolo de control (ASCII 25, no imprimible)
# '\x61': 'a' (ASCII 97)

cad2 = b'\x62\x39\x40'
# Comentario: Otra cadena de bytes:
# '\x62': 'b' (ASCII 98)
# '\x39': '9' (ASCII 57)
# '\x40': '@' (ASCII 64)

# Decodificación a UTF-8
# Nota: La decodificación a UTF-8 es válida, pero estos bytes son en realidad ASCII.
# Como ASCII es un subconjunto de UTF-8, la decodificación funciona sin problemas.
# Si hubieran bytes fuera del rango ASCII (ej. caracteres con tildes), UTF-8 sería necesario.
cadena_cad1_utf8 = cad1.decode('utf-8')
print(f"  bytes UTF-8: {cadena_cad1_utf8}")# bytes UTF-8:  a
# Salida:   bytes UTF-8:  a
# Comentario: El '\x20' es un espacio, el '\x19' no es imprimible y UTF-8 lo "oculta" o lo muestra como un control.
# El '\x61' es 'a'.

cadena_cad2_utf8 = cad2.decode('utf-8')
print(f" bytes UTF-8: {cadena_cad2_utf8}")#bytes UTF-8: b9@
# Salida:  bytes UTF-8: b9@
# Comentario: '\x62' es 'b', '\x39' es '9', '\x40' es '@'. Todos son imprimibles.

# Suma (Concatenación)
print(cad1 + cad2)
# Salida: b' \x19ab9@'
# Comentario: El operador '+' para cadenas de bytes realiza una concatenación.
# Une las dos secuencias de bytes una detrás de otra, formando una nueva secuencia.
# Python muestra el espacio y los caracteres imprimibles, y el '\x19' en su notación hexadecimal
# porque no tiene una representación de carácter estándar.

# Multiplicación (Repetición)
print(cad1 * 2)
# Salida: b' \x19a \x19a'
# Comentario: El operador '*' con un entero repite la secuencia de bytes el número de veces indicado.
# b'\x20\x19\x61' repetido dos veces es b'\x20\x19\x61\x20\x19\x61'.

# Comparación de Contenido (Igualdad)
print(cad1 == cad2)
# Salida: False
# Comentario: Compara si el contenido de las dos cadenas de bytes es idéntico.
# Como cad1 (b' \x19a') y cad2 (b'b9@') tienen bytes diferentes, el resultado es False.

# Comparación de Contenido (Desigualdad)
print(cad1 != cad2)
# Salida: True
# Comentario: Opuesto a '=='. Como no son iguales, el resultado es True.

# Comparación de Identidad de Objeto
print(cad1 is cad2)
# Salida: False
# Comentario: El operador 'is' comprueba si dos variables apuntan al *mismo objeto* en memoria.
# Aunque sus contenidos pudieran ser iguales (en este caso no lo son), Python generalmente crea
# objetos de bytes separados para literales distintos, por lo que no son el mismo objeto.

print(cad1 is cad2) # Repetido, misma salida.
# Salida: False
# Comentario: Misma comprobación de identidad de objeto.
