"""
Se puede especificar un rango de índices si le especificamos dónde
comenzar y dónde terminar el rango.

Al especificar un rango, el valor de retorno será una nueva lista con los
elementos especificados.

"""
#Crear una lista de elementos y devolver el segundo, tercer y cuarto elemento
# (indices 2 3 4).
# Nota: La búsqueda comenzará en el índice 2 (incluido) y finalizará en el
# índice 5 (no incluido). Recordemos que el primer elemento tiene el índice O.
thislist = ["Manzana", "plátano", "cereza", "naranja", "kiwi", "melon", "mango"]
print(thislist[2:5])
#['cereza', 'naranja', 'kiwi']


#Rango de índices negativos
#Podemos especificar índices negativos si desea comenzar la búsqueda desde el final de la lista:
thislist = ["Manzana", "plátano", "cereza", "naranja", "kiwi", "melon", "mango"]
#                                               -4       -3       -2      -1
print(thislist[-4:-1])#  de derecha a izquierda, siendo -4 naranja y -1 que no cuenta mango
#Este ejemplo devuelve los elementos del índice -4 (incluido) al índice -1 (excluido)
# (indices siendo 0 el mango, melon -1 , kiwi -2 , naranja -3 )
#
#['naranja', 'kiwi', 'melon']
print(thislist[-4])# naranja
print(thislist[-2])# melon
print(thislist[-1])# mango
# cuenta pero de derecha a izquierda, siendo el ultimo el -1
print(thislist[-3:])# ['kiwi', 'melon', 'mango']



#Cambiar valor del elemento
#Para cambiar el valor de un elemento específico, consulte el número de índice:
thislist = ["Manzana", "plátano", "cereza"]
print(thislist)#['Manzana', 'plátano', 'cereza']
#Cambiar el segundo elemento:
thislist [1] = "Pera"
print(thislist)#['Manzana', 'Pera', 'cereza']



#Recorrer una lista
#Puede recorrer los elementos de la lista utilizando un bucle for :
#Imprima todos los elementos de la lista, uno por uno:
thislist = ["Manzana", "plátano", "cereza"]
for x in thislist:
    print (x)
#Manzana
#plátano
#cereza


#Comprobar si el elemento existe
#Para determinar si un elemento específico está presente en una lista, use la palabra clave in :
thislist = ["Manzana", "plátano", "cereza"]
#Compruebe si "manzana" está presente en la lista con in
if "Manzana" in thislist:
    print("Sí, 'Manzana' se encuentra en la lista.")
# Sí, 'Manzana' se encuentra en la lista.



#Longitud de la lista
#Para determinar cuántos elementos tiene una lista, use el método len() :
#Imprima el número de elementos en la lista:
thislist = ["Manzana", "plátano", "cereza"]
print(len(thislist))#3

"""
####Copiar una lista
No puede copiar una lista simplemente escribiendo list2 = listi, porque:
list2 solo será una referencia a list1, 
y los cambios realizados en list1 también se realizarán automáticamente en list2 
NO  ES UNA COPIA ES UNA REFERENCIA A
"""
thislist = ["Manzana", "plátano", "cereza"]
#Hay formas de hacer una copia, una es usar el método de lista incorporado copy() .
mylist = thislist.copy()
print(thislist)# ['Manzana', 'plátano', 'cereza']
print(mylist)# ['Manzana', 'plátano', 'cereza']

# CAMBIAMOS la lista en thislist metemos fresa y en mylist metemos Piña quitando plàtano
thislist[1] = "Fresa"
mylist[1] = "Piña"
# son copias diferentes
print(thislist)# ['Manzana', 'Fresa', 'cerez# a']
print(mylist)# ['Manzana', 'Piña', 'cereza']



#Otra forma de hacer una copia es usar la listO métodos incorporada listo .
thislist = ["Manzana","plátano","cereza"]
#Haga una copia de una lista con el método list() :
mylist = list(thislist)  # lista_nueva = list(lista)
print(mylist) #['Manzana', 'plátano', 'cereza']
print(thislist)#['Manzana', 'plátano', 'cereza']


# Obtener el ID de ese objeto
identificador_objeto_thislist  = id(thislist)

print(f"El objeto {thislist } tiene el ID: {identificador_objeto_thislist }")
# El objeto ['Manzana', 'plátano', 'cereza'] tiene el ID: 139690626357760

# Si creas otro objeto con el mismo contenido, tendrá un ID diferente
# hemos copiado con  list(thislist)
identificador_objeto_mylist = id(mylist)

print(f"El objeto {mylist} tiene el ID: {identificador_objeto_mylist}")
# El objeto ['Manzana', 'plátano', 'cereza'] tiene el ID: 139690626497984



# Puedes usar 'is' para comprobar si dos variables apuntan al mismo objeto (mismo ID)
print(f"¿'mi_objeto_lista' y 'misma_lista' son el mismo objeto? {thislist is mylist}") # False



# COMPARACION DE OBJETOS
#Para comparar el contenido (los elementos) de estos dos objetos tipo lista (thislist y mylist),
# que como bien has demostrado son objetos diferentes en memoria (thislist is mylist es False),
# usarías el operador de igualdad ==.

