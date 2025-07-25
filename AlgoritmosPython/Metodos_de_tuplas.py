

#Métodos de las tuplas
"""
Python tiene dos métodos integrados que puede usar en tuplas.

count() Returns the number of times a specified value occurs in a tuple
index() Searches the tuple for a specified value and returns the position of where it was
found

count() Devuelve el número de veces que aparece un valor especificado en una tupla.
index() Busca en la tupla un valor especificado y devuelve la posición donde se encontró.
"""
miTupla=("Angel", 4, 5.345, True, 4)
tuplaUnitaria=("Sara",) #es una Tupla unitaria.
#Hay que poner al final ","

print(miTupla[2]) #Igual que en las listas
miLista=list(miTupla) #Con list convierto una tupla en una lista
miTupla2=tuple(miLista) #Con tuple convierto una lista en una tupla.

print("Angel" in miTupla) #Está "Angel" en miTupla?, devuelve True o False

print(miTupla.count(4))# 2, las veces  que encuentra el valor de 4 en
# ("Angel", 4, 5.345, True, 4)
#Cuantas veces se encuentra el elemento 4 en miTupla?

print(len(miTupla)) #5,  Longitud de miTupla

"""
Podemos definir la tupla sin poner los paréntesis, es lo que se conoce como 
“empaquetado de tupla”. 
En principio no se recomienda:
"""
miTupla="Angel", 4, 5.345, True, 4
# como  miTupla=("Angel", 4, 5.345, True, 4)


#Desempaquetado de tupla. Permite asignar todos los elementos de una tupla
# a diferentes variables:
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3 = miTupla
"""
Solo con esto ya nos ha asignado los valores de miTupla a las variables que hemos 
definido, podemos hacer la prueba imprimiéndolas:
"""
print(nombre)#Angeñ
print(num1)#4
print(num2)#5.345
print(valor1)# True
print(num3)# 4
