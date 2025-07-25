
#Sets, Conjuntos

"""
Los sets son un tipo de datos en Python que permite almacenar múltiples
elementos en una misma variable.

A diferencia de las listas, la colección de elementos que forman un set:
• No se puede indexar
• No respeta un orden
• No puede contener valores duplicados



Los sets se representan dentro de python con el tipo de dato set.

La sintaxis que se utiliza para definir un set en Python
es la siguiente:
{val1, val2, ..., valn}

También llamados sets.
 Los sets (conjuntos) son un tipo de datos básico de Python diferente
 a las secuencias y los diccionarios, pero aun así de gran utilidad.


 Los sets son conjuntos de objetos mutables no ordenados,
 (únicos y no ordenados), que se basan en la noción matemática de
 conjuntos.

De hecho, implementan una serie de métodos que permiten trabajar con
 conjuntos de objetos de la misma manera que lo hacemos en conjuntos
matemáticos.

Podemos hacer intersecciones, uniones, diferencias, etc.

No obstante, un conjunto no puede incluir objetos mutables como listas,
 diccionarios, e incluso otros conjuntos.


Son útiles cuando queremos trabajar con datos
masivos y queremos extraer información relevante
de ellos.

"""
# Sets iniciales para los ejemplos
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1, 2}
set_vacio = set()

mi_conjunto = {1, "texto", 3.5, True, (1, 2, 3)}

print(type(mi_conjunto))# set

"""
No obstante, un conjunto no puede incluir objetos mutables como listas,
 diccionarios, e incluso otros conjuntosm si puede tuplas.
"""