#El operador == en Python compara si los elementos de las listas son los mismos y están en el mismo orden.

print(f"ID de thislist: {id(thislist)}")
print(f"ID de mylist: {id(mylist)}")

# Comparamos si son el mismo objeto (identidad)
print(f"¿'thislist' es 'mylist'? (Identidad) {thislist is mylist}")

# Comparamos si tienen el mismo contenido (valor)
print(f"¿'thislist' == 'mylist'? (Contenido) {thislist == mylist}")





### JAVA y PYTHON

"""
En Java, un método equals() bien implementado (que sobrescribe el de Object) a menudo comienza 
1-verificando si el objeto que se compara es null,
2-luego si es el mismo objeto (this == obj), 
3- y finalmente si es de la misma clase o una subclase compatible (usando instanceof o getClass() == obj.getClass()) 
4-antes de comparar los valores de los atributos.

El operador == en Java, para objetos, solo compara si son la misma referencia en memoria.
"""
"""
En Python, la situación es un poco más flexible:
El operador == (que llama al método __eq__):
Por defecto, para muchos tipos integrados (como números, cadenas, tuplas), == se enfoca en la igualdad de valor, 
y a menudo puede comparar valores incluso entre tipos diferentes si son conceptualmente "iguales" o coercibles. 

Por ejemplo:
"""
print(1 == 1.0)  # True (compara valor, no tipo estricto)
print("1" == 1)  # False (no coercible automáticamente en esta comparación de valor)
"""
Cuando se compara objetos de clases personalizadas (las que tú defines), 
si no sobrescribes el método __eq__, el == por defecto heredado de object se comporta como is, 
es decir, verifica la identidad (si es el mismo objeto en memoria).

Si sobrescribes el método __eq__ en tu propia clase, 
tú decides completamente cómo se maneja la comparación. 
Puedes optar por verificar el tipo (usando isinstance() o type(self) is type(other)) 
antes de comparar atributos, o puedes no hacerlo, dependiendo de la lógica que necesites.
"""
"""
¿Hay algo parecido a la verificación de tipo de equals() de Java en Python?
No hay una verificación de tipo obligatoria implícita al usar == como la que a menudo se implementa por convención 
en Java con equals().
Si deseas una verificación de tipo estricta para la igualdad en tus clases personalizadas, 
debes implementarla explícitamente dentro de tu método __eq__.
"""
#Ejemplo de __eq__ en Python con verificación de tipo:

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # COMPARAR LA IDENTIDAD,
        # 1. Comprobar si son el mismo objeto (identidad)
        if self is other:
            return True

        # COMPARAR EL TIPO
        # 2. Comprobar si 'other' es del mismo tipo (equivalente a getClass() == other.getClass() en Java)
        #    O: isinstance(other, Punto) para permitir subclases
        if not isinstance(other, Punto):
            return NotImplemented # Indica que la comparación no está definida entre estos tipos
        """
        NotImplemented es una constante especial en Python. No es ni True, ni False, ni None. 
        Es un valor que le dice al intérprete de Python: 
        "Mira, no sé cómo comparar estos dos objetos (o realizar esta operación) con la implementación actual de este método."
        Indica que la comparación (o la operación) no está definida entre esos tipos. 
        En el ejemplo que diste:
        Si other no es un objeto de tipo Punto (ni una subclase de Punto), tu Punto.__eq__ no sabe cómo compararlo. 
        En lugar de lanzar un error inmediatamente o devolver un False incorrecto, devuelve NotImplemented.
        
        Le da una segunda oportunidad a Python. Cuando __eq__ devuelve NotImplemented:
        Python no considera la comparación como True o False todavía.
        En su lugar, intenta intercambiar los operandos y llamar al método correspondiente del otro objeto.
        Si estabas haciendo p1 == otra_cosa, y p1.__eq__(otra_cosa) devuelve NotImplemented, 
        Python intentará llamar a otra_cosa.__eq__(p1).

        Si la comparación "invertida" también devuelve NotImplemented, o si no hay un método compatible, 
        o si al final ninguna de las partes puede decidir el resultado, entonces Python recurre a la comparación por 
        defecto (normalmente por identidad, es decir, si son el mismo objeto en memoria), 
        o en algunos casos puede lanzar un TypeError si la operación es completamente incompatible.
        """


        # COMPARAR EL CONTENIDO
        # 3. Si son del mismo tipo, comparar los valores de los atributos
        return self.x == other.x and self.y == other.y

# --- Pruebas ---
p1 = Punto(1, 2)
p2 = Punto(1, 2)
p3 = Punto(3, 4)
otra_cosa = (1, 2) # Una tupla

print(f"p1 == p2: {p1 == p2}")     # True (mismo valor, mismo tipo)
print(f"p1 == p3: {p1 == p3}")     # False (diferente valor)
print(f"p1 == otra_cosa: {p1 == otra_cosa}") # False (diferente tipo, gestionado por __eq__)

