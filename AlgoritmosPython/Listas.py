"""
Introducción
Hasta ahora hemos visto cómo guardar un dato en
una variable para poder trabajar posteriormente con
él.

Ahora vamos a ver las estructuras que posee
Python para poder trabajar con colecciones de datos.


Las estructuras de datos en Python se pueden
entender como un tipo de dato compuesto, debido a
que en una misma variable podemos almacenar no
sólo un dato, sino infinidad de ellos.

Dichas estructuras, pueden tener diferentes características y
funcionalidades.


Hay cuatro tipos de estructuras de recopilación de
datos en el lenguaje de programación Python:

desordenada: diccionarios
ordenada: lista
orden relevante cuando se define:  lista
no respeta el orden: conjunto

no duplicados:  conjuntos diccinario
duplicados: lista  tupla

inmutable: tupla
mutable/cualquier tipo contiene: lista, diccionario



####
En diccionarios  Como clave podemos utilizar cualquier valor inmutable:
podríamos usar números, cadenas, booleanos, tuplas…
pero no listas o diccionarios, dado que son mutables.

utilizarse como claves en un diccionario: tuplas
no utilizarse como claves en un diccinario : listas, diccionarios
#####


indexada o permitir busquedas: conjunto, diccionario
no indexada: listas (miraro bien ),  tupla, conjunto

tamaño variable: lista

expandir dinamicamentem añdir elementos   lista

extraccion genera un nuevo objeto : tupla

rapidez : tuplas
menos espacio: tuplas


contenido
un conjunto no puede incluir objetos mutables como listas,diccionarios,
 e incluso otros conjuntos.


#####Tipo de Colección
Elementos que puede contener
Restricciones importantes

#####Listas (list)
Cualquier tipo de dato, incluyendo: números, cadenas de texto, booleanos, None, otras listas, tuplas, diccionarios, conjuntos, objetos personalizados, etc.
Ninguna restricción en el tipo de sus elementos. Son colecciones ordenadas y mutables.

#####Tuplas (tuple)
Cualquier tipo de dato, incluyendo: números, cadenas de texto, booleanos, None, otras tuplas, listas, diccionarios, conjuntos, objetos personalizados, etc.
Ninguna restricción en el tipo de sus elementos. Son colecciones ordenadas e inmutables (una vez creadas, no se pueden modificar sus elementos, aunque los elementos internos mutables sí se pueden cambiar si son objetos como listas o diccionarios).

#####Conjuntos (set)
Solo elementos hasheables (inmutables). Esto incluye: números, cadenas de texto, booleanos, None, tuplas (si todos los elementos de la tupla también son hasheables), frozenset.
No pueden contener objetos mutables como listas, diccionarios u otros sets directamente, porque los elementos de un conjunto deben ser hasheables para que el conjunto funcione eficientemente (ya que el conjunto necesita calcular un hash de sus elementos para almacenarlos).

#####Diccionarios (dict)
Claves: Solo elementos hasheables (inmutables). Esto incluye: números, cadenas de texto, booleanos, None, tuplas (si todos los elementos de la tupla también son hasheables), frozenset.<br>Valores: Cualquier tipo de dato (igual que las listas y tuplas).
Las claves deben ser hasheables. Los valores no tienen restricciones y pueden ser mutables. Son colecciones no ordenadas (desde Python 3.7, mantienen el orden de inserción) que almacenan pares clave-valor.




se puede utilizar el operador []: listas , tuplas


matrices asociativas: diccionarios


• La lista (list); es una colección ordenada y modificable. Permite miembros duplicados.
• Tupla (tuple); es una colección ordenada e inmutable. Permite miembros duplicados.

• Conjuntos (Set); es una colección que no está ordenada ni indexada.
No hay miembros duplicados.
• Diccionario (Dictionary); es una colección desordenada, modificable e indexada.
No hay miembros duplicados.

Al elegir un tipo de colección, es útil comprender las propiedades de ese tipo.
Elegir el tipo correcto para un conjunto de datos en particular podría significar
un aumento en la eficiencia y seguridad.
"""




# Listas
"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.


Las listas en Python se representan con el tipo list y la sintaxis que se utiliza 
para definirlas consiste en indicar una lista de objetos separados entre comas y
encerrados entre corchetes: [obj1, obj2, ..., objn]

Las listas son estructuras de datos que nos permiten almacenar gran cantidad de valores 
(equivalentes a los arrays en otros lenguajes de programación). 

Se pueden expandir dinámicamente añadiendo nuevos elementos, es decir, 
la cantidad de valores que contendrán podrá variar a lo largo de la ejecución del programa.


Las listas pueden contener cualquier tipo de dato:
números, cadenas, booleanos… y también otras listas e incluso funciones, objetos, etc. 

Se pueden mezclar diferentes tipos de datos. 

