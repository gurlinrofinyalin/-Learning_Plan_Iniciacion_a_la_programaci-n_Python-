la = [1, 2, 3, 4, 5]
print(type(la))#<class 'list'>
lb = list('abcde')
print(type(lb))#<class 'list'>
lc = list('ABCDE')
print(type(lc))#<class 'list'>

#soporta cualquier número de argumentos posicionales zlist

#zip() comprime iterables(en este caso listas ) en tuplas por índice.
# la, lb, lc son listas
zlist = list(zip(la, lb, lc))# crea una lista de tuplas

print(type(zlist))#<class 'list'>  zlist es una lista de tuplas

print(zlist)# es una lista de tuplas
# [(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'), (4, 'd', 'D'), (5, 'e', 'E')]

primer_elemento = zlist[0]# Índice 0 acceso a la primera tupla
print(primer_elemento)# (1, 'a', 'A')
print(type(primer_elemento))# <class 'tuple'>
segundo_elemento = zlist[1]# Índice 1 acceso a la primera tupla
print(segundo_elemento)# (2, 'b', 'B')
print(type(segundo_elemento))# <class 'tuple'>

print('-----------------------------------------')
a, b, c = zip(*zlist) # El * en zip desempaqueta lista de tuplas
print(type(a))
print(a)# (1, 2, 3, 4, 5)
print(b)#('a', 'b', 'c', 'd', 'e')
print(c)#('A', 'B', 'C', 'D', 'E')
print('-----------------------------------------')
print(la, lb, lc, sep = '\n')
'''
[1, 2, 3, 4, 5]
['a', 'b', 'c', 'd', 'e']
['A', 'B', 'C', 'D', 'E']
'''
print('-----------------------------------------')
print(la, lb) # Seperador por defecto es espacio
#[1, 2, 3, 4, 5] ['a', 'b', 'c', 'd', 'e']