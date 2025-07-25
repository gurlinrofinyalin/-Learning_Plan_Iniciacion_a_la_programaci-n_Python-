#Bucles for y contadores
"""
Los bucles for de Python son más parecidos a los for-each
de otros lenguajes de programación.
Es decir, están destinados a recorrer los elementos de secuencias
o iterables.

Primero de todo, veamos cómo es un for al estilo C y
al estilo Pythónico.
La vía Pythónica es, en casi todos los casos, más legible
y más rápida de ejecutar.
"""
"""
# Versión C/C++. No lo uséis!

letras = list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(letras)):
    print(letras[i], end='')
#abedefghijkimnopqrstuvwxyz
"""
# Versión Pythónica. Más legible y rápido
letras = list('abcdefghijklmnopqrstuvwxyz')
for c in letras:
    print(c, end=' ')
#abedefghijkimnoparstuvwxyz


"""
La función range nos devuelve un listado de
números consecutivos de la longitud que le pasemos.
En este caso, le hemos pasado la longitud de la lista
de letras.
"""


# Ejemplos de uso de range
# HAY QUE ENVOLVERLO EN UNA LISTA
# O
# RECORRERLO CON UN FOR
print("\n-------------")
# se envuelve en una lista
print(list(range(5))) # Devuelve 5 elementos empezando en 0
#[0, 1, 2, 3, 4]
#   0 inicio por defecto 5 final  1 salto por defecto
print("\n-------------")
# se envuelve en una lista
print(list(range(-5, 5))) # Devuelve elementos en el rango -5, 5
#[-4, -3, -2, -1, 0, 1, 2, 3, 4]
#   -5 inicio 5 final  1 salto por defecto
print("\n-------------")
# se envuelve en una lista
print(list(range(-5, 5, 2))) # Elementos -5 a 5 en saltos de 2
#   -5 inicio 5 final  2 salto
#[-5, -3, -1, 1, 3]
"""
Por lo general, es siempre recomendable utilizar el bucle for 
    al estilo de Python. 
    Cuando empecemos a utilizar bucles nos veréis tentados
a utilizar los for de la manera típica de otros lenguajes. 
Salvo algunas excepciones, siempre es mejor hacerlo de la manera 
Pythónica.
A continuación, exponemos algunos de los esos
casos típicos donde los recién llegados a Python
tienen tendencia a programar bucles for no Pythónicos. 
También damos la alternativa que se debe utilizar.
"""

#recorrer varias listas simultáneamente.
import random
# ALACAMOS QUE
# letras = list('abcdefghijklmnopqrstuvwxyz')

print("\n----NO SE INCLUYE EL NUMERO A LA DERECHA DEL PRIMER :----")


# creamos 3 sublistas a apartior de trozos

l1 = letras[:8]
# desde el 0 al 7    8 letras
print(l1)# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

l2 = letras[8:16]
# desde el 8 al 15    8 letras
print(l2)# ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

l3 = letras[16:] #
# desde el 16 al final 25      10 letras
print(l3)# ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(random.shuffle(l1))  esto da none
#barajamos cada trozo
random.shuffle(l1)
print(l1)# ['a', 'f', 'e', 'g', 'c', 'b', 'd', 'h']
random.shuffle(l2)
print(l2)#['l', 'm', 'p', 'o', 'n', 'i', 'j', 'k']
random.shuffle(l3)


print("\n----")

# NO RECOMENDADO   NO  PYTHONICA
# tienes que preocuparte de la lista mas corta en longitud
for i in range(len(l1)):
    print(l1[i] +l2[i] +l3[i] , end=' ')
# fjt eoq hlw cmu bnz gpy dkx aiv

print("\n----")

# PYTHONICA  RECOMENDADA
# combina las listas y crea tipo  str
# CON ZIP no tienes que preocuparte de que una lista sea mas corta
# que otra, cuando acaba la lista mas corta se para solo
# coge el caracter de una lista l1 otro de l2 otro de l3
for a,b,c in zip(l1,l2,l3):
    #print(type(a))# str
    print(a+b+c , end=' ') # concatenamos con espacio al final
#fjt eoq hlw cmu bnz gpy dkx aiv

print("\n----")

"""
En este ejemplo estamos troceando la lista letras en
tres partes, luego barajamos cada una de las partes y
recorremos las tres listas simultáneamente para ir
mostrando en pantalla una letra de cada lista en cada
iteración. 


La versión Pythónica utiliza la función zip,
La única diferencia es que, en este caso, 
en lugar de unir dos listas estamos haciéndolo con tres. 

La gran ventaja de zip (además de ser más legible) es que 
no tenemos que preocuparnos de que todas las listas sean de igual 
longitud. 
Cuando una de las listas se termina, zip detiene la ejecución. 
En la alternativa no Pythónica, tendríamos que consultar las 
longitudes de cada lista y recorrer el bucle siguiendo 
los índices de la lista más corta.
"""





"""
Otro ejemplo típico en el que los programadores
noveles de Python tienden a hacer uso de for no
Pythónicos es cuando estamos haciendo
búsquedas de índices de los elementos de una
lista.  
"""
letras = list('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

# cada vez que se ejecuta el programa las letras se BARAJEAN
random.shuffle(letras) # baraja las letras

print(letras)
#['r', 'f', 't', 'h', 'a', 'o', 'g', 'i', 'm', 'q', 's', 'y', 'j', 'u', 'c', 'x', 'p', 'w', 'z', 'l', 'b', 'd', 'n', 'e', 'k', 'v']
#[0,   1,    2,   3,  4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25]
print(''.join(letras))# junta los elementos de la lista
# usa el espacio
# rqkmjgvzblsaoicfntxewduphy

print("\n----")
# NO RECOMENDABLE NO PYTHONICA
print("numero de elementos",len(letras))#numero de elementos 26
# se añade un espacio al final de elementos por la coma

print(range(len(letras)))#range(0, 26)

print(list(range(len(letras))))#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

for i in range(len(letras)):
    if letras[i] in vocales:
        print('{} en la posición {}'. format(letras[i], i))


"""
a en la posición 4
o en la posición 5
i en la posición 7
u en la posición 13
e en la posición 23
"""




print("\n----")
# PYTHONICA RECOMENDABLE
"""
En este ejemplo buscamos las posiciones de las vocales en un abecedario
 desordenado. Para ello usamos la función enumerate, que nos pide una
secuencia y nos devuelve la misma secuencia asociada a sus índices
"""
for i, letra in enumerate(letras):
    # i es la posicion de la letra
    #  si la letra existe en las vocales nos da la posicion
    # como estan barajadas , ejemplo a no es posicion 0
    if letra in vocales:
        print('{} en la posición {}'. format(letra, i))


"""
a en la posición 4
o en la posición 5
i en la posición 7
u en la posición 13
e en la posición 23
"""
print("\n----")









