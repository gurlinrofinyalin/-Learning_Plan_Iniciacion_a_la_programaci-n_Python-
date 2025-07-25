#Bytes y Bytearray

# Bytes es INMUTABLE
# Bytearray es MUTABLE

"""
¿Qué son los bytes en Python?
Un byte es una ubicación de memoria con un tamaño de 8 bits.
Un objeto bytes es una secuencia inmutable de bytes,
conceptualmente similar a un string.

El objeto bytes es importante porque cualquier tipo
de dato que se escribe en disco se escribe como una
secuencia de bytes, los enteros o las cadenas de
texto son secuencias de bytes.


 Lo que convierte la cadena de bytes en una cadena
 de texto o un número entero, es la forma en la que se interpreta.
 """

"""  video 
Un byte es una ubicación de memoria con un tamaño de 8 bits. Es una
secuencia inmutable de bytes, conceptualmente similar a un s
"""

# sintaxis b'<cadena de bytes>'
cadena_bytes = b'\x02\x1f'
print(cadena_bytes) # Salida: b'\x02\x1f'
# Comentario: Esto define una cadena de bytes (objeto 'bytes')
# utilizando la sintaxis de escape hexadecimal '\x'.
# '\x02' representa el byte con el valor decimal 2.
# '\x1f' representa el byte con el valor decimal 31 (que es 15 + 16 = 31).
# La 'b' inicial indica que es un literal de bytes.

"""
calculamos que 1F en hexadecimal es 31 en decimal:
El sistema hexadecimal (base 16) usa 16 símbolos: los dígitos del 0 al 9, 
y luego las letras A, B, C, D, E, F para representar los valores del 10 al 15.
Aquí está la equivalencia de las letras:
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
Para convertir un número hexadecimal a decimal, multiplicas cada dígito por 
una potencia de 16, dependiendo de su posición, 
y luego sumas los resultados. 
Las posiciones se cuentan desde la derecha, empezando en 0.

Para el número hexadecimal 1F:
        posicion 1                   posicion 0
1F =           1                          F  
     1 * (16^1)            +        15 * (16^0) 
     1 * 16 = 16                    15 * 1 = 15
          16               +               15      = 31

Dígito de la derecha (F):                           LA F 
Este dígito está en la posición 0 (16^0).
El valor decimal de F es 15.
Cálculo: 15 * (16^0) = 15 * 1 = 15

Dígito de la izquierda (1):                          el 1
Este dígito está en la posición 1 (16^1). 
El valor decimal de 1 es 1.
Cálculo: 1 * (16^1) = 1 * 16 = 16

Finalmente, sumamos los resultados de cada posición:
15 (del dígito F) + 16 (del dígito 1) = 31

Así es como 1F hexadecimal se convierte en 31 decimal.
"""



cadena_bytes = b'\x02\x1f'
print(type(cadena_bytes)) # Salida: <class 'bytes'>
# Comentario: Esto confirma que la variable 'cadena_bytes' es de tipo 'bytes'.
# Las cadenas de bytes se utilizan para trabajar con datos binarios directamente.

# numero entero -> cadena representacion binaria (prefijado 0b)
print(bin(543)) # Salida: 0b1000011111
# La función 'bin()' convierte un número entero (543) a su representación binaria
# en formato de cadena, prefijado con '0b'.
# 543 en decimal es 1000011111 en binario.


print(type(bin(543))) # Salida: <class 'str'>
# Esto demuestra que el resultado de 'bin()' es una cadena (string), no un tipo numérico.
# Es una representación textual del valor binario.

# hay que añadir el padding de ceros a la izquierda
# 00000010 | 00011111
# Esto muestra visualmente cómo los dos bytes (0x02 y 0x1F) se verían en binario.
# 0x02 es 00000010 en binario.
# 0x1F es 00011111 en binario.

# numero entero -> cadena representacion hexagesimal(prefijado 0x)
print(hex(543)) # Salida: 0x21f
# La función 'hex()' convierte un número entero (543) a su representación hexadecimal
# en formato de cadena, prefijado con '0x'.
# 543 en decimal es 21F en hexadecimal.

num_bytes = b'\x02\x1f'
# Se define nuevamente la misma secuencia de bytes para una demostración posterior.