Las listas son mutables.
Una de las características importantes de las listas es que se corresponden con una 
colección ordenada de objetos. 

El orden en el que se especifican los elementos cuando se define una lista es relevante 
y se mantiene durante toda su vida.

Sintaxis de las listas:
Crear una lista es tan sencillo como indicar entre corchetes y separados por comas, 
los valores que queremos incluir en la lista:
nombreLista=[elem1, elem2, elem3…]
"""

#Se pueden mezclar elementos de distinto tipo.
miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1,2]]
print(type(miLista))# <class 'list'>


#También se pueden crear desde strings:
print(list('Python'))# ['P', 'y', 't', 'h', 'o', 'n']

#Podemos acceder a cada uno de los elementos de la
#lista escribiendo el nombre de la lista e indicando el
#índice del elemento entre corchetes.
print(miLista[0]) # Imprimiría: Angel

"""
Si queremos acceder a un elemento de una lista incluida dentro de otra 
lista tendremos que utilizar dos veces este operador, primero para indicar a qué
posición de la lista exterior queremos acceder, y el segundo para seleccionar 
el elemento de la lista interior:
"""
miLista = ["una lista", [1, 2]]
mi_var = miLista [1][0] #
print(mi_var)# 1


#También podemos utilizar este operador para modificar un elemento de la lista
#si lo colocamos en la parte izquierda de una asignación:
miLista = [22, True]
miLista [0] = 99 # Con esto
print(miLista)# [99, True]  cambiamos el 22 por el 99


# Para imprimir toda la lista podemos poner:
print(miLista[:])# [99, True]
print(miLista)# [99, True]

# Se puede declarar una lista vacía, sin elementos.
#Como en Java, el primer elemento de la lista está en el índice o posición cero.
miLista3 = []
print(miLista3)# []

"""
Nota: Si pongo índices negativos lo que hace Python es contar desde el final hasta 
el principio empezando por -1, es decir, en mi caso el elemento “Angel” podría ser 
la posición [0] o la [-3]. 
en 

"""
miLista=["Angel", 43, 667767250]
print(miLista[0])#Angel
print(miLista[-3])#Angel

#Como en los strings.
#Si pongo:  miLista[-2:]  crea una lista con el -2:final
# final es -1, de izquierda a derecha
Lista2=miLista[-2:] #Me crea una sublista con los elementos [43, 667767250]
print(Lista2)# [43, 667767250]


#Podemos utilizar los  operadores vistos en el tema anterior para comparar listas
lista2 = ["t2","t1","t3"]

lista1=[1,2,3]

print(lista1)
print(lista2)
print(lista1== lista2)# False


print(lista1 in lista2)# False

print(lista1 is ["t2","t1","t3"])# False
print(lista1 is [1,2,3])# porque da False
"""
#Podemos utilizar los  operadores vistos en el tema anterior para comparar listas
lista2 = ["t2","t1","t3"]

lista1=[1,2,3]

print(lista1)
print(lista2)
print(lista1== lista2)# False


print(lista1 in lista2)# False

print(lista1 is ["t2","t1","t3"])# False
print(lista1 is [1,2,3])# porque da False


"""
# operador =  LOS DOS OBJETOS HACEN REFERENCIA AL MISMO ESPACIO DE MEMORIA
#dos variables hagan referencia al mismo objeto en Python,
# no necesitas un método de copia como list().
#  En su lugar, simplemente asignas una variable a la otra.
#Esto se conoce como asignación por referencia o crear un alias. Ambas variables "apuntarán" al mismo objeto en la memoria.
original_list = ["Manzana", "plátano", "cereza"]
# Asignar por referencia: 'alias_list' ahora apunta al MISMO objeto que 'original_list'
alias_list = original_list
print(f"Original: {original_list}, ID: {id(original_list)}")
print(f"Alias:    {alias_list}, ID: {id(alias_list)}")
# Comprobamos si son el mismo objeto con 'is'
print(f"¿'original_list' es 'alias_list'? {original_list is alias_list}") # Esto será True

# Ver qué pasa si modificamos uno de ellos
print("\n--- Modificando 'alias_list' ---")
alias_list.append("naranja")

print(f"Original después de modificar alias: {original_list}")
print(f"Alias después de modificar alias:    {alias_list}")

# Ambos han cambiado porque son el mismo objeto en memoria.




# Una lista puede contener una funcion
def func():
    print("Hola satan")

print(type(func))#<class 'function'>


lista = ["texto1","texto2",func]
print(lista)#['texto1', 'texto2', <function func at 0x7fec44cc44a0>]


# los elementos de una lista no tienen que ser unicos
# Puede repetirse el mismo elemento varias veces en la misma lista

lista = ["texto1","texto1","texto1"]
print(lista)#['texto1', 'texto1', 'texto1']

