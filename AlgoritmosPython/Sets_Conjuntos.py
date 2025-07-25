#Los sets son un tipo de datos en Python que permite
#almacenar múltiples elementos en una misma variable

# los set se representan con el tipo de dato set

# sintaxis   {val1,val2 ..., valn}


#Crear un conjunto
thisset = {"apple", "banana", "cherry"}

# NO SON ORDENADOS  no estamos seguros de como aparecen los elementos
print(thisset)#{'banana', 'apple', 'cherry'}

print(type(thisset))#<class 'set'>

#Declaración
mi_conjunto= {"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}


mi_conjunto={"Angel", "Sara", "Pilar"}
#Añadir un nuevo elemento
mi_conjunto.add("Antonio")
print(mi_conjunto)# {'Pilar', 'Sara', 'Antonio', 'Angel'}


ni_conjunto={"Angel","Sara", "pilar"}
#Añadir varios elementos mi_conjunto
mi_conjunto.update({"Fran", "Maria"})
print(mi_conjunto)#{'Pilar', 'Sara', 'Fran', 'Maria', 'Angel', 'Antonio'}


mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
#Unión de colecciones
# EN LOS CONJUNTOS NO EXISTEN LOS VALORES DUPLICADOS
# si  hay repeticiones solo sale una vez, ejemplo Angel que esta en los dos sets
union= mi_conjunto  | mi_conjunto2
print(union)#{'Manolo', 'Angel', 'Sara', 'Pilar', 'Juan'}



#Intersección de conjuntos
# CREAMOS UN CONJUNTO CON LOS VALORES QUE ESTABAN EN LOS DOS CONJUNTOS
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
interseccion= mi_conjunto & mi_conjunto2
print(interseccion)#{'Angel'}


letras = "aaabbbcccdddeeefff"
#ELiminamos duplicados pero desordenamos
# elimina duplicados
# estan desordenados
print(set(letras))#{'f', 'a', 'e', 'b', 'd', 'c'}

#ELiminamos duplicados pero ORDENAMOS pero en una LISTA []
print(sorted(set(letras)))# ['a', 'b', 'c', 'd', 'e', 'f']


# TEST DE MEMBRESIA  vamos si esta el elemento en
print("th" in "Python")#True
#PYTHON LOS INCORPORA TANTO EN SECUENCIA COMO EN DICCIONARIOS LOS TEST


#Diferencia de conjuntos
# la diferencia  son los elementos
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
diferencia= mi_conjunto - mi_conjunto2
# en este caso de mi_conjunto quitaria los elementos duplicados en mi_conjunto2
# en este caso solo Angel , asique del mi_conjunto  solo no estan en el
# mi_conjunto2 Pilar y Sara
#VAMOS QUE DEVUELVE LOS ELEMENTOS DEL mi_conunto, que no esten en mi_conjunto2
print(diferencia)#{'Pilar', 'Sara'}

# la diferencia  son los elementos
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
diferencia= mi_conjunto2 - mi_conjunto
# en este caso de mi_conjunto2 quitaria los elementos duplicados en mi_conjunto
# en este caso solo Angel , asique del mi_conjunto2  solo no estan en el
# mi_conjunto Juan Manolo
#VAMOS QUE DEVUELVE LOS ELEMENTOS DEL mi_conunto2, que no esten en mi_conjunto
print(diferencia)#{'Juan', 'Manolo'}


# Comprobar si un elemento esta en un conjunto
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
print("Angel" in mi_conjunto)#True         #Devuelve true o false

# Para comprobar con la interseccion & si un elemento esta en los dos conjuntos
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
print("Angel" in (mi_conjunto & mi_conjunto2)) #True


# Si queremos con la Union | si un elemento esta en alguno de los 2 conjuntos
# quitando la repeticion , asi tiene mas rendimiento
mi_conjunto={"Angel", "Sara", "Pilar"}
mi_conjunto2={"Angel", "Manolo", "Juan"}
print("Sara" in (mi_conjunto | mi_conjunto2)) #True

# Recorrer
# Acceso a elementos
miSet =  {"manzana", "naranja", "platano"}
for x in miSet:
    print(x)
#naranja
#platano
#manzana

# comprobar si esta el elemento en el
miSet =  {"manzana", "naranja", "platano"}
print("platano" in miSet)# True


# agregar 1 elemento a un conjunto usamos el metodo add
miSet =  {"manzana", "naranja", "platano"}
miSet.add("pera")
print(miSet)# {'naranja', 'manzana', 'pera', 'platano'}

# agregar varios  elementos a un conjunto
miSet =  {"manzana", "naranja", "platano"}
miSet.update({"pera","coco","piña"})
print(miSet)#  {'piña', 'naranja', 'platano', 'coco', 'manzana', 'pera'}


# Cantidad de elementos en un conjunto
miSet =  {"manzana", "naranja", "platano"}
print(len(miSet))# 3



# borrar elementos a un conjunto  REMOVE  genera un error KeyError si no esta el elemento
miSet =  {"manzana", "naranja", "platano"}
try:
    miSet.remove("platano")
except KeyError:
    print("no esta el elemento ")
print(miSet)#{'naranja', 'manzana'}


# borrar elementos a un conjunto  DISCARD no genera un error si no esta el elemento
miSet =  {"manzana", "naranja", "platano"}
miSet.discard("platano")
print(miSet)#{'naranja', 'manzana'}


# borrar EL ULTIMO elemento a un conjunto
# NO SABEMOS CUAL ES EL ULTIMO ELEMENTO LOS SETS NO ESTAN ORDENADOS
# AUNQUE PODEMOS SABER CUAL SE ELIMINO PORQUE DEVUELVE EL ELEMENTO
miSet =  {"manzana", "naranja", "platano"}
elemento_eliminado = miSet.pop()
print(elemento_eliminado)#manzana
print(miSet)#{'naranja', 'manzana'}


# VAciar de elementos el set
miSet =  {"manzana", "naranja", "platano"}
miSet.clear()
print(miSet)#set()



# BOrra el set completamente y  si accedes cuando esta borrado da error NameError
miSet =  {"manzana", "naranja", "platano"}
del miSet
try:
    print(miSet)
except NameError:
    print("no existe el conjunto ")


# Unir dos o mas conjuntos
#EXCLUYEN ELEMENTOS DUPLICADOS    UNION
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
# estan desordenados
print(set3)# {1, 2, 3, 'b', 'a', 'c'}




# insertar los elementos del conjunto set2 al conjunto set1
#EXCLUYEN ELEMENTOS DUPLICADOS   UPDATE
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
# estan desordenados
print(set1)#{1, 2, 3, 'a', 'b', 'c'}

# crear un conjunto con el constructor
miSet = set (("manzana", "naranja", "platano"))
print(miSet)#{'platano', 'manzana', 'naranja'}


# SET  es MUTABLE
# FROZENSET  es INMUTABLE

#
que = {"azul, amarillo, verde"}
print(type(que))# <class 'set'>  MUTABLE
fset = frozenset({"azul, amarillo, verde"})
print(type(fset))#<class 'frozenset'> INMUTABLE
print(fset)# frozenset({'azul, amarillo, verde'})


# Creo una empresa con los clientes
iniciales
empresa = Empresa(clientes=[hector,
juan])
# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)
print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")
print("\n==BORRAR CLIENTES POR DNI==")
# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")
# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)
==LISTADO DE CLIENTES==
[<__main__.Cliente object at
0x0000023F567B42E8>,
<__main__.Cliente object at
0x0000023F567B4320>]
==MOSTRAR CLIENTES POR DNI==
Hector Costa Guzman
Cliente no encontrado
==BORRAR CLIENTES POR DNI==
Cliente no encontrado
Juan Gonzalez Marquez > BORRADO
==LISTADO DE CLIENTES==
[<__main__.Cliente object at
0x0000023F567B42E8>]



