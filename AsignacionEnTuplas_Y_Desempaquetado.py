#Asignación en tuplas
"""
Python permite la asignación en tuplas. Es decir,
que podemos asignar los elementos de una tupla a
varias variables a la vez.
"""
a, b = (3, 4) # Asignamos los elementos de la tupla a cada variable
print(a, b)
#3 4

#es muy conveniente en bucles for. desempaquetado en tuplas
t = [(1, 2), (3, 4), (5, 6)] # lista de tuplas
for x, y in t: # asigna el primer digito a x y el segundo a y
    print (x + y, end= ' ')# luego lo suma  y le pone un espacio
# 3 7 11
print("\n")
"""
estamos recorriendo una lista de tuplas 
y las vamos asignando a dos variables simultáneamente (x, e y) 
que luego utilizamos dentro del for para ir sumándolas. 
Este proceso se llama desempaquetado en tuplas.
"""

#Util en recorrer dos listas en paralelo:
la = [10, 20, 30, 40] # lista
lb = [5, 25, 50, 10] # lista
for a, b in zip(la, lb):  # con zip las combina en una tupla
                          # y desempaqueta en for
    m = max(a, b) # max(a, b) devuelve el máximo entre a y b
    print(m , end=' ')
#10 25 50 40
"""
recorremos dos listas usando la función zip (cremallera) que, 
en cada iteración, nos devuelve una tupla cogiendo un elemento de cada
una de las listas. Luego, dentro del for, 
comparamos cuál de los dos elementos es mayor con la función max 
y lo mostramos por pantalla.
"""


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