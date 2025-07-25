

#Métodos de las listas
"""
Method Description
append() Añade un elemento al final de la lista
clear() Borra los elementos de la lista.
copy() Devuelve una copia de la lista.
count() Devuelve el número de veces que se encuentra un elemento en la lista
extend() Añade los elementos de una lista a otra.
index() Devuelve el índice del primer
elemento cuyo valor es el especificado.
insert() Añade un elemento en la posición especificada.
pop() Borra el elemento en la posición especificada y devuelve el elemento eliminado.
remove() Elimina el elemento con el valor especificado
reverse() Invierte el orden de la lista.
sort() Ordena la lista
"""

#Los métodos más usados son:
#len(), append(), pop(), insert() y remove().
"""
Como las listas son colecciones mutables, muchos de
los métodos de éstas la modifican in-place en lugar de
crear una lista nueva, como por ejemplo sort() o reverse().
"""
miLista1 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
miLista2 = ["Maria", 2, 5.56, True] # Se puede mezclar diferentes elementos
print(miLista1[1]) # Para un elemento en concreto, se empieza a contar desde la posición cero.
print(miLista1[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, “Angel y María”.

"""
Si escribimos tres números (inicio:fin:salto) en lugar
de dos, el tercero se utiliza para determinar cada
cuantas posiciones añadir un elemento a la lista,
Ejemplo:
"""
miLista1 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
miLista2 = ["Maria", 2, 5.56, True] # Se puede mezclar diferentes elementos
print (miLista1[1]) # Para un elemento en concreto, se empieza a contar desde la posición cero.
print (miLista1[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, “Angel y María”.

#Listas anidadas
"""
Una lista puede contener cualquier tipo de objeto.
Esto incluye otra lista. Una lista puede contener
sublistas, que a su vez pueden contener sublistas, y
así hasta una profundidad arbitraria.
Estas operaciones sirven para matrices pequeñas y
operaciones sencillas. Sin embargo, si queremos
operar con matrices grandes o en problemas
complejos, Python dispone de librerías para este tipo
de usos. El principal ejemplo es Numpy, un proyecto
de código abierto con gran respaldo de la comunidad
científica y de numerosas organizaciones privadas. El
proyecto Numpy es uno de los principales
responsables del tremendo éxito de Python en el
campo de Data Science. 
"""