# Listas por comprension
# cramos  listas con objetos ya almacenados
# una lista por comprensioon es una expresion
# con una notacion particular que genera una lista

# las listas poor compresion cogen su nombre de la
# notacion por conjuntos

miLista=[1,2,3,4,5,6,7]
print(miLista)#[1, 2, 3, 4, 5, 6, 7]

## milista2 tiene Los valores (2*elemento)
# siendo elemento los valores de la Lista miLista
# recorre la lista miLista , y cada valor lo multiplica por 2
miLista2 = [2*elemento for elemento in miLista]
print(miLista2)#[2, 4, 6, 8, 10, 12, 14]


##Crear una Lista solo con los elementos pares
#recorre la lista miLista,  comprobando si el elemento de miLista es par
# si es para lo mete a la listaPares
listaPares = [elemento for elemento in miLista if elemento % 2 == 0 ]
print(listaPares)#[2, 4, 6]


##A La manera tradicional seria:
listaPares=[]
for i in miLista:
    if i%2==0:
        listaPares.append(i)# AÑADIMOS EL ELEMENTO
print(listaPares)#[2, 4, 6]



##Anidar iteraciones dentro de la lista
a=["a", "b", "c"]
b= (1,2,3)
print(type(a))#<class 'list'>
print(type(b))#<class 'tuple'>

##Para cada elemento de la lista a, me recorre todos los elmentos de b
# a es lo que se multiplica
# b es el multiplicador, primero 1 2 3
# serian como dos for anidados
c=[elemento1 * elemento2 for elemento1 in a for elemento2 in b]
print(c)#['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'c', 'cc', 'ccc']

d=[]
for elemento1 in a:
    for elemento2 in b:
        d.append(elemento1 * elemento2)

print(d)#['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'c', 'cc', 'ccc']





