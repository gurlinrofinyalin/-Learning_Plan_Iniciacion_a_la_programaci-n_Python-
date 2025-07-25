#Diccionarios
"""
Los diccionarios, también llamados matrices asociativas,
deben su nombre a que son colecciones que relacionan una clave
y un valor.

Un diccionario es una colección desordenada, modificable e indexada.


En Python, los diccionarios se escriben entre llaves y tienen
claves y valores.

Son estructuras de datos que nos permiten almacenar valores de
diferente tipo (números, strings, etc) e incluso listas y
otros diccionarios.

La principal característica de los diccionarios es que los datos
se almacenan asociados a una clave de tal forma que se crea una
 asociación de tipo clave-valor para cada elemento.

Los elementos almacenados no están ordenados.

Ejemplo: Crear e imprimir un diccionario.
"""
dic = {
"Nombre":"Santiago",
"Apellido":"Hernandez",
"Pais":"España",
"Ciudad":"Madrid"
}
print(dic)#


# Otra forma de definir diccionarios con la funcion dict()
#  la clave no esta  entre comillas
dic2 = dict(
Nombre="Santiago",
Apellido="Hernandez",
Pais="España",
Ciudad="Madrid"
)
"""
En Python un diccionario sería similar a lo que en Java un 
hashtable o en PHP un array asociativo.


El primer valor se trata de la clave y el segundo del
valor asociado a la clave. 

Como clave podemos utilizar cualquier valor inmutable: 
podríamos usar números, cadenas, booleanos, tuplas… 
pero no listas o diccionarios, dado que son mutables. 

Esto es así porque los diccionarios se implementan como tablas
hash, y a la hora de introducir un nuevo par clave/valor en 
el diccionario se calcula el hash de la clave para después poder 
encontrar la entrada correspondiente rápidamente. 

Si se modificara el objeto clave después de haber sido 
introducido en el diccionario, evidentemente, su hash también
cambiaría y no podría ser encontrado.
"""
