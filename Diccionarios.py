
# DICCIONARIOS
"""Los diccionarios, también llamados
matrices asociativas, deben su nombre a
que son colecciones que relacionan 
una clave y un valor.
Un diccionario es una colección 
desordenada, 
modificable 
e indexada.

En Python, los diccionarios se escriben
entre llaves y tienen claves y valores.
"""
# Declaración de un diccionario
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print("\n--------------\n")
# A los valores almacenados en un diccionario se accede por su clave

peliculas = {"Love Actually": "Richard Curtis",
"Kill Bill": "Tarantino",
"Amélie": "Jean-Pierre Jeunet"}
# se consulta con la clave
print(peliculas["Love Actually"])# Richard Curtis

print("\n--------------\n")
# Reasignar valores a un diccionario
print(peliculas) # {'Love Actually': 'Richard Curtis', 'Kill Bill': 'Tarantino', 'Amélie': 'Jean-Pierre Jeunet'}
peliculas["Kill Bill"] = "Quentin Tarantino"  # cambiamos el valor
print(peliculas)# {'Love Actually': 'Richard Curtis', 'Kill Bill': 'Quentin Tarantino', 'Amélie': 'Jean-Pierre Jeunet'}

print("\n--------------\n")
# Usar una lista dentro de un diccionario:
miDiccionario3 = {"nombre":"Jordan",
                  "Equipo":"Bulls",
                  "Anillos":[1991, 1992,1993, 1996, 1997, 1998]}
# vemos el valor con la clave m en este caso e suna tupla
print(type(miDiccionario3["Anillos"]))#<class 'list'>
print(miDiccionario3["Anillos"])# [1991, 1992, 1993, 1996, 1997, 1998]


print("\n--------------\n")
# Usar una tupla dentro de un diccionario:
miDiccionario3 = {"nombre":"Jordan",
                  "Equipo":"Bulls",
                  "Anillos":(1991, 1992,1993, 1996, 1997, 1998)}
# vemos el valor con la clave m en este caso e suna tupla
print(type(miDiccionario3["Anillos"]))#<class 'tuple'>
print(miDiccionario3["Anillos"])# (1991, 1992, 1993, 1996, 1997, 1998)

print("\n--------------\n")
# Quitar valores de un diccionario NO TIENE PORQUE SER EL PRIMERO con POP

peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
print(peliculas)
# {'Love Actually': 'Richard Curtis', 'Kill Bill': 'Tarantino', 'Amélie': 'Jean-Pierre Jeunet'}
peliculas.pop("Love Actually")# quitamos el elemento
print(peliculas)
#{'Kill Bill': 'Tarantino', 'Amélie': 'Jean-Pierre Jeunet'}


print("\n--------------\n")
# Quitar valores de un diccionario NO TIENE PORQUE SER EL PRIMERO con PoP

peliculas2 = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
print(peliculas2)
# {'Love Actually': 'Richard Curtis', 'Kill Bill': 'Tarantino', 'Amélie': 'Jean-Pierre Jeunet'}
peliculas2.pop("Kill Bill")# quitamos el elemento
print(peliculas2)
#{'Love Actually': 'Richard Curtis', 'Amélie': 'Jean-Pierre Jeunet'}


print("\n--------------\n")
# Crear un diccionario a partir de dos listas:
lista_claves=["nombre", "edad"]
lista_valores=["Angel", 43]
# usando zip
diccionario = dict(zip(lista_claves , lista_valores))
print(diccionario)# {'nombre': 'Angel', 'edad': 43}


print("\n--------------\n")
# Para comprobar si una clave está en el diccionario:
print("nombre" in diccionario) #Devuelve true o false
# True  si que esta    {'nombre': 'Angel', 'edad': 43}


print("\n--------------\n")
# Imprima las claves del diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
for c in peliculas:
    print(c)#
"""  claves
Love Actually
Kill Bill
Amélie
"""


print("\n--------------\n")
# Imprima los valores del diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
for x in peliculas:
    print(peliculas[x])#

"""
Richard Curtis
Tarantino
Jean-Pierre Jeunet
"""

print("\n--------------\n")
# Imprima claves y valores del diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
for indice in peliculas:
    print("clave {} = valor {}".format(indice,peliculas[indice]))  #

"""
clave Love Actually = valor Richard Curtis
clave Kill Bill = valor Tarantino
clave Amélie = valor Jean-Pierre Jeunet
"""



print("\n-------items-------\n")
# Imprima claves y valores del diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
for clave, valor in peliculas.items():
    print(f"La clave es '{clave}' y el valor es '{valor}'.")
"""
La clave es 'Love Actually' y el valor es 'Richard Curtis'.
La clave es 'Kill Bill' y el valor es 'Tarantino'.
La clave es 'Amélie' y el valor es 'Jean-Pierre Jeunet'.
"""



print("\n----- enumerate ---------\n")
# Imprima la clave y el indice de la clave del  diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}

for indice, valor in enumerate(peliculas):
    print(f"Índice: {indice}, Valor: {valor}")
"""
Índice: 0, Valor: Love Actually
Índice: 1, Valor: Kill Bill
Índice: 2, Valor: Amélie

"""



print("\n--------------\n")
# Longitud de un diccionario:
peliculas = {"Love Actually": "Richard Curtis",
             "Kill Bill": "Tarantino",
             "Amélie": "Jean-Pierre Jeunet"}
print(len(peliculas))# 3

print("\n--------------\n")
# Agregar elementos a un diccionario: AL FINAL
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
miDiccionario["color"] = "red"
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

print("\n--------popitem------\n")
# Eliminar el último elemento insertado:
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
miDiccionario.popitem() # elimina el ultimo elemento
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang'}

print("\n--------------\n")
# La palabra clave del, elimina el elemento con el nombre de clave especificado:
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
del miDiccionario["model"]
print(miDiccionario)
# {'brand': 'Ford', 'year': 1964}

try:
    print(miDiccionario["model"])
except KeyError:
    print("si no esta la clave en el diccionario es un error")

print("\n--------------\n")
# La palabra clave del también puede eliminar completamente el diccionario:
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
del miDiccionario
try:
    print(miDiccionario)
except NameError:
    print(" cuando el diccionario se borra no puede consultarse despues")


print("\n--------------\n")
# La palabra clave clear() vacía el diccionario:
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
miDiccionario.clear()# vacia el diccionario
print(miDiccionario)# {}  sale vacio no es un error consultarlo


print("\n------copy--------\n")
# Copiar un diccionario
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
midict = miDiccionario.copy()
print(midict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print("\n--------dict------\n")
# Otra forma de copiar un diccionario
miDiccionario = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(miDiccionario)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
midict = dict(miDiccionario)
print(midict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print("\n--------------\n")
# Diccionarios anidados
child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}
#  contiene los  tres diccionarios anteriores
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)
"""
{'child1': {'name': 'Emil', 'year': 2004}, 
'child2': {'name': 'Tobias', 'year': 2007}, 
'child3': {'name': 'Linus', 'year': 2011}}
"""

print(myfamily["child1"])
# {'name': 'Emil', 'year': 2004}
print(myfamily["child2"])
#{'name': 'Tobias', 'year': 2007}
print(myfamily["child3"])
#{'name': 'Linus', 'year': 2011}
