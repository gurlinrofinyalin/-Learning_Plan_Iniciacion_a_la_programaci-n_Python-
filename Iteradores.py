#Iteradores
"""
los iteradores, y cuál es el protocolo que permite que
cualquier secuencia de Python pueda ser recorrida en un for.

sobrecargando un par de funciones, podemos dotar a nuestras propias
clases de esas capacidades de iteración.

Objetos Iterables
 podemos recorrer cualquier secuencia en un bucle for:
"""
from warnings import catch_warnings

# recorriendo una lista y elevando al cuadrado a cada elemento
for num in [1, 2, 3, 4, 5, 6]:
    print(num ** 2, end= ' ')
#1 4 9 16 25 36
print("\n---------")
# recorriendo la lista y dividiendo el elemento entre 2
for num in [12, 38, 99, 1]:
    print(num / 2, end= ' ')
#6.0 19.0 49.5 0.5

print("\n---------")
# recorremos el string que es un array , lo ponemos en mayuscula
for letra in 'Python':
    print(letra.upper(), end=' ')
#P Y T H O N
print("\n---------")


"""
De hecho, es posible recorrer estas secuencias porque son iterables 
El concepto de iterable es una generalización del término secuencia.
 Un objeto terable es un objeto que cumple una de estas condiciones:

• Está almacenado físicamente como una secuencia
• Produce un resultado detrás de otro en el contexto de una 
herramienta de iteración como un bucle for, una lista por comprensión, 
etc.

Otra manera de comprender el concepto de objeto iterable es entender 
que un iterable es, o bien una secuencia ordenada físicamente 
(como una lista, tupla, etc.) o bien un objeto que se comporta
virtualmente como una secuencia.



#El Protocolo de Iteración de Python

Pero, ¿qué significa que un objeto se comporta como una secuencia virtual? 
Básicamente significa que implementa un protocolo, llamado protocolo de
iteración, 
que define cómo tiene que comportarse un objeto de manera que sea 
capaz de devolver un elemento detrás de otro a demanda cuando queramos 
recorrerlo.

La mejor manera de entender el protocolo de iteración es verlo funcionar 
en los objetos builtin de Python. 

Los tipos builtin de Python son estructuras de datos
que han sido optimizadas y que, interiormente están
implementadas en C para aumentar su velocidad.
numeros int double 
Strings 
listas   []
diccionarios  {}  con clave valor
tuplas ()
sets{}   sin clave valor
ficheros 
booleanos none
tipos de unidades de programa funciones clases modulos


Nosotros lo vamos a ver con el tipo file, que lo usaremos para ir 
recorriendo un fichero línea a línea.

Primero, vamos a crear el fichero, que contendrá una versión recortada del 
Zen de Python:
"""
# aclaramos que esto se imprime en 4 lineas usando comillas y \
zen = '''\
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''
#  abrimos el archivo en modo escritura
# no se agrega se vuelve a escribir
f = open('archivos/short.zen.txt', 'w')
f.writelines(zen) # Escribe el fichero
f.close() # Cierra el fichero

#a leer ese fichero línea a línea
# abrimos el archivo en modo lectura
from pathlib import Path
file_name= 'short.zen.txt'
path = Path(f"./archivos/{file_name}")
print(type(path))# <class 'pathlib.PosixPath'>


f= open(path, 'r')
print(f.readline())
#'Bello es mejor que feo. \n'
print(f.readline())
#'Explícito es mejor que implícito.\n'
print(f.readline())
#'Simple es mejor que complejo. \n'
print(f.readline())
#'Complejo es mejor que complicado. \n'
print(f.readline()) # none
# Devuelve una cadena vacía cuando termina el fichero
print(f.close()) # Cierra el fichero
print("\n---------")
"""
El método readline nos permite ir leyendo el fichero
línea a línea hasta que nos encontremos una cadena
vacía.
"""





"""
De hecho, los ficheros en Python implementan un método 
que tiene un comportamiento muy parecido.

El método __next__ también lee una línea del fichero
cada vez que lo llamamos. 
Sin embargo, cuando finaliza el fichero, 
nos genera una excepción de tipo StopIteration.
"""

f = open('archivos/short.zen.txt', 'r')

try:
    print(type(f.__next__()))#<class 'str'>

    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())  # produce una excepcion StopIteration
                         # al finalizar el archivo
except StopIteration:
    print("Llegó al final del archivo.")
finally:
    f.close()  # cerrar el archivo
"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Iteradores.py", line 135, in <module>
    f.__next__()
StopIteration
"""
print("\n---------")
"""
Esta función __next__() es lo que llamamos el protocolo de iteración de Python. 
Cualquier objeto que implemente esta función para avanzar al siguiente
resultado y que lance la excepción StopIteration tras el último resultado 
es considerado como un iterador.

Esto implica que cualquier objeto que implementa estas dos reglas, 
puede ser incluido en un bucle for, en una lista por comprensión, etc. 
ya que lo que hacen en realidad estos mecanismos es ir llamando a la 
función __next__ en cada iteración.

De hecho, esto es lo que pasa con el tipo builtin de ficheros de Python: 
podemos recorrerlo en un bucle for para ir procesando sus líneas una a una:
"""
for linea in open('archivos/short.zen.txt'):
    print(linea.upper(), end='')
"""
BELLO ES MEJOR QUE FEO.
EXPLÍCITO ES MEJOR QUE IMPLÍCITO.
SIMPLE ES MEJOR QUE COMPLEJO.
COMPLEJO ES MEJOR QUE COMPLICADO.
"""


print("\n---------")

#La función next
"""
Para simplificar la iteración manual con __next__,
Python ofrece la función builtin next que nos permite
acceder a la iteración manual de __next__ más fácilmente. 
Lo que hace realmente 
la función next(obj) es llamar directamente a obj.__next()__:
"""
f = open('archivos/short.zen.txt', 'r')
print(type(f))#<class '_io.TextIOWrapper'>
try:
    print(f.__next__())# usamos next( objeto)  en vez de objeto.__next__()
    #'Bello es mejor que feo.\n'
    print(next(f)) # # función next(obj) es llamar directamente a obj.__next()__
    #'Explícito es mejor que implícito.\n'
    print(next(f)) # usamos next( objeto)  en vez de objeto.__next__()
    #'Complejo es mejor que complicado.\n'
    print(next(f))
    #'Complejo es mejor que complicado.\n'

    print(next(f))
except StopIteration:
    print("Llegó al final del archivo.")
finally:
    f.close()  # cerrar el archivo
"""
StopIteration Traceback(most recent
call last) <ipython-input-77-468f0afdf1b9> in <module>()
----> 1 next(f)
StopIteration
"""

print("\n---------")

# se puede hacer con esto sin saltos de linea strip()
#eliminar caracteres de los extremos (inicio y fin) de una cadena de texto.
with open('archivos/short.zen.txt', 'r') as f:
    for line in f:
        print(line.strip())

print("\n---------")