print(num_bytes) # Salida: b'\x02\x1f'
# Se imprime el objeto de bytes.
# Los caracteres '\x02' y '\x1f' se muestran así porque son caracteres
# no imprimibles o de control en ASCII, por lo que Python los representa
# con su escape hexadecimal.

print(type(num_bytes)) # Salida: <class 'bytes'>
#  Confirma de nuevo que 'num_bytes' es un objeto de tipo 'bytes'.

print(int.from_bytes(num_bytes, "big")) # Salida: 543
# Este es un punto clave. 'int.from_bytes()'
# convierte una secuencia de bytes en un número entero.
# El argumento "big" especifica el orden "big-endian", lo que significa que el byte
# más significativo (el que vale más) está al principio.

# Cálculo: (valor del primer byte * 256) + (valor del segundo byte)
# (0x02 * 256) + (0x1f) = (2 * 256) + 31 = 512 + 31 = 543.
# Esto demuestra que la secuencia de bytes b'\x02\x1f' representa el número entero 543.

# otra forma de definir cadenas de bytes con la funcion bytes()
cadena_bytes2 = bytes(3)


print(cadena_bytes2) # Salida: b'\x00\x00\x00'
# El constructor 'bytes()' cuando se le pasa un único argumento entero (como 3),
# crea un objeto de bytes de esa longitud (3 bytes)
# e inicializa todos los bytes con el valor nulo (0x00).
# Es útil para crear búferes de bytes vacíos o inicializados a cero.


# son lo mismo uno en big y otro en little
# en big se transmite el byte con el valor mas grande
# y en little se transmite con el valor mas bajo
# en big se manda primero el byte mas grande \x02 512 de los 43
# aclaramos que como \x02  es un 2 decimal , seria base 256, serian 2 x 256 = 512
print(int.from_bytes(num_bytes, "big")) # Salida: 543

# en little se manda primero el byte mas pequeño \x1fm 31 de los 543
num_bytes_little= b'\x1f\x02'
print(int.from_bytes(num_bytes_little, "little"))# Salida: 543

"""
EXPLICACION DE 
print(int.from_bytes(num_bytes, "big")) # Salida: 543
# Este es un punto clave. 'int.from_bytes()'
# convierte una secuencia de bytes en un número entero.
# El argumento "big" especifica el orden "big-endian", lo que significa que el byte
# más significativo (el que vale más) está al principio.




### Orden de Bytes: Big-Endian vs. Little-Endian
Cuando un número ocupa más de un byte de memoria 
(como el 543, que necesita dos bytes: \x02 y \x1f), 
hay 2 formas principales de organizarlos en la memoria o al transmitirlos:

##Big-Endian ("extremo grande" primero):
El byte más significativo (el que tiene mayor valor, como el 02 en 02 1F) se almacena 
o transmite primero (al principio).

Piensa en cómo escribimos los números: el 5 en 543 es el "más significativo" porque representa 500, y lo escribimos primero. Big-endian es lo más parecido a nuestra forma de escribir.

Ejemplo para 543 (\x02\x1f):
Byte 1: \x02 (el 256)
Byte 2: \x1f (el 31)


ACLARACION 
Explicación más clara del cálculo con b'\x02\x1f'
          b'     \x02              \x1f '
                2× (256 ^ 1)        31× (256 ^ 0)
                 2×(256)             31× (1)
Suma total:      512        +       31   =  543
     
Cuando interpretamos una secuencia de bytes como un número entero, 
cada byte es como un "dígito" en una base 256 (no base 10 como nuestros números normales, ni base 16 como hexadecimal, sino base 256 porque un byte puede tener 256 valores diferentes, de 0 a 255).
Para b'\x02\x1f' en big-endian:
Byte 1 (\x02): Es el byte más significativo. Su valor decimal es 2.
Este byte ocupa la posición de 256 elevado a 1 
(el equivalente a las "decenas" o "centenas" pero en base 256).
Contribución al total: 2× (256 ^ 1)  osease = 2 × 256 =  512

Byte 2 (\x1f): Es el byte menos significativo. Su valor decimal es 31.
Este byte ocupa la posición de 256 ^ 0
(el equivalente a las "unidades" en base 10).
Contribución al total: 31× (256 ^ 0) osease = 31 × 1   = 31


Suma total: 512+31=543

Así que, el \x02 es el byte que se va a multiplicar por 256 (dando 512), 
y \x1f es el byte que se va a multiplicar por 1 (dando 31).



##Little-Endian ("extremo pequeño" primero):
El byte menos significativo (el que tiene menor valor, como el 1F en 02 1F) 
se almacena o transmite primero (al principio).

Es como si escribieras 543 como 345. 
Es menos intuitivo para nosotros, 
pero muy común en la arquitectura de procesadores (especialmente Intel x86/x64).
Ejemplo para 543 (\x02\x1f): 
Si se almacenara en little-endian, se vería como \x1f\x02 en la memoria/transmisión.

Byte 1: \x1f (el 31)
Byte 2: \x02 (el 256)

¿Qué pasaría si no estuviera al principio (si fuera Little-Endian)?
#### IMPORTANTE 
Si el orden fuera Little-Endian, la secuencia de bytes para 543 sería b'\x1f\x02'.

Si tú le pasaras b'\x1f\x02' a int.from_bytes() 
y le dijeras que lo interpretara como "big-endian", obtendrías un resultado incorrecto:

num_bytes_little = b'\x1f\x02' # Estos bytes representan 543 en Little-Endian
"""

