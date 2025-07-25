#Tuplas

"""
Las tupas son un tipo de dato complejo y particular del lenguaje de programación Python.
Una tupla es un objeto idéntico a una lista excepto por las siguientes propiedades:

• Al igual que las listas, definen una colección ordenada de objetos, sin embargo, utilizan la
sintaxis (obj1, obj2, ..., objn) en lugar de [obj1, obj2, ..., objn]

• Las tuplas son inmutables, es decir, no se pueden modificar después de su creación.

• No permiten añadir, eliminar, mover elementos (no append, extend, remove)

• Sí permiten extraer porciones, pero el resultado de la extracción es una tupla nueva.

• No permiten búsquedas (no index)

• Permiten comprobar si un elemento se encentra en la tupla.

Las tuplas se representan dentro de Python con el tipo de dato tuple.

¿Qué utilidad o ventaja presentan las tuplas respecto a las listas?
• Más rápidas
• Manos espacio (mayor optimización)
• Formatean string.
• Pueden utilizarse como claves en un diccionario(las listas no).


La sintaxis básica de una tupla sería:
nombreTupla = (elem1, elem2, elem3…)

Los paréntesis son opcionales pero recomendables.

Las posiciones son como en las listas, el elem1 está en la posición 0, el elem2 en la 1, etc

Podemos utilizar el operador [] debido a que las tuplas, al igual que las listas,
forman parte de un tipo de objetos llamados secuencias.

Las cadenas de texto también son secuencias, por lo que no os extrañará que podamos
hacer cosas como estas:
"""
c = "hola mundo"
print(c[0]) # h
print(c[5:]) # mundo
print(c[::3]) # hauo

"""
Al ser inmutables, lógicamente no podemos hacer un append, pop, etc.
¿Cuándo utilizar una tupla en lugar de una lista?

USO 
Hay determinados casos de uso en los que puede ser recomendable utilizar una tupla en
 lugar de una lista:

• La ejecución del programa es más rápida cuando se manipula una tupla que cuando se
 trata de una lista equivalente. 
 (Esto probablemente no se note cuando la lista o tupla es pequeña).

• Si los valores de la colección van a permanecer constantes durante la vida del programa,
 el uso de una tupla en lugar de una lista protege contra la modificación accidental.
 
• Hay otro tipo de datos de Python que presentaremos próximamente llamado diccionario, 
que requiere como uno de sus componentes un valor inmutable.
 Una tupla puede ser utilizada para este propósito, mientras que una lista no puede serlo.
 """



#Acceso a elementos de tupla
"""
Puede acceder a los elementos de tupla haciendo referencia al número de índice, 
entre corchetes: 
Ejemplo: Imprime el segundo elemento en la tupla:
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])#banana


#Indexación Negativa
"""
La indexación negativa significa comenzar desde el final, -1 refiere al último elemento,
-2 refiere al segundo último elemento, etc.
Ejemplo: Imprima el último elemento de la tupla
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])#cherry      el ultimo elemento


#Rango de índices
"""
Puede especificar un rango de índices especificando dónde comenzar y dónde terminar 
el rango. Al especificar un rango, el valor de retorno será una nueva tupla con los
 elementos especificados.
Ejemplo: Devuelve el tercer, cuarto y quinto elemento
 
Nota: La búsqueda comenzará en el índice 2 (incluido) y finalizará en el índice 5 
(no incluido).
Recuerde que el primer elemento tiene el índice 0.
"""
thistuple = ("apple", "banana", "cherry", "orange" , "kiwi", "melon", "mango")
print(thistuple[2:5])# ('cherry', 'orange', 'kiwi')    indice 2 3 4



#Rango de índices negativos
"""
Especifique índices negativos si desea comenzar la búsqueda desde el final de la tupla:
Ejemplo:
Este ejemplo devuelve los elementos del índice -4
(incluido) al índice -1 (excluido)
"""
thistuple = ("apple", "banana", "cherry", "orange" , "kiwi", "melon", "mango")
#               -7      -6          -5       -4        -3       -2       -1
print(thistuple[-4:-1])#                  ('orange', 'kiwi', 'melon')
# siendo los indices -4 -3 -2 sin el -1 que no esta incluido


# INMUTABLES
#Cambiar valores de tupla
"""
Una vez que se crea una tupla, no puede cambiar sus valores. 
Las tuplas son inmutables.
Pero hay una solución alternativa. Podemos convertir la tupla en una lista, 
cambiar la lista y volver a convertir la lista en una tupla.

#Ejemplo: Convierte la tupla en una lista para poder cambiarla:
"""
x = ("apple", "banana", "cherry")
y = list(x)# convertimos tupla en lista
y[1] = "kiwi" # agregamos  elemento
x = tuple(y) # convertimos en tupla
print(x)#


# Recorrer una tupla
"""
Puedes recorrer los elementos de la tupla utilizando un bucle for.
Ejemplo: Iterar a través de los elementos e imprimir los valores.
"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

"""
Comprobar si el artículo existe
Para determinar si un elemento específico está presente en una tupla, 
usa la palabra clave in:
Ejemplo: Comprueba si "manzana" está presente en la tupla.
"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


#Longitud de la tupla
"""
Para determinar cuántos elementos tiene una tupla, usa el método len():
Ejemplo: Imprime el número de elementos en la tupla.
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))# 3



#Agregar artículos
"""
Una vez que se crea una tupla, no puedes agregarle elementos. Las tuplas son inmutables.
Ejemplo: No puedes agregar elementos a una tupla.
"""
thistuple = ("apple", "banana", "cherry")
try:
    thistuple[3] = "orange" # This will
except TypeError: #raise an error
    print("la tupla es inmutable no puedes agregar un elemento")


#Crear tupla con un artículo
"""
Para crear una tupla con un solo elemento, debes agregar una coma después del elemento,
 a menos que Python no reconozca la variable como una tupla.
Ejemplo: Tupla de un artículo, recuerda la coma.
"""
thistuple = ("apple",) # esto es una tupla por la coma son 2 elementos
print(type(thistuple))#<class 'tuple'>

#NOT a tuplem sin la coma es un string en este caso
thistuple = ("apple")
print(type(thistuple))#<class 'str'>


#Eliminar elementos
"""
Nota: No puedes eliminar elementos en una tupla.
Las tuplas no se pueden cambiar, por lo que no puedes eliminar elementos de él, 
pero puedes eliminarlas por completo:

Ejemplo: La palabra clave del puede eliminar la tupla por completo.
"""
thistuple = ("apple", "banana", "cherry")
del thistuple
try:
    print(thistuple) #this will raise an error because the tuple no longer exists
except NameError:
    print("la tupla se elimino")



#Une dos tuplas
"""
Para unir dos o más tuplas, puedes usar el operador + :
Ejemplo: Une dos tuple.
"""
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)# ('a', 'b', 'c', 1, 2, 3)



#El constructor tuple ()
"""
También es posible usar el constructor tuple () para
hacer una tupla.
Ejemplo: Usando el método tuple () para hacer una tupla.
"""
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)#('apple', 'banana', 'cherry')
print(type(thistuple))#<class 'tuple'>

