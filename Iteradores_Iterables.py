#Iteradores e iterables
"""
Ahora que empezamos a entender cómo funciona el
protocolo de iteración en Python, vamos a
profundizar un poco más para entender como las
diferencias entre objetos iterables como las
secuencias que hemos visto al principio de la unidad
y los iteradores que acabamos de conocer

La función iter
Acabamos de ver como los ficheros en Python son
iteradores ya que implementan la función __next__.
Veamos si ocurre lo mismo con otros tipos de datos
como las listas:
"""
lista = [1, 2, 3]
try:
    next(lista) # una lista no es un iterador
except TypeError:
    print("una lista no es un iterador")
"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Iteradores_Iterables.py", line 17, in <module>
    next(lista)
TypeError: 'list' object is not an iterator
"""


"""
¿Qué es lo que ha pasado? La función next nos está
produciendo una excepción de tipo TypeError
diciéndonos que las listas nos son iteradores. ¿Pero,
entonces, como es posible que podamos recorrer
una lista en un bucle for?

 las listas son iterables, y con el error que acabamos de obtener está claro 
 que un iterable no es lo mismo que un iterador.
 
 las listas son objetos iterador porque tiene el metodo __next__
 que la permite ser iterada en bucles for etc 
 
 ITERADOR vd ITERABLE
  Por ello, es el momento de entender qué es un iterable 
  y en qué se diferencia de un iterador:

• Iterable: 
Un objeto iterable es un objeto que devuelve un iterador. 
Para ello implementa el método __iter__.

• Iterador: Un iterador es un objeto que implementa:
__next__() → para dar el siguiente valor.
__iter__() que devuelve self → para que pueda usarse en bucles for, 
iter(), etc.

 
Tener el método __iter__() que devuelve self
 Esto permite que se pueda usar en un for o con iter().

Tener el método __next__() que devuelve el siguiente valor
  O lanza StopIteration cuando se termina.
 




Como vemos, los objetos iterables no son iteradores, 
sino que devuelven iteradores cuando se les pide.
Veamos un ejemplo con nuestra lista:

"""
try:
    # si no usas un bucle for etc debes  usar  o llamar a __iter__()
    # o iter(li)
    # para obtener un iterable
    li = lista.__iter__()# arriba vemos que no se podia iterar
    # pero con el metodo  obj.__iter__() devolvemos un iterador
    print(type(li)) # <class 'list_iterator'>

    print(li.__next__()) #1   # entonces ya se puede iterar
    print(next(li)) #2
    print(next(li)) #3
    print(next(li)) # provoca excpecion
except StopIteration:
    print(" se acabo la lista ")
"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Iteradores_Iterables.py", line 65, in <module>
    print(next(li))
          ^^^^^^^^
StopIteration
"""


"""
Para simplificar la iteración manual, Python implementa la función iter.
De esta manera iter(obj_iterable) es equivalente a obj_iterable.__iter()__
"""
try:
    li = iter(lista)  # devolvemos un iterador
    print(type(li)) # <class 'list_iterator'>

    print(next(li)) #1
    print(next(li)) #2
    print(next(li)) #3
    print(next(li)) #  crea una excepcion
except StopIteration:
    print(" se acabo la lista ")
"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Iteradores_Iterables.py", line 63, in <module>
    print(next(li)) # provoca excpecion
          ^^^^^^^^
StopIteration
"""

"""
De hecho, lo que hacen los bucles for, las listas por
comprensión, etc. es llamar a la función __iter__ del
objeto iterable que van a recorrer antes de empezar a
hacerlo. Con esto obtienen el iterador que es lo que
recorren de verdad.
Notad también que a medida que avanzamos
por un objeto iterador, vamos consumiéndolo y
ya no podemos volver atrás. Cuando llegamos
al final del iterador y obtenemos la excepción
StopIteration, decimos que hemos consumido el
iterador. Para volver a recorrerlo de nuevo,
tendríamos que pedirle al iterable que ha
creado el iterador que lo genere de nuevo.
"""
try:
    li = iter(lista)
    print(next(li))#1
    print(next(li))#2
    print(next(li))#3
    print(next(li))
except StopIteration:
    print(" se acabo la lista ")
"""
StopIteration    Traceback (most recent call last)
<ipython-input-100-deb767b63ff8> in ‹module>()
----> 1 next(li)
StopIteration:
Traceback (most recent call last)
"""

try:
    print(next(li))# Hemos consumido el iterador: no podemos iterar más
except StopIteration:
    print(" no se puede iterar mas , se acabo la lista ")
"""
StopIteration             Traceback (most recent call last)
<ipython-input-101-deb767b63ff8> in ‹module>( )
----> 1 next(li)
StopIteration:
"""

li = iter(lista)  # Generamos otro iterador para volver a recorrerlo
print(next(li))#1       este es nuevo
