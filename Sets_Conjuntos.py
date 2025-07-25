
# SETs, conjuntos
"""
Un conjunto es una colección de
ELEMENTOS UNICOS
que NO ORDENADA
NI INDEXADA,
por lo que no puede estar seguro de en qué orden aparecerán los elementos.

En Python, los conjuntos se escriben entre llaves.{}

como un diccionario pero  solo  con valores unicos y sin claves

Una vez que se crea un conjunto, no puede
cambiar sus elementos, pero puede agregar
nuevos elementos.
"""
# Declaración:
mi_conjunto = {"Angel", "Sara", "Pilar"}
mi_conjunto2 = {"Angel", "Manolo", "Juan"}

print(mi_conjunto , " de tipo ", type(mi_conjunto))
# {'Sara', 'Angel', 'Pilar'}  de tipo  <class 'set'>
print(mi_conjunto2 , " de tipo ", type(mi_conjunto2))
#{'Manolo', 'Angel', 'Juan'}  de tipo  <class 'set'>

print("\n-----------set-----------\n")
# Otra forma de declararlo
mi_conjunto3 = set(("Angel", "Sara", "Pilar"))
print(mi_conjunto3)# {'Sara', 'Angel', 'Pilar'}

print("\n----------add-------------\n")
# Para añadir un nuevo elemento:
print(mi_conjunto)# {'Pilar', 'Angel', 'Sara'}
mi_conjunto.add("Antonio")
print(mi_conjunto) #{'Pilar', 'Angel', 'Antonio', 'Sara'}
# NO SE SABE EL ORDEN COMO SE VE

print("\n-----------------------\n")
# Para añadir varios elementos:
print(mi_conjunto)#{'Angel', 'Pilar', 'Sara', 'Antonio'}
# NO SE SABE EL ORDEN COMO SE VE
mi_conjunto.update({"Fran", "María"})
print(mi_conjunto)#{'Pilar', 'Sara', 'María', 'Fran', 'Angel', 'Antonio'}
# NO SE SABE EL ORDEN COMO SE VE


print("\n-----------todos los elementos pero no repite si hay alguna repeticion------------\n")
# Unión de colecciones.
# SI HAY UN VALOR REPETIDO SOLO APARECERA UNA SOLA VEZ
print(mi_conjunto)#{'Sara', 'María', 'Pilar', 'Angel', 'Fran', 'Antonio'}
print(mi_conjunto2)#{'Angel', 'Manolo', 'Juan'}
union = mi_conjunto | mi_conjunto2
print(union)# COMO VEMOS Angel solo sale una vez
#{'Sara', 'Manolo', 'Pilar', 'Fran', 'Antonio', 'María', 'Angel', 'Juan'}

print("\n-----------solo los elementos que estan en los dos conjuntos ------------\n")
# Intersección de conjuntos:
# Nos crea otro conjunto con los valores que estaban duplicados en ambos conjuntos.
# En nuestro caso sólo Angel.
print(mi_conjunto)#{'Sara', 'María', 'Pilar', 'Angel', 'Fran', 'Antonio'}
print(mi_conjunto2)#{'Angel', 'Manolo', 'Juan'}
interseccion= mi_conjunto & mi_conjunto2
print(interseccion) # {'Angel'} ,solo se repetia Angel en los dos conjuntos

print("\n---todos los elementos menos los que estan en los dos conjuntos ----------------\n")
# Diferencia de conjuntos.
# Nos crea otro conjunto con los elementos que no están duplicados.
print(mi_conjunto)#{'Sara', 'María', 'Pilar', 'Angel', 'Fran', 'Antonio'}
print(mi_conjunto2)#{'Angel', 'Manolo', 'Juan'}
diferencia= mi_conjunto - mi_conjunto2
print(diferencia)#{'María', 'Antonio', 'Pilar', 'Sara', 'Fran'}
# Angel no sale porque era el que estaba en los dos

print("\n--------NO TIENEN INDICE LOS CONJUNTOS-------------\n")
# Para comprobar si un elemento está en un conjunto:

"Angel" in mi_conjunto # Devuelve true o false
# Recorra el conjunto e imprima los valores:
miSet = {"manzana", "banana", "cereza"}
for x in miSet:
    print(x)
"""
banana
manzana
cereza

No puede acceder a los elementos de un
conjunto haciendo referencia a un índice,
ya que los conjuntos no están ordenados,
los elementos no tienen índice.
"""


print("\n-----------------------\n")
# Obtenga la cantidad de elementos en un conjunto:
miSet = {"manzana", "banana", "cereza"}
print(len(miSet))# 3


print("\n---remove genera un error si el elemento a borrar no esta--------------------\n")
# Elimine "banana" utilizando el metodo remove() :
miSet = {"manzana", "banana", "cereza"}

print(miSet)#{'manzana', 'cereza', 'banana'}
miSet.remove("banana")# elimina el elemento
print(miSet)# {'manzana', 'cereza'}
"""
Si el elemento a eliminar no existe,
remove() generará un error.
"""

print("\n----discard() no genera error si no esta el elemento a borrar-------------------\n")
# Elimine "banana" utilizando el metodo discard() :
miSet = {"manzana", "banana", "cereza"}
print(miSet)#{'manzana', 'banana', 'cereza'}
miSet.discard("banana")
print(miSet)#{'manzana', 'cereza'}

"""
Si el elemento a eliminar no existe,
discard() NO generará un error.
"""
print("\n---pop elimina un elemento al final NO SABE CUAL ELIMINA--------------------\n")
# Elimine el último elemento utilizando el método pop() :
"""También puede usar el método pop() para eliminar un elemento,
pero este método eliminará el último elemento.
Recuerde que los conjuntos no están ordenados,
por lo que no sabrá qué elemento se elimina.
"""

miSet = {"manzana", "banana", "cereza"}
print(miSet)#{'cereza', 'manzana', 'banana'}
x = miSet.pop() #  no se sabe cual elimina ejmplo cereza
print(x) # se recoge el elemento elilminado ejemplo cereza
print(miSet)# {'manzana', 'banana'}


print("\n---------clear--------------\n")
# El método clear() vacía el conjunto:
miSet = {"manzana", "banana", "cereza"}
miSet.clear()
print(miSet)# set()


print("\n----------del error si se accede-------------\n")
# La palabra clave del borrará completamente el conjunto:
miSet = {"manzana", "banana", "cereza"}
del miSet
try:
    print(miSet)
except NameError:
    print(" no esta definido el conjunto")

print("\n----------union    excluye duplicados-------------\n")
# Unión de conjuntos
# El metodo union() devuelve un nuevo
#  conjunto con todos los elementos de ambos conjuntos:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  # estaran desordenados
print(set3)#{'c', 1, 2, 3, 'b', 'a'}

# Tanto union() como update() excluirán cualquier elemento duplicado.

print("\n------------update excluye duplicados-----------\n")
# El método update() inserta los elementos en set2 en set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)#   SE INSERTAN .update(SIGUE IGUAL)#
print(set1)#{1, 'b', 'c', 'a', 2, 3}
print(set2)#{1, 2, 3}

# Tanto union() como update() excluirán cualquier elemento duplicado.