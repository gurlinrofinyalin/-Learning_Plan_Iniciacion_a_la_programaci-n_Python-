# LISTAS ANIDADAS
"""
Una lista puede contener cualquier tipo de objeto. Esto incluye otra lista.

Una lista puede contener sublistas, que a su vez pueden contener sublistas,
y así hasta una profundidad arbitraria.

Las listas soportan anidamiento arbitrario. Esto significa que podemos
crear combinaciones anidadas de listas (listas dentro de listas) tan
profundas como necesitemos.

Es decir, una lista formada por listas.

Esta característica puede utilizarse para crear matrices.


El indexado es igual que en una lista plana,
pero ahora podemos anexar más índices para seleccionar elementos individuales.
"""
thislist=[['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]

print(thislist)# [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
print(thislist[0])#['a1', 'a2', 'a3']   indexamos la primera lista
print(thislist[1])#['b1', 'b2', 'b3']   indexamos la segunda lista
print(thislist[2])#['c1', 'c2', 'c3']   indexamos la tercera lista

print(thislist[1:])#[['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]
# indexamos la segunda y tercera fila porque es hasta el final


print(thislist[0][-1])# a3
#  acceso a la primera fila ultimo elemento
# siendo el [0] el acceso a la primera fila
# siendo [0][-1] el acceso al ultimo elemento porque es -1


print(thislist[2][0])# c1
#  acceso a la tercera fila primer elemento


"""
Estas operaciones sirven para matrices pequeñas y operaciones sencillas.
Sin embargo, si queremos operar con matrices grandes o en problemas
complejos, Python dispone de librerías para este tipo de usos. 

El principal ejemplo es Numpy, un proyecto de código abierto con gran 
respaldo de la comunidad científica y de numerosas organizaciones privadas. 

El proyecto Numpy es uno de los principales responsables del tremendo éxito de
Python en el campo de Data Science.
"""


#Además de crear matrices, el anidamiento de listas nos permite
# crear anidamientos no homogéneos como el siguiente
# Para acceder a los elementos de una sublista utilizamos la sintaxis [][]
#No hay límite en la cantidad de listas que podemos anidar, pueden ser
#tantas como soporte la memoria de nuestro sistema  RAM.
thislist = [["a1", "a2", "a3"],
            ["b1", "b2"],
            ["c1", "c2", "c3", "c4", "c5", "c6"]]
print(thislist)

lista = [1, [2 ,[ 3, 4], 5], 6]
print(lista[0])#1

print(lista[1])   #[2, [3, 4], 5]
print(lista[1][1])#    [3, 4]
print(lista[1][1][0])#  3

print(lista[2])#6

#Es importante entender que los operadores aplicarán sobre la primera lista
#y no aplicarán de manera recursiva.
print(lista)#           [1, [2, [3, 4], 5], 6]
print([3,4] in lista)#         False              esta en la lista TODA
print(lista[1])#            [2, [3, 4], 5]
print([3,4] in lista[1]) #      True               esta en el indice 1