"""
# ¡Error de interpretación! Le estamos diciendo que es big-endian cuando no lo es.
valor_incorrecto = int.from_bytes(num_bytes_little, "big")
print(valor_incorrecto)
# Cálculo: (0x1f * 256) + 0x02 = (31 * 256) + 2 = 7936 + 2 = 7938
# Salida: 7938 (¡Incorrecto si el número original era 543 y estaba en little-endian!)
Para interpretar b'\x1f\x02' (que es 543 en little-endian) correctamente, tendrías que especificarlo a int.from_bytes():

 

num_bytes_little = b'\x1f\x02' # Los bytes que representan 543 en Little-Endian

valor_correcto = int.from_bytes(num_bytes_little, "little")
print(valor_correcto)
# Cálculo: (0x02 * 256) + 0x1f = (2 * 256) + 31 = 512 + 31 = 543
# Salida: 543 (¡Correcto!)
¿Por qué tiene que estar al principio (si usamos "big-endian")?
No es que "tenga que estar al principio" siempre, 
sino que debes indicarle a Python (o al sistema que esté leyendo los bytes) 
cuál es el orden en el que se organizaron esos bytes originalmente.

Si los bytes fueron generados o transmitidos en orden Big-Endian, 
entonces int.from_bytes() debe recibir el argumento "big" para que los interprete 
correctamente.
Si los bytes fueron generados o transmitidos en orden Little-Endian, 
entonces int.from_bytes() debe recibir el argumento "little".

La consistencia es clave. 
Si no se ponen de acuerdo en el orden de los bytes, 
el número resultante será incorrecto.

¿Cuándo se usa cada uno?
Big-Endian: Es el orden de red estándar (Network Byte Order) 
y es común en protocolos de Internet (como IP, TCP, UDP) 
y en algunos formatos de archivo. 
También se usa a veces como el orden predeterminado en entornos de procesadores 
Motorola (aunque esto es menos común ahora).

Little-Endian: Es el orden predominante en la arquitectura de procesadores x86/x64 
(Intel y AMD), que es la base de la mayoría de los ordenadores personales actuales.
Por eso, int.from_bytes() necesita ese argumento "big" o "little": 
para saber cómo "montar" los bytes individuales en un único número entero.
"""

#Transformando tipos de datos en bytes

# cadena de texto en bytes
texto = "Hola mundo"#
print(type(texto))#<class 'str'>
print(texto)#Hola mundo

texto_bytes = b'Hola mundo'#
print(type(texto_bytes))#<class 'bytes'>
print(texto_bytes)#b'Hola mundo'


# Estos bytes se interpretan como A, B y C en ASCII
ABC = b'\x41\x42\x43'
# Aquí defines una cadena de bytes.
# Cada secuencia '\xNN' representa un byte cuyo valor hexadecimal es NN.
# En este caso:
# '\x41' es el valor hexadecimal 41, que en ASCII corresponde al carácter 'A'.
# 16 x 4 +1 = 65   osease A
# '\x42' es el valor hexadecimal 42, que en ASCII corresponde al carácter 'B'.
# 16 x 4 +2 = 66   osease B
# '\x43' es el valor hexadecimal 43, que en ASCII corresponde al carácter 'C'.
# 16 x 4 +3 = 67   osease C



