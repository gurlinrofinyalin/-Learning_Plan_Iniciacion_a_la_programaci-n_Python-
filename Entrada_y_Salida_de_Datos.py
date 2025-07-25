#Entrada y salida de datos en Python

"""
Cómo recibir información del usuario en Python
A veces, podemos necesitar que el usuario
introduzca un valor por consola.

Para hacer esto, Python proporciona una función input().
Síntaxis:"""
input('prompt')
"""
Donde prompt es una cadena opcional (un mensaje) que se mostrará 
en el momento de realizar la petición de entrada.

Ejemplo 1: Pedir al usuario que introduzca su nombre.
"""
# Entrada input del usuario
nombre = input('Introduce tu nombre: ')
# Salida
print("Hola, " + nombre)
print(type(nombre))
"""
Salida:
Introduce tu nombre: Angel
Hola, Angel
<class ‘str’>

Nota: Python toma todo aquello que el usuario introduzca por medio de un input() 
como un string. 
Para convertirlo a cualquier otro tipo de datos, tenemos que convertir la 
entrada explícitamente. Por ejemplo, para convertir la entrada a int o float
tenemos que usar el método int() y float() respectivamente.


Ejemplo 2: Solicitar un número y sumarle una unidad.
"""
# Entrada por parte del usuario como número entero
num = int(input('Introduce un número: '))
add = num+1
# Salida
print(add)
"""
Salida:
Introduce un número: 34
35


Cómo pedir varios valores de una sola vez
Podemos tomar múltiples entradas a la vez, usando el método map()
"""
#split() es un método de cadena (string) en Python. Su función principal es dividir
# una cadena en una lista de subcadenas. Si no le pasas ningún argumento a split()
#  divide la cadena por cualquier espacio en blanco (espacios, tabulaciones, saltos de
#  línea) y descarta los espacios en blanco vacíos resultantes.


#map() una función Su propósito es aplicar una función dada a cada elemento de un iterable
# (como una lista) y devolver un objeto map (que es un tipo de iterable).

#En este  código, map(int, ...) le dice a Python que aplique la función int() a cada
# elemento que le llegue de la lista creada por split

# desempaquetado de secuencias (o tuplas/listas).
#El objeto map que devuelve map(int, ...) es un iterable.
#Python toma los elementos de ese iterable uno por uno y los asigna a las variables
# a la izquierda del signo =.   que son a b c

a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end = " ")
print(a, b, c)
"""
Salida:
Introduce un número: 2 3 4
Los números son: 2 3 4



Entrada de datos en listas, conjuntos, tuplas, etc.
En el caso de List y Set, la entrada puede tomarse del usuario de 2 maneras.
• Solicitando los elementos List/Set uno por uno usando los métodos append()/add().
• Usando los métodos map() y list() / set().

###Solicitando elementos de List/Set uno por uno
Para introducir los elementos de la Lista/Set uno por uno usaremos 
el método append()  en el caso de las Listas, 
y el método add() en el caso de los conjuntos.
"""
List = list()
Set = set()
l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del Set: "))

print("Introduzca los elementos de la lista:")
for i in range(0, 1): # pide
    list.append(int(input()))

print("Introduzca los elementos del Set:")
for i in range(0, 5): # pide 0 1 2 3 4 , 5 veces para el conjunto
    Set.add(int(input()))

print(list)
print(set)



""" Entrada de datos en listas, conjuntos, tuplas, etc.
Uso de los métodos map() y list() / set()
"""
# creamos una lista con los elementos que se reciban separados por espacios
# donde cada objeto sera guardado en una lista por split , entonces map  ejecutara
# la funcion int, a cualquier elemento de la lista convirtiendolo en entero
# despues esos elementos, se convierten en una lista
List = list(map(int, input("Introduzca los elementos de la lista:").split()))
# lo mismo que lo de arriba pero al final se convirten en un conjunto
Set = set(map(int, input("Introduzca los elementos del Set: ").split()))
print(List)
print(Set)

