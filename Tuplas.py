
# TUPLAS
"""Una tupla es una colección
ordenada
e
inmutable.

En Python, las tuplas se escriben entre paréntesis.  ()
"""

# Declaración de una tupla
miTupla = ("manzana", "banana", "cereza")
print(miTupla[1]) # banana
print("\n---------\n")

# Otra forma de declararla
miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)#('manzana', 'banana', 'cereza')
print("\n---------\n")


# Indexación Negativa
miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])# cereza
print("\n---------\n")

# Rango de índices
# Devuelve el tercer, cuarto y quinto elemento:
miTupla = ("manzana", "banana", "cereza","naranja", "kiwi", "melon", "mango")
# seria el  indice                  2         3         4
print(miTupla[2:5])# ('cereza', 'naranja', 'kiwi')
print("\n---------\n")

# Convierta la tupla en una lista para poder cambiarla:
miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla) # hacemos una lista
print(miLista," de tipo ",type(miLista))
#['manzana', 'banana', 'cereza']  de tipo  <class 'list'>
miLista[1] = "kiwi" # cambiamos el alemento NO LO AÑADIMOS
miTupla = tuple(miLista) # convertimos a tupla
print(miTupla," de tipo ",type(miTupla))
#('manzana', 'kiwi', 'cereza')  de tipo  <class 'tuple'>


print("\n---------\n")
# Recorrer una tupla
miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
    print(x)

"""
manzana
banana
cereza
"""


print("\n---------\n")
# Comprobar si existe un elemento
# Compruebe si "manzana" está presente en la tupla:
miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
    print("Sí, 'manzana' está en la tupla.")
# Sí, 'manzana' está en la tupla.


print("\n---------\n")
# Otra forma, simplemente con un boolean
print("manzana" in miTupla)# True

print("\n---------\n")
# Longitud de la tupla
miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))# 3  numero de elementos  con len

print("\n---------\n")
# Unir dos tuplas
tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)
tupla3 = tupla1 + tupla2
# unir dos tuplas con +
print(tupla3)# ('a', 'b', 'c', 1, 2, 3)

print("\n---------\n")
# Cuantas veces se encuentra el elemento 4 en miTupla?
# se hace con count
miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))# 2


print("\n---------\n")
# Desempaquetdo de tupla
# tantas variables a la izquierda como valores
# las puedes llamar como quieras
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3 = miTupla
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)