# Comprobación de identidad (como Java == para objetos)
print(f"p1 is p2: {p1 is p2}")     # False (objetos diferentes)
print(f"p1 is p1: {p1 is p1}")     # True (mismo objeto)

"""
En este ejemplo de Python, el __eq__ que implementamos se parece mucho a un equals() bien implementado en Java, 
porque primero verifica la identidad, luego el tipo, y finalmente el contenido. 
Pero esta verificación de tipo la has puesto tú explícitamente al definir __eq__. Python no la impone automáticamente para todas las comparaciones ==.
"""








### HASH  
try:
    print(f"Hash de {mylist}: {hash(mylist)}")
except TypeError as e:
    print(f"Error al hashear una lista mylist: {e}")

try:
    print(f"Hash de {thislist}: {hash(thislist)}")
except TypeError as e:
    print(f"Error al hashear una lista thislist: {e}")


"""
El "hashcode" en Python es el valor entero que devuelve la función incorporada hash() para un objeto. 
Este valor se utiliza para la eficiencia en estructuras de datos como diccionarios (dict) y conjuntos (set).
Solo los objetos inmutables pueden ser hasheables 
y, por lo tanto, tener un "hashcode" numérico útil. 

Ejemplos de tipos hasheables (inmutables) son:
Números (enteros, flotantes)
Cadenas de texto (str)
Tuplas (tuple) (si todos sus elementos también son hasheables)
Objetos frozenset
Ejemplo de cómo obtener un hashcode numérico real:
"""
my_string = "hola"
my_tuple = (1, 2, "a")
my_number = 123

print(f"Hash de '{my_string}': {hash(my_string)}")
print(f"Hash de {my_tuple}: {hash(my_tuple)}")
print(f"Hash de {my_number}: {hash(my_number)}")

# Intentar con una lista causará un error:
try:
    my_list = [1, 2, 3]
    print(f"Hash de {my_list}: {hash(my_list)}")
except TypeError as e:
    print(f"Error al hashear una lista: {e}")
"""
__hash__ es el método especial que, si está definido y no es None, devuelve el hashcode de un objeto.
La función incorporada hash() llama a este método __hash__ internamente.
Las listas (list) son mutables y, por diseño de Python, no son hasheables, 
por lo que no tienen un "hashcode" numérico utilizable en el sentido de una clave de diccionario o elemento de conjunto.
"""


"""
 el comportamiento son ligeramente diferentes entre Java y Python en este punto.

En Java:

El método hashCode() está diseñado principalmente para devolver un valor entero que se usa en colecciones basadas 
en hashes (como HashMap o HashSet). 
La regla es que si dos objetos son "iguales" (.equals()), deben tener el mismo hashCode().
Por defecto, la implementación de hashCode() en Object (la clase base en Java) a menudo deriva de la dirección 
de memoria del objeto, lo que puede dar la impresión de que estás viendo la "referencia" o "ID". 
Pero no es su propósito principal ni su contrato. 
Para obtener el "hash de identidad" (que es más parecido al id() de Python), 
Java tiene System.identityHashCode().

Para comparar si dos variables apuntan al mismo objeto en Java, se usa el operador ==.

En Python:
Para obtener la referencia única del objeto (su identidad en memoria, su "ID"), 
la función que debes usar es id(). 
Esta es la forma directa y garantizada de saber si dos variables apuntan al mismo objeto en memoria.
El método __hash__ (o la función hash()) en Python tiene exactamente el mismo propósito que hashCode() en Java: 
devolver un valor entero para usar en colecciones basadas en hashes (diccionarios, conjuntos).

La diferencia clave es que, en Python, los objetos mutables (como las listas) no tienen un __hash__ que devuelva 
un valor útil, sino que lanzan un error si intentas hashearlos, precisamente para evitar problemas en diccionarios 
y conjuntos si el objeto cambia.
En resumen:

Si en Java pensabas que hashCode() te daba la "referencia/ID" del objeto, en Python, el equivalente directo 
para obtener esa identidad única y constante del objeto es id(). 
El __hash__ en Python es para la "hashabilidad" del objeto en colecciones, no para su identidad única.
"""


# Crear un objeto
mi_objeto_lista = [10, 20, 30]

# Obtener el ID de ese objeto
identificador_objeto = id(mi_objeto_lista)

print(f"El objeto {mi_objeto_lista} tiene el ID: {identificador_objeto}")

# Si creas otro objeto con el mismo contenido, tendrá un ID diferente
otra_lista_igual = [10, 20, 30]
print(f"El objeto {otra_lista_igual} tiene el ID: {id(otra_lista_igual)}")

# Si una variable apunta al mismo objeto, tendrá el mismo ID
misma_lista = mi_objeto_lista
print(f"El objeto {misma_lista} tiene el ID: {id(misma_lista)}")

# Puedes usar 'is' para comprobar si dos variables apuntan al mismo objeto (mismo ID)
print(f"\n¿'mi_objeto_lista' y 'otra_lista_igual' son el mismo objeto? {mi_objeto_lista is otra_lista_igual}")
print(f"¿'mi_objeto_lista' y 'misma_lista' son el mismo objeto? {mi_objeto_lista is misma_lista}")