"""
Salida:
Introduzca los elementos de la lista: 2
Introduzca los elementos del Set: 3
[2]
{3}


Entrada de datos en una tupla
Sabemos que las tuplas son inmutables, no hay métodos disponibles para agregar elementos 
a las tuplas. 
Para agregar un nuevo elemento a una tupla, primero deberemos convertir la tupla en lista,
 luego agregaremos el elemento a la lista y nuevamente convertiremos la lista en una tupla.
"""
T = (2, 3, 4, 5, 6) # tupla
print("Tupla inicial")
print(T)

L = list(T) # convertimos
L.append(int(input("Introduzca el nuevo elemento: "))) # agregamos a la lista
L = tuple(L)  # convertimos en tupla
print("Tupla final")
print(T)

"""
Tupla inicial
(2, 3, 4, 5, 6)
Introduzca el nuevo elemento : 77
Tupla final
(2, 3, 4, 5, 6, 77)
Salida de datos en Python



Python proporciona la función print() para mostrar la salida a los dispositivos de 
salida estándar.
Sintaxis:
print(valor)
Ejemplo: salida de impresión de Python
"""
# Demostración de la función print()
print("GFG")
# Demostración de la función print() con espacios porque usamos la coma
print('G', 'F', 'G')
"""
GFG
G F G

# despues de cada caracter usando la coma se imprime un espacio
osease sep=' '
# despues del ultimo cvaracter se imprime un caracter de nueva  linea  OSEASE 
end


En el ejemplo anterior, podemos ver que en el caso de la segunda declaración de 
impresión hay un espacio entre cada letra y la declaración de impresión siempre 
agrega un carácter de nueva línea al final de la cadena. Esto se debe a que 
después de cada carácter se imprime el parámetro sep y al final de la cadena se 
imprime el parámetro  final. 

Intentemos cambiar este parámetro sep y end.
Ejemplo: Salida de Python Print con parámetro
personalizado de separación y finalización

end por defecto
El valor por defecto de end es el carácter de nueva línea (\n). 
Esto significa que, después de que print() termina de mostrar sus argumentos, 
automáticamente salta a la siguiente línea.

sep por defecto
El valor por defecto de sep (separator, separador) es un espacio simple (' '). 
Esto significa que, si pasas múltiples argumentos a print() separados por comas, 
Python los separará por un espacio cuando los muestre.
"""
print("GFG", end = "@")# cambiamos el \n  nueva linea , por una arroba al final de linea
# con lo cual se unen las dos lineas
print('G', 'F', 'G', sep = "#")# la separacion entre estos en vez de un espacio es una
# almuhadilla
"""
GFG@G#F#G


Salida de datos conformato
La salida de datos con formato en Python se puede hacer de diversas formas.
Uso de literales de cadena formateados

Podemos usar literales de cadena con formato,comenzando una cadena con f o F 
antes de abrir comillas o comillas triples. 
En esta cadena, podemos escribir expresiones de Python entre { } que pueden
referirse a una variable o cualquier valor literal.

Ejemplo: formato de cadenas de Python usando una cadena F
"""
# Declaramos una variable
name = "Antonio"
print(f'hola {name}!. Qué tal?')
"""
# Salida
Hola Antonio! Qué tal?



Usando format()
También podemos usar la función format() para formatear nuestra salida para que se vea
presentable. Las llaves { } funcionan como marcadores de posición. 
Podemos especificar el orden en que aparecen las variables en la salida.
Ejemplo: formato de cadena de Python usando la función format()
"""
# Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida estableciendo cual es cual al final
print('El valor de a es {} y b es {}'.format(a,b))
# estableciendo el orden con 1 y 2 en {}
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
# nombrando las variables al final del format  en vez de usar numeros
# para poder ordenarlas
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,
                                                                value_b=b,
                                                                sub_value=sub))
"""
El valor de a es 20 y b es 10
30 es la suma de 20 y 10
10 es la resta de 20 y 10
"""


"""
Uso del operador %
Podemos usar el operador '%'. 
Los valores de % se reemplazan con cero o más valores de elementos. 
El formateo usando % es similar al de 'printf' en el lenguaje de programación C.
%d – entero
%f – flotante
%s - cadena
%x - hexadecimal
%o – octal
Ejemplo:
"""

