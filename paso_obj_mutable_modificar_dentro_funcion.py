# pasamos una lista modificable
# modificamos la lista en el interior de la funcion
def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)
l = [1, 2, 3]
print(l) #[1, 2, 3]  resultado sin modificar
print(minimo(l)) # Modifica la lista aquí
print(l) #[1000, 2, 3]   resultado modificado





#EVITAR MODIFICAR LA LISTA
# hacemos una copia
# l es lista
def minimo(lista):
    lista[0] = 1000 # Modificamos la lista en el interior
    return min(lista)
lista = [1, 2, 3]
print(lista)#[1, 2, 3]
# AQUI LE  PASAMOS UNA COPIA DE LA LISTA A LA FUNCION
#  CON  lista[:]
print(minimo(lista[:])) # minimo modifica la lista aquí
print(lista)#[1, 2, 3]