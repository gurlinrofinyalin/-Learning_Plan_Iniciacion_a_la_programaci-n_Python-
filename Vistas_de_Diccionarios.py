#Vistas en diccionarios

"""
Otro uso muy común del desempaquetado en tuplas es navegar por
los objetos de un diccionario. Anteriormente vimos un ejemplo donde
recorríamos un diccionario a través de sus claves.
Ahora vamos a ver cómo recorrer todos sus elementos a la vez:
"""
print("\n")
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values))
print(d)# {'nombre': 'Guido', 'apellidos': 'van Rossum', 'edad': 60}
for k, v in d.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v)) # sien k la clave  y v el valor

"""
nombre: Guido
apellidos: van Rossum
edad: 60


el método dict.items nos devuelve una tupla (clave, valor) 
correspondiente a una entrada del diccionario en cada 
iteración del for
"""






"""
Tened en cuenta que a partir de Python 3.5, el
método dict.items devuelve una vista de los
elementos del diccionario, es decir, no devuelve los
objeto en sí hasta que no los recorramos o los
convirtamos explícitamente en listas. 

#dict_keys(['nombre', 'apellidos', 'edad'])   esto es una vista

Otros métodos tienen el mismo comportamiento son dict.keys y
dict.values, que devuelven vistas de las claves y los
valores respectivamente.
"""
for k in d.keys():
    print(k, end= ' ')
#apellidos edad nombre
print("\n----------")
for v in d.values():
    print(v, end= ' ')
#Van Rossum 60 Guido
print("\n----------")

#Si en lugar de recorrerlos, intentamos extraer todas las claves
#o elementos vemos que no devuelven una lista, sino que son vistas del diccionario
print(d.keys()) # extrae una vista de las claves del diccionario porque no lo recorremos
#dict_keys(['nombre', 'apellidos', 'edad'])
print("\n----------")
print(type(d.keys())) #<class 'dict_keys'>
print("\n----------")
print(d.values())
#dict_values(['Guido', 'van Rossum', 60])
print("\n----------")
print(type(d.values())) #<class 'dict_values'>
print("\n----------")


print(d.items())
#dict_items([('nombre', 'Guido'), ('apellidos', 'van Rossum'), ('edad', 60)])
print("\n----------")
print(type(d.items()))#<class 'dict_items'>

print("\n----------")
"""   SE TIENEN QUE RECORRER 
O 
ENVOLVERLAS EN LISTAS PARA PODER INDEXARLAS

Tened en cuenta que no podemos acceder
directamente a estas listas, sino que tenemos que, o
bien recorrerlas como hemos visto antes, o bien
envolverlas en listas para poder indexarlas,
trocearlas, etc.:
"""

""" ERROR
d.keys()[1] # No podemos acceder a una vista de diccionario
------------------------------------
Error. Texto omitido por simplicidad
TypeError: 'dict_keys' object does not support indexing
"""
# ACCESO envolver en una lista  list( vista de llaves )[indice]
list(d.keys())[1] # 'edad'

print(list(d.keys())[1]) # apellidos
print(list(d.values())[1]) # van Rossum