# Entrada de datos
num = int(input("Introduzca un número: "))
add = num+5
# Salida
print("La suma es %d" %add) # se usa %d  porque es un entero
"""
Introduzca un número: 2
La suma es 7
"""




#Especificadores de Formato Comunes con el Operador %
#Tipos Numéricos
#%d o %i: Entero decimal.
print("Mi edad es %d años." % 30) # Mi edad es 30 años.

#%f o %F: Flotante (número decimal). Por defecto, muestra 6 decimales.
print("Pi es aproximadamente %f." % 3.14159265) # Pi es aproximadamente 3.141593.

#%e o %E: Flotante en notación científica (exponencial).
print("Un número muy grande: %e." % 1234567890.0) # Un número muy grande: 1.234568e+09.

#%g o %G: Flotante (usa %f o %e según cuál sea más corto).
print("Un flotante corto: %g." % 0.00000123) # Un flotante corto: 1.23e-06.

#%x o %X: Entero en formato hexadecimal (minúsculas o mayúsculas).
print("10 en hexadecimal es %x." % 10) #10 en hexadecimal es a.
print("255 en hexadecimal es %X." % 255) # 255 en hexadecimal es FF.

#%o: Entero en formato octal.
print("8 en octal es %o." % 8) # 8 en octal es 10.

###Tipos de Cadena y Carácter
#%s: Cadena (string).
# También puede formatear otros tipos de datos al convertirlos implícitamente a cadena.
print("Hola, %s!" % "Mundo")# Hola, Mundo!

#Ejemplo (formateando un entero a cadena):
print("El número es %s." % 123) # El número es 123.

#%c: Carácter (espera un entero o una cadena de un solo carácter).
print("El carácter es %c." % 65) # El carácter es A. (65 es el ASCII de 'A')
print("El carácter es %c." % 'B') # El carácter es B.

#Otros Especificadores y Modificadores
#Además de los tipos, puedes usar modificadores para controlar el ancho, la precisión,
# el alineamiento, etc.:

#Ancho mínimo del campo: %(ancho)d, %(ancho)s, etc.
# Rellena con espacios si el valor  es más corto.
# "   123"
print("Número: %5d." % 123) # Número:   123. (tres espacios antes del 123)

#Precisión (para flotantes): %.(decimales)f
print("Pi con 2 decimales: %.2f." % 3.14159) # Pi con 2 decimales: 3.14.

#Precisión (para cadenas): %.(longitud_maxima)s Trunca la cadena si es más larga.
print("Cadena truncada: %.5s." % "larguisima")# Cadena truncada: larga.

#Relleno con ceros: %0(ancho)d
print("Número con ceros: %05d." % 123) # Número con ceros: 00123.

#Alineación: %-s para alineación a la izquierda.
# pone 6 espacios a la derecha de "Hola      "
print("Izquierda: %-10sDerecha" % "Hola") # Izquierda: Hola      Derecha

#Consideraciones Actuales
#Aunque el operador % sigue siendo funcional, en el código Python moderno,
# las f-strings (literal string interpolation) y el método .format() son las
#  opciones preferidas para el formateo de cadenas debido a su mayor legibilidad,
#  flexibilidad y seguridad.

#Ejemplo con f-strings (Python 3.6+):
nombre = "Alice"
edad = 30
pi = 3.14159265
# los dos puntos dividen la variable o valor  con el formateo .2f  x   etc
# se usa el f o F al inicio de las comillas
print(f"Hola, {nombre}! Tienes {edad} años.")
print(f"Pi con 2 decimales: {pi:.2f}")
print(f"10 en hexadecimal: {10:x}")
#Ejemplo con .format():
nombre = "Bob"
edad = 25
#   se debe de usar los dos puntos y el .format al final
print("Hola, {}! Tienes {} años.".format(nombre, edad))
print("Pi con 2 decimales: {:.2f}".format(3.14159))
print("10 en hexadecimal: {:x}".format(10))
#Ambas opciones son generalmente más legibles y menos propensas a errores que el
# operador %, especialmente cuando se manejan muchos valores o se requiere un
# formato complejo. Sin embargo, los fundamentos del formateo de tipos
# (entero, flotante, cadena, etc.) se mantienen en los tres métodos.