print(type(ABC)) # Salida: <class 'bytes'>
# Esto confirma que 'ABC' es un objeto de tipo 'bytes'.
# Los objetos 'bytes' son secuencias inmutables de bytes, utilizadas para datos binarios.

print(ABC) # Salida: b'ABC'
# Al imprimir una cadena de bytes, Python intenta decodificar los bytes a caracteres
# ASCII si son imprimibles. Como 0x41, 0x42 y 0x43 son los códigos ASCII de 'A', 'B' y 'C',
# Python los muestra directamente como b'ABC' para mayor legibilidad.

print(int("41", base=16)) # Salida: 65
# La función 'int()' con el argumento 'base=16' interpreta la cadena "41" como
# un número hexadecimal y lo convierte a su valor decimal equivalente.
# Hexadecimal 41 = (4 * 16^1) + (1 * 16^0) = 64 + 1 = 65.
# 65 es el valor decimal del carácter 'A' en la tabla ASCII.

print(int("42", base=16)) # Salida: 66
# Comentario: Similarmente, "42" hexadecimal es 66 decimal. 66 es el valor ASCII de 'B'.

print(int("43", base=16)) # Salida: 67
# Comentario: "43" hexadecimal es 67 decimal. 67 es el valor ASCII de 'C'.

cadena_bytes = b'\x20\x19\x61\x62\x39\x40'
#              b'    \x19  a    b   9   @'
# Otra cadena de bytes con diferentes valores hexadecimales:
# '\x20': Espacio (decimal 32)
# '\x19': Símbolo de control (decimal 25) - no imprimible
# '\x61': 'a' (decimal 97)
# '\x62': 'b' (decimal 98)
# '\x39': '9' (decimal 57)
# '\x40': '@' (decimal 64)

# COMO IMPRIMO ESO # b'\x19ab9@' con b'\x20\x19\x61\x62\x39\x40'

# Para imprimirlo de la forma b' ab9@', el primer byte '\x20' es un espacio.
# El segundo byte '\x19' NO es un carácter ASCII imprimible estándar. Python
# lo representará con su notación hexadecimal.
# Los demás sí son imprimibles.
print(cadena_bytes) # Salida: b' \x19ab9@'
# Python muestra el espacio y los caracteres imprimibles ('a', 'b', '9', '@')
# directamente. Sin embargo, el byte '\x19' no tiene una representación directa en ASCII
# como carácter imprimible, por lo que Python lo muestra de nuevo en su forma hexadecimal.

print(bytes(1)) # Salida: b'\x00'   el byte nulo (b'\x00') es un byte cuyo valor numérico es 0
# El constructor 'bytes()' con un solo argumento entero (aquí, 1) crea
# un objeto 'bytes' de esa longitud, inicializado con bytes nulos (valor 0x00).
# Esto crea una secuencia de un solo byte con valor cero.

print(type(bytes(1))) # Salida: <class 'bytes'>
# Comentario: Confirma que el resultado es un objeto 'bytes'.

cadena_bytes2 = b'\x00'  # no es un caracter imprimible ,  byte nulo (b'\x00') es un byte cuyo valor numérico es 0
print(cadena_bytes2) # Salida: b'\x00'
# Otra forma de definir directamente una cadena de bytes con un solo byte nulo.
# Python lo muestra como '\x00' porque el byte nulo tampoco es un carácter imprimible.





entero_cero = 0
# Convertimos el entero 0 a un byte
# Le decimos que ocupe 1 byte y que el orden no importa (o 'big' por convención)
bytes_del_cero = entero_cero.to_bytes(1, 'big')

print(f"El entero {entero_cero} es de tipo: {type(entero_cero)}") # Salida: El entero 0 es de tipo: <class 'int'>
print(f"Convertido a bytes es: {bytes_del_cero}") # Salida: Convertido a bytes es: b'\x00'
print(f"Su tipo es: {type(bytes_del_cero)}") # Salida: Su tipo es: <class 'bytes'>