# LISTAS
"""
La lista es un tipo de colección
ordenada
y modificable.

Es decir, una secuencia de valores de
cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""
miLista=["Angel", 43, 667767250]
# primer     0   1         2         3
miLista2 = [22, True, "una lista", [1, 2]]
miListac= miLista[2]#667767250
miLista2c= miLista2[3][1]#2
print(miListac,"\n")
print(miLista2c,"\n")
# MÉTODOS DE LAS LISTAS
# Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)# ['P', 'Y', 'T', 'H', 'O', 'N']    se convierte en lista
print("\n-----------\n")


# Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])
print("\n-----------\n")
#primer      0       1       2
# segundo   0 1     0 1     0 1
miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1][0]#3
miVar2 = miLista[1][1]#4
print(miVar,"\n")
print(miVar2,"\n")

print("\n-----------\n")
# Función con una lista como parámetro
def miFunccion(listaFrutas):
    for x in listaFrutas: # recorrer la lista
        print(x)

frutas = ["Manzana", "banana", "cereza"]
miFunccion(frutas)

"""
Manzana
banana
cereza

"""