##Puedo incluso poner alguna condicion
c=[elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(c)#['a', 'aaa', 'b', 'bbb', 'c', 'ccc']

e=[]
for elemento1 in a:
    for elemento2 in b:
        if elemento2!=2:
            e.append(elemento1*elemento2)
print(e)# ['a', 'aaa', 'b', 'bbb', 'c', 'ccc']



#           col 1              col  2                col 3
m = [['a1', 'a2', 'a3'], ['bl', 'b2', 'b3'], ['c1', 'c2', 'c3']]
# Obtiene la segunda columna
# recorre la matriz m, cogiendo solo el indice 1 que es la columna 2
#  los corchetes [] exteriores indican que vamos a crear una lista
#  [       row[1] for row in m        ]
# se crea la variable row, de la que se recoge el segundo elemento, osease indice 1

# leerla
# dame row 1 para  cada row en m
#Esta expresión recorre la matriz m fila a fila, guardando cada fila en la variable
#row y, en cada iteración, obtiene el segundo elemento de la fila
col2 = [row[1] for row in m]
print(col2)#['a2', 'b2', 'c2']
# m no se ha modificado
print(m)#[['a1', 'a2', 'a3'], ['bl', 'b2', 'b3'], ['c1', 'c2', 'c3']]



nl = [['a1', 'a2', 'a3'], ['bl', 'b2', 'b3'], ['c1', 'c2', 'c3']]

# Extrae la diagonal de la matriz
#  crea una lista por los [] externos
# siendo m la matriz
"""
    nl = [['a1', 'a2', 'a3'], 
          ['bl', 'b2', 'b3'], 
          ['c1', 'c2', 'c3']]
"""
#m[0][0]    a1
#m[1][1]         b2
#m[2][2]                c3
print([m[i][i] for i in [0, 1, 2]])#  ['a1', 'b2', 'c3']

# Pueden haber expresiones dentro
# Extraemos las longitudes de los elementos de 'nl'
#  crea una lista por los [] externos
# recorre la matriz dando la
print([len(row) for row in nl]) #[3, 3, 3]
"""
Con tu nl:

row = ['a1', 'a2', 'a3'] -> len(row) es 3

row = ['b1', 'b2', 'b3'] -> len(row) es 3

row = ['c1', 'c2', 'c3'] -> len(row) es 3
"""


# Filtramos elementos
#  crea una lista por los [] externos
print([len(row) for row in nl if len(row) > 2]) #[3, 3, 3]




# Más expresiones dentro
#  crea una lista por los [] externos
# recorre un rango de 0 a 9
# y eleva al cuadrado
squares = [n ** 2 for n in range(10)]
print(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




la = [1, 2, 3]
# lista[:]
# cuando lo usamos con un string , nos devuelve una referencia a ese mismo objeto
# cuando usamos una listam nos devuelve una copia del objeto
lb = la[:]      # Copiamos la lista, copia del objeto

print(lb)#[1, 2, 3]

lc = list(la)  # otra manera de hacer una copia
print(lc)#[1, 2, 3]

la[2] = 'z'
print(la)#[1, 2, 'z']

print(la)#[1, 2,'z']   # hemos modificado ''la''
print(lb)#[1, 2, 3]    # pero no ''1b''
print(lc)#[1, 2, 3]    # ni ''1c''


"""
en objetos mutables
cuando un objeto es compartido  es modificado en el lugar
las demas referencias al objeto tambien observaran ese cambio

Para aislar una variable de cambios externos lo mejor es hacer una 
copia del objeto 

las copias pueden ser planas o profundas


"""
# Aislar una variable
import copy # importamos modulo copy
la = [1, 2, [31, 32, 33]] # Lista anidada

# Copia plana solo copia elementos de ler nivel
# Copia 'plana' (igual que 1b = la[:])
"""
Los elementos del primer nivel de la (que son 1, 2 y la referencia a la lista interna
 [31, 32, 33]) son copiados por referencia a lb.
lb[0] es 1 (una nueva referencia a un número inmutable).
lb[1] es 2 (una nueva referencia a un número inmutable).
lb[2] apunta a la MISMA LISTA INTERNA que la[2].
"""
lb = copy.copy(la)

# Copia profunda copia a todos los niveles
# Copia profunda. Por si hay elementos anidados
"""
Para cada elemento en la, deepcopy intenta crear una copia independiente
y nueva en todos los niveles de anidamiento.
lc[0] es 1 (una nueva referencia a un número inmutable).
lc[1] es 2 (una nueva referencia a un número inmutable).
lc[2] apunta a una NUEVA LISTA INTERNA [31, 32, 33], que es completamente 
independiente de la lista interna de la y lb.
"""
lc = copy.deepcopy(la)


la[1] = 'z'      # nivel 1
la[2][2] = 'zz'  # nivel 2

print(la)#[1,'z', [31, 32,'zz']]
print(lb)#[1, 2,  [31, 32,'zz']]   # Copia plana solo copia elementos de primer nivel
print(lc)#[1, 2,  [31, 32, 33]]    # Copia profunda copia a todos los niveles
                                   # copian varios niveles de anidamiento
#EXPLICACION

#osease , la copia plana, todo lo que haya dentro de la lista , si es otra lista,
# solo se copia la referencia
#pero si es una copia profunda , se hace una copia independiente de esa lista que
# esta dentro de la lista



"""
print(la) # [1, 'z', [31, 32, 'zz']]  <- Correcto. 'z' por la[1], 'zz' por la[2][2]
print(lb) # [1, 2,  [31, 32, 'zz']]   <- Correcto. '2' porque la[1] era inmutable, pero 'zz' porque la[2] apuntaba a la MISMA lista interna modificada.
print(lc) # [1, 2,  [31, 32, 33]]    <- Correcto. '2' porque la[1] era inmutable, y '33' porque lc tiene su PROPIA copia de la lista interna.
"""



"""  [1, 2, [31, 32, 33]]
Primer Nivel: 1, 2, [31, 32, 33]
Segundo Nivel:        31, 32, 33  es una lista de otra lista
Tercer Nivel: (Ninguno en este ejemplo)
"""




"""
¡Absolutamente, estoy seguro! Y la observación que haces de que "solo cambia el 33 y el 2" es precisamente el comportamiento que ilustra la diferencia clave entre una copia plana (copy.copy()) y una copia profunda (copy.deepcopy()) con objetos mutables anidados.

Vamos a desglosar el comportamiento de cada lista, paso a paso, con tus print y lo que ocurre internamente:

Contexto: Mutabilidad en Python
Objetos Mutables: Listas, diccionarios, conjuntos son mutables. Si modificas un objeto mutable, el cambio se ve por todas las referencias que apuntan a ese mismo objeto en memoria.

Objetos Inmutables: Números, cadenas de texto (strings), tuplas son inmutables. Si intentas "modificarlos", en realidad estás creando un nuevo objeto.

En tu ejemplo:
la = [1, 2, [31, 32, 33]]

1 y 2 son números (inmutables).

[31, 32, 33] es una lista (mutable). Esta lista interna es un elemento anidado.

Análisis Paso a Paso
Estado Inicial: 

la = [1, 2, [31, 32, 33]]
# En memoria:
# la apunta a la lista principal [1, 2, <dirección_lista_interna>]
# <dirección_lista_interna> apunta a [31, 32, 33]
lb = copy.copy(la) (Copia Plana)

copy.copy() crea una nueva lista principal lb.

Los elementos del primer nivel de la (que son 1, 2 y la referencia a la lista interna [31, 32, 33]) son copiados por referencia a lb.

Esto significa:

lb[0] es 1 (una nueva referencia a un número inmutable).

lb[1] es 2 (una nueva referencia a un número inmutable).

lb[2] apunta a la MISMA LISTA INTERNA que la[2].

Estado después de copy.copy():
la  ---> [1, 2, ----> [31, 32, 33]]
              |
lb  ---> [1, 2, -----^
lc = copy.deepcopy(la) (Copia Profunda)

copy.deepcopy() crea una nueva lista principal lc.

Para cada elemento en la, deepcopy intenta crear una copia independiente y nueva en todos los niveles de anidamiento.

Esto significa:

lc[0] es 1 (una nueva referencia a un número inmutable).

lc[1] es 2 (una nueva referencia a un número inmutable).

lc[2] apunta a una NUEVA LISTA INTERNA [31, 32, 33], que es completamente independiente de la lista interna de la y lb.

Estado después de copy.deepcopy():
la  ---> [1, 2, ----> [31, 32, 33]]

lb  ---> [1, 2, ----> ^ (misma lista interna que la)

lc  ---> [1, 2, ----> [31, 32, 33]] (NUEVA lista interna, diferente de la/lb)
la[1] = 'z' (Modificación en el primer nivel de la)

la[1] (el número 2) se cambia a la cadena 'z'. Como los números son inmutables, esto simplemente hace que la[1] apunte a un nuevo objeto 'z'.

lb[1] y lc[1] no se ven afectados, porque aunque originalmente apuntaban al mismo 2 que la[1], al cambiar la[1] se rompió esa conexión. Además, 2 es inmutable.

Estado después de la[1] = 'z':
la  ---> [1, 'z', ----> [31, 32, 33]]

lb  ---> [1, 2,  -----> ^

lc  ---> [1, 2,  -----> [31, 32, 33]]
la[2][2] = 'zz' (Modificación en el segundo nivel de la - la lista anidada)

Aquí es donde ocurre la diferencia crítica. Estás modificando la lista interna a la que la[2] apunta, cambiando su tercer elemento de 33 a 'zz'.

¿Qué pasa con lb? Como lb[2] apunta a la MISMA LISTA INTERNA que la[2], cualquier cambio en esa lista interna a través de la también será visible a través de lb. ¡Por eso lb[2][2] también se convierte en 'zz'!

¿Qué pasa con lc? Como lc[2] apunta a una COPIA INDEPENDIENTE de la lista interna, modificar la lista interna a la que apunta la[2] no afecta a la lista interna de lc. ¡Por eso lc[2][2] sigue siendo 33!

Estado FINAL:
la  ---> [1, 'z', ----> [31, 32, 'zz']]  <-- la lista interna ha cambiado

lb  ---> [1, 2,  -----> ^               <-- lb ve el cambio porque comparte la lista interna

lc  ---> [1, 2,  -----> [31, 32, 33]]   <-- lc no ve el cambio porque tiene su PROPIA copia de la lista interna

"""



"""
EXPLICACION


osease , la copia plana, todo lo que haya dentro de la lista , si es otra lista, solo se copia la referencia



pero si es una copia profunda , se hace una copia independiente de esa lista que esta dentro de la lista



¡Exactamente! Lo has captado a la perfección. Esa es la esencia de la diferencia entre copia plana y copia profunda en Python.

Para resumir tu entendimiento:

Copia Plana (copy.copy() o [:]):

Crea una nueva lista principal.

Para los elementos que están directamente en el primer nivel de la lista original:

Si el elemento es inmutable (ej. número, cadena, tupla), se copia el valor. Como son inmutables, cualquier cambio en el original para ese índice de primer nivel no afectará a la copia (y viceversa, porque se reemplazan los objetos inmutables, no se modifican).

Si el elemento es mutable (ej. otra lista, un diccionario, un conjunto), SOLO SE COPIA LA REFERENCIA (la dirección en memoria) a ese objeto. Esto significa que la lista original y la copia plana comparten el mismo objeto anidado. Si modificas ese objeto anidado a través de la lista original, el cambio se reflejará también en la copia plana, y viceversa.

Copia Profunda (copy.deepcopy()):

Crea una nueva lista principal.

Para todos los elementos, en todos los niveles de anidamiento:

Se crea una copia independiente (un nuevo objeto en memoria) de cada elemento, sea mutable o inmutable.

Esto garantiza que la lista original y la copia profunda sean completamente independientes. Modificar un elemento anidado en la lista original NO afectará a la copia profunda, y viceversa, porque cada una tiene su propia versión de todos los objetos.



"""