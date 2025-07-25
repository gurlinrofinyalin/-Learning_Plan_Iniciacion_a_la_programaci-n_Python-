# Un bytearray se corresponde con una cadena de bytes
# MUTABLE      (el bytes no es mutable )
from AlgoritmosPython.BytesConvertirASCII import cadena_utf8

# LA CREACION DE TIPO DATO bytearray debe hacerse
# siempre con la funcion  bytearray
cadena_bytes = bytearray(b'\x20\x19\x61\x62\x39\x40')
print(cadena_bytes.decode('ascii'))#  ab9@
print(cadena_bytes.decode('utf-8'))#  ab9@
print(type(cadena_bytes))#<class 'bytearray'>
print(cadena_bytes)#bytearray(b' \x19ab9@')

# acceso indexing
print(cadena_bytes[0])#32

# acceso slicing
print(cadena_bytes[0:4])#bytearray(b' \x19ab')

# modificacion de bytearray que es mutable
# bytes es inmutable

print(cadena_bytes)#bytearray(b' \x19ab9@')
cadena_bytes[0:1] = b'8'
print(cadena_bytes)#bytearray(b'8\x19ab9@')


# si realizamos la asignacion , de un unico elemento del bytearray
# debemos proporcionar un valor de tipo int



"""
Las funciones ord() y chr() son herramientas fundamentales en Python para trabajar
 con caracteres y sus representaciones numéricas, específicamente sus puntos de 
 código Unicode (que en el rango ASCII son los mismos que sus valores ASCII).

ord() (Ordinal)
ord() te da el valor numérico (decimal) de un carácter dado.
Sintaxis: ord(c) donde c es una cadena de un solo carácter.
Qué hace: Retorna el punto de código Unicode del carácter.
 Para caracteres ASCII, esto es equivalente a su valor decimal ASCII.
"""
print(help(ord))
"""
Help on built-in function ord in module builtins:

ord(c, /)
    Return the Unicode code point for a one-character string.

None
"""
# Comentario: Esta es la documentación oficial de Python para 'ord()'.
# Indica que toma una cadena de UN solo carácter y devuelve su valor Unicode (entero).

"""chr() (Character)
chr() es lo opuesto a ord(). Toma un número y te devuelve el carácter correspondiente.
Sintaxis: chr(i) donde i es un número entero que representa un punto de código Unicode.
Qué hace: Retorna una cadena de UN solo carácter Unicode cuyo punto de código es i.
"""
print(help(chr))
"""
elp on built-in function chr in module builtins:

chr(i, /)
    Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

None
"""
# Comentario: Esta es la documentación oficial de Python para 'chr()'.
# Indica que toma un número entero y devuelve el carácter Unicode correspondiente.









cadena_bytes = bytearray(b'8\x19ab9@')
# Comentario: Aquí se inicializa un objeto 'bytearray'.
# Un 'bytearray' es una secuencia de bytes MUTABLE, lo que significa que
# sus elementos pueden ser modificados después de su creación, a diferencia de los objetos 'bytes' (que son inmutables).
# Los valores iniciales son:
# '\x38' (decimal 56, carácter '8')
# '\x19' (decimal 25, un carácter de control no imprimible)
# '\x61' (decimal 97, carácter 'a')
# '\x62' (decimal 98, carácter 'b')
# '\x39' (decimal 57, carácter '9')
# '\x40' (decimal 64, carácter '@')

print(cadena_bytes[0]) # Salida: 56
# Comentario: Al acceder a un elemento individual de un 'bytearray' por su índice (posición),
# Python devuelve el valor DECIMAL de ese byte. El primer byte (índice 0) es '\x38', cuyo valor decimal es 56.

# un caracter convertido a punto de codigo unicode (para ascii es su decimal )
print(ord('8')) # Salida: 56
# Comentario: La función 'ord()' toma una cadena de UN solo carácter ('8' en este caso)
# y devuelve su punto de código Unicode (que para caracteres ASCII es su valor decimal).
# Esto verifica que el carácter '8' tiene un valor decimal de 56, coincidiendo con el byte en la posición 0.

print(cadena_bytes[2]) # Salida: 97
# Comentario: Accedemos al byte en el índice 2 (el tercer byte) del 'bytearray'.
# El tercer byte es '\x61', cuyo valor decimal es 97.

# un caracter convertido a punto de codigo unicode (para ascii es su decimal )
print(ord('a')) # Salida: 97
# Comentario: Usamos 'ord()' con el carácter 'a'.
# Devuelve su punto de código Unicode, que es 97. Esto confirma la correspondencia
# entre el carácter 'a' y el valor 97 del byte en la posición 2.

# chr() es lo opuesto a ord(). Toma un número y te devuelve el carácter correspondiente.
#  numero entero a caracter unicode
print(chr(97)) # Salida: a
# Comentario: La función 'chr()' toma un número entero (97) y lo convierte
# en el carácter Unicode correspondiente. El número 97 representa el carácter 'a'.

# Modificación de un elemento del bytearray
cadena_bytes[2] = ord('c')
# Comentario: Aquí se modifica el byte en el índice 2 del 'bytearray'.
# El valor 'ord('c')' obtiene el valor decimal del carácter 'c' (que es 99).
# Dado que 'cadena_bytes' es un 'bytearray' (y por lo tanto mutable),
# podemos cambiar su contenido. El byte que antes valía 97 ('a') ahora vale 99 ('c').

print(cadena_bytes[2]) # Salida: 99
# Comentario: Imprimimos el valor del byte en el índice 2 después de la modificación.
# La salida es 99, confirmando que el valor se ha actualizado correctamente.

print(cadena_bytes) # Salida: bytearray(b'8\x19cb9@')
# Comentario: Al imprimir el 'bytearray' completo, podemos ver el efecto de la modificación.
# La representación muestra que el tercer byte ha cambiado de 'a' a 'c'.
# Antes era b'8\x19ab9@', ahora es b'8\x19cb9@'.



cad1 = bytearray(b'\x20\x19\x61')
cad2 = bytearray(b'\x62\x39\x40')
print(cad1)#bytearray(b' \x19a')
print(cad2)#bytearray(b'b9@')
print(cad1+cad2)#bytearray(b' \x19ab9@')

print(cad1 *2)#bytearray(b' \x19a \x19a')




