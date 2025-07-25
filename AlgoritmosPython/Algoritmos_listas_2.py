#Hay varias formas de unir o concatenar dos o más listas en Python.

#Una de las formas más fáciles es mediante el uso del operador + .
#Unir dos listas:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)#['a', 'b', 'c', 1, 2, 3]


#Otra forma de unir dos listas es agregando todos los elementos de list2 a list1, uno por uno:
#Anexar list2 a list1:
list1 = ["a","b","c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)# usamos append para  agregar los elementos de list2 a list1
print(list1)# ['a', 'b', 'c', 1, 2, 3]


#O podemos usar el método extend(), cuyo propósito es agregar elementos de una lista a otra lista:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
#Use el método extendO para agregar list2 al final de list1:
list1.extend(list2) # agregamos los elementos de list2 en  list1
print(list1)#['a', 'b', 'c', 1, 2, 3]




#Estructuras de datos
# También es posible usar el constructor list() para hacer una nueva lista.
thislist = list(("Manzana", "plátano", "cereza"))
print(thislist) #['Manzana', 'plátano', 'cereza']


lista1=[1,2,3]
lista2=[4,5,6]
lista1+=lista2
print(lista1)

lista1 *= 2
print(lista1)

print(len(lista1))

print(min(lista1))

print(max(lista1))

try:
    ver = [1, 2, 3]+4
except TypeError:
   print("no sirve ")
"""
Operaciones con listas
Las listas soportan muchos de los operadores y funciones de Python por
defecto presentados en los temas anteriores.
"""

try:
    ver = [1, 2, 3]+[4]
except TypeError:
   print("sirve ESTO NO SALE ")
else:
    print("sirve")
    print(ver)



#METODOS MAS UTILIZADOS EN LAS LISTAS
"""


append() Añade un elemento al final de la lista
clear() Borra los elementos de la lista.
Copy() Devuelve una copia de la lista.
count() Devuelve el número de veces que se encuentra un
elemento en la lista extend() Añade los elementos de una lista a otra.
index() Devuelve el índice del primer elemento cuyo valor es el especificado.
insert() Añade un elemento en la posición especificada.
pop() Borra el elemento en la posición especificada y devuelve el elemento eliminado.
"""

miLista = ["Angel", "Maria", "Manolo","Antonio", "Pepe"]
miLista2 = ["nombre", 2, 5.56, True] #Se pueden mezclar diferentes elementos.

#Para un eLemento en concreto, se empieza a contar desde La posición cero.
print(miLista[1])# Maria
#Empezando desde cero incluido hasta ,el dos sin incluir,esto es, "Angel y María".
print(miLista[0:2])#['Angel', 'Maria']
"""
Como las listas son colecciones mutables, muchos de los métodos de éstas
la modifican in-place en lugar de crear una lista nueva, como por ejemplo
sort o reverse.
"""


l = [99, True, "una lista", [1, 2]]
mi_var = l[0:2]
print(mi_var)# [99, True]
mi_var = l[0:4:2] # empieza indice 0, hasta 3 , salta de 2 en 2
print(mi_var)# [99, 'una lista']
#Como en el ejemplo anterior, pero en el caso de que sea cero,
# si no pongo se sobreentiende el [:2] es igual que   [0:2]
print(miLista[:2])#['Angel', 'Maria']

#Desde el elemento [1] incluido, hasta el tres sin incluir,
print(miLista[1:3])# ['Maria', 'Manolo']

#Desde el elemento [2] hasta el final
print(miLista[2:])#['Manolo', 'Antonio', 'Pepe']

# LA ULTIMA POSICION ES EL  INDICE -1
#Desde el final que seria el -1 , la segunda posición que seria -2
print(miLista[-2])#Antonio

#Lista completa.
# seria como poner print(miLista)
print(miLista[:]) #['Angel', 'Maria', 'Manolo', 'Antonio', 'Pepe']
print(miLista)# ['Angel', 'Maria', 'Manolo', 'Antonio', 'Pepe']
"""
Si escribimos tres números (inicio:fin:salto) en lugar de dos, el tercero se
utiliza para determi nar cada cuantas posiciones añadir un elemento a la
lista, Ejemplo:
"""
print(miLista)# ['Angel', 'Maria', 'Manolo', 'Antonio', 'Pepe']
miLista.append("Antonio") #Añade el elemento al final de la lista.
print(miLista)# ['Angel', 'Maria', 'Manolo', 'Antonio', 'Pepe', 'Antonio']

print(miLista)#['Angel', 'Maria', 'Manolo', 'Antonio', 'Pepe', 'Antonio']
miLista.insert(2, "Sandra")#Añade el elemento en la posición [2].
print(miLista)# ['Angel', 'Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio']

print(miLista)#['Angel', 'Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio']
miLista.extend(["Sara", "Diego"])#Concatena La nueva Lista a la anterior.
print(miLista)#['Angel', 'Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'Diego']


#Me dice en qué posición está "Antonio", en este caso 3,
# osease devuelve  la posicion
#si hay más elementos "Antonio", nos da el primero.
print(miLista)#['Angel', 'Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'Diego']
#                  0        1        2          3        4
print(miLista.index("Antonio"))#4  indice 4

#Esta este elemento en la Lista?.
# Imprime true o false dependiendo de si esta o no
print("pepe" in miLista)# Falsem  no esta pepe en la lista


#Nota: pop() devuelve el elemento eliminado mientras que remove() no lo hace.
print(miLista)#['Angel', 'Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'Diego']
miLista.remove("Angel")#ELimina un elemento de la lista. en este caso Angel el primero
print(miLista)#['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'Diego']
# NO DEVUELVE EL ELMENTO

#Nota: pop() devuelve el elemento eliminado mientras que remove() no lo hace.
print(miLista)#['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'Diego']
elementodevuelto = miLista.pop() #ELimina el "último" elemento de una Lista. En este caso Diego el ultimo
print(miLista)#['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara']
print(elementodevuelto)#Diego



#Puedo crear una lista concatenando los elementos de otras listas:

#Crea una Lista nueva que es el resultado de concatenar Las dos anteriores.
# ['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'nombre', 2, 5.56, True]
miLista3= miLista  +  miLista2

miLista4=[4, 6, 7] * 2 #Me crearía una lista como esta [4, 6, 7, 4, 6, 7]

print(miLista[:])# ['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara']
print(miLista2[:])# ['nombre', 2, 5.56, True]
print(miLista3[:])# ['Maria', 'Sandra', 'Manolo', 'Antonio', 'Pepe', 'Antonio', 'Sara', 'nombre', 2, 5.56, True]
print(miLista4[:])# [4, 6, 7, 4, 6, 7]

#Puedo crear una lista concatenando los elementos de otras listas:
Listas=[lista1, lista2]
print(lista1)#[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(lista2)#                                       [4, 5, 6]
print(Listas)#[[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6], [4, 5, 6]]

#Para ordenar listas:

lista3=[2,5,32,8,45,3,1]
print(lista3)#[2, 5, 32, 8, 45, 3, 1]
lista3.sort()#Estas dos funciones no funcionan si mezclamos números y strings.
print(lista3)#[1, 2, 3, 5, 8, 32, 45]

#Para ordenar en orden inverso:
print(lista3)#[1, 2, 3, 5, 8, 32, 45]
lista3.reverse()#Estas dos funciones no funcionan si mezclamos números y strings.
print(lista3)#[45, 32, 8, 5, 3, 2, 1]


#DEL  La palabra clave del elimina el índice especificado:
thislist = ["Manzana", "plátano", "cereza"]
del thislist[0] # elimina el indice 0 que es Manzana
print(thislist)#['plátano','cereza']
# si se accede al indice que no existe igual da error
try:
    print(thislist[4])
except IndexError:
    print("ese elemento en ese indice no existe")



#La palabra clave del también puede eliminar la lista por completo:
thislist = ["Manzana", "plátano", "cereza"]
del thislist
# si se accede a el despues lanza una excepcion
try:
    print(thislist)
except NameError:
    print("la lista no esta definida")


#El método clearO vacía la lista:
thislist = ["Manzana", "plátano", "cereza"]
thislist.clear()
print(thislist)# []  # no da error al acceder a una lista vacia


#Podemos utilizar otros conceptos de indexación,
# como el slicing o el stride para modificar vanos elementos de una lista
lista=["texto2","texto3"]
print(lista)#["texto2","texto3"]
lista += ["texto4", "textos", "texto6"]
print(lista)# ['texto2', 'texto3', 'texto4", 'texto5', 'texto6']|

print(lista[0:3])#['texto2', 'texto3', 'texto4']

# metemos en el indice 0 1 2 los numeros 1 2 3
lista[0:3]= [1, 2, 3]# sustituimos
print(lista)# ['texto2', 'texto3', 'texto4", 'texto5', 'texto6']|
#  indices        0        1          2          3          4
print(lista)# [1, 2, 3, 'textos', 'texto6']


print(lista[0:3])#[1, 2, 3]
print(lista)# ['texto2', 'texto3', 'texto4", 'texto5', 'texto6']|
#  indices        0        1          2          3          4
lista[0:3] = [1,2] # seria como quitar 1 elemento porque elegimos 3 indices
# 0 1 2 y solo le damos  una lista con 2  elementos
print(lista)# [1, 2, 'textos', 'texto6']

print(lista)# [1, 2, 'textos', 'texto6']
lista[2:2] = [3,4,5] # sustituimos el elemento 2 por 3 4 5
# osease sustituimos el 3 por el 3 4 5
print(lista)#[1, 2, 3, 4, 5, 'textos', 'texto6']

print(lista)#[1, 2, 3, 4, 5, 'textos', 'texto6']   tenemos 7 elementos
lista[0:6] =[] # seria vaciar los elementos  0 1 2 3 4 5 menos el indice 6
print(lista)#['texto6']   el indice 6 es el ultimo




