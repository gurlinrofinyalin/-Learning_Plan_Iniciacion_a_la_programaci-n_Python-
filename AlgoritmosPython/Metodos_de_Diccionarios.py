
# Métodos de los diccionarios

"""
Python tiene un conjunto de métodos integrados que podemos usar
en los diccionarios.

clear() Borra todos los elementos de un diccionario
copy() Devuelve una copia de un diccionario
fromkeys() Devuelve un diccionario con las claves y valores especificados
get() Devuelve el valor de una clave
items() Devuelve una lista que contiene una tupla por cada par clave-valor
keys() Devuelve una lista que contiene las claves del diccionario

pop() Borra el elemento con la clave especificada
popitem() Borra el último par clave-valor insertado
setdefault() Devuelve el valor de la clave especificada.
Si no existe, inserta la clave con el valor especificado.


update() Actualiza el diccionario con el par clave-valor que se especifique
values() Devuelve una lista con los valores del diccionario
"""



# Diccionario inicial para los ejemplos
mi_diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Nueva York",
    "profesion": "ingeniera"
}

print("--- Diccionario Inicial ---")
print(f"Original: {mi_diccionario}\n")
# {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York', 'profesion': 'ingeniera'}

# 1. clear() - Borra todos los elementos de un diccionario
print("--- 1. clear() ---")

# Hacemos una copia para no borrar el original
dic_para_clear = mi_diccionario.copy()

dic_para_clear.clear()
print(f"Después de clear(): {dic_para_clear}\n")#{}

# 2. copy() - Devuelve una copia de un diccionario
print("--- 2. copy() ---")
copia_diccionario = mi_diccionario.copy()
print(f"Copia del diccionario: {copia_diccionario}")
print(f"¿Es la misma ID que el original? {mi_diccionario is copia_diccionario}\n")
# Debería ser False porque  son objetos diferentes, no se hicieron con operador =

# 3. fromkeys() - Devuelve un diccionario con las claves y valores especificados
print("--- 3. fromkeys() ---")
claves = ['a', 'b', 'c']
valor_por_defecto = 0
nuevo_dic_fromkeys = dict.fromkeys(claves, valor_por_defecto)
print(f"Diccionario con fromkeys(): {nuevo_dic_fromkeys}\n")
# {'a': 0, 'b': 0, 'c': 0}
print("--- 3.1 fromkeys()  otro ---")
claves = ['a', 'b', 'c']
valor_por_defecto = [1,2,3]
nuevo_dic_fromkeys = dict.fromkeys(claves, valor_por_defecto)
print(f"Diccionario con fromkeys(): {nuevo_dic_fromkeys}\n")
#  Diccionario con fromkeys(): {'a': [1, 2, 3], 'b': [1, 2, 3], 'c': [1, 2, 3]}

# CON ZIP LO LOGRAMOS
#El método zip() es perfecto para combinar dos listas (o cualquier iterable) de
# manera que puedas emparejar elementos de una con elementos de la otra.
print("--- Usando zip() para asignar valores diferentes ---")
claves = ['a', 'b', 'c']
valores = [1, 2, 3] # Esta lista contiene los valores que quieres asignar secuencialmente
# 'zip(claves, valores)' creará pares así: ('a', 1), ('b', 2), ('c', 3)
# Luego, podemos construir el diccionario a partir de esos pares.
diccionario_con_zip = dict(zip(claves, valores))
print(f"Claves: {claves}")
print(f"Valores: {valores}")
print(f"Diccionario resultante con zip(): {diccionario_con_zip}")
# {'a': 1, 'b': 2, 'c': 3}




# 4. get() - Devuelve el valor de una clave
print("--- 4. get() ---")
print(f"Original: {mi_diccionario}\n")
# {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York', 'profesion': 'ingeniera'}
valor_edad = mi_diccionario.get("edad")#30
valor_pais = mi_diccionario.get("pais", "No encontrado")
# Con valor por defecto si no existe, devuelve  "No encontrado" si no existe
print(f"Valor de 'edad' con get(): {valor_edad}")
print(f"Valor de 'pais' con get() (no existe): {valor_pais}\n")

# 5. items() - Devuelve una lista que contiene una tupla por cada par clave-valor
print("--- 5. items() ---")
print(f"Original: {mi_diccionario}\n")
# {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York', 'profesion': 'ingeniera'}

pares_clave_valor = mi_diccionario.items()
print((pares_clave_valor))#
#dict_items([('nombre', 'Alice'), ('edad', 30), ('ciudad', 'Nueva York'), ('profesion', 'ingeniera')])

# Convertimos a lista para ver mejor
print(f"Pares clave-valor con items(): {list(pares_clave_valor)}\n")
#[('nombre', 'Alice'), ('edad', 30), ('ciudad', 'Nueva York'), ('profesion', 'ingeniera')]

# acceso a uno de los elementos
# Usar next() para obtener el primer elemento directamente del iterador
# 'iter()' se usa aquí para asegurarse de que estamos trabajando con un iterador explícito,
# aunque dict_items ya se comporta como uno.
primer_elemento = next(iter(pares_clave_valor))
print(f"Primer elemento sin convertir a lista: {primer_elemento}")
#Primer elemento sin convertir a lista: ('nombre', 'Alice')


# 6. keys() - Devuelve una lista que contiene las claves del diccionario
print("--- 6. keys() ---")
solo_claves = mi_diccionario.keys()
print(f"Claves con keys(): {list(solo_claves)}\n") # Convertimos a lista para ver mejor
#Claves con keys(): ['nombre', 'edad', 'ciudad', 'profesion']


# 7. pop() - Borra el elemento con la clave especificada
# podemos coger el elemento borrado
print("--- 7. pop() ---")
dic_para_pop = mi_diccionario.copy() # hacemos una copia
valor_eliminado = dic_para_pop.pop("profesion") # borramos en la copia
# AQUI SOLO OBTENEMOS EL VALOR NO LA CLAVE
print(f"Valor eliminado con pop('profesion'): {valor_eliminado}")# ingeniera
print(f"Diccionario después de pop(): {dic_para_pop}\n")
# Diccionario después de pop(): {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York'}



# 8. popitem() - Borra el último par clave-valor insertado (desde Python 3.7)
print("--- 8. popitem() ---")
dic_para_popitem = mi_diccionario.copy()# hacemos copia
par_eliminado = dic_para_popitem.popitem() # borramos el ultimo
# AQUI OBTENEMOS LA CLAVE Y EL VALOR
print(f"Par eliminado con popitem(): {par_eliminado}") #('profesion', 'ingeniera')
print(f"Diccionario después de popitem(): {dic_para_popitem}\n")
#Diccionario después de popitem(): {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York'}

# 9. setdefault() - Devuelve el valor de la clave especificada.
#    Si no existe, inserta la clave con el valor especificado.
print("--- 9. setdefault() ---")
dic_para_setdefault = mi_diccionario.copy()
valor_existente = dic_para_setdefault.setdefault("nombre", "Bob")
# devuelve Alice que es el valor de la clave nombre
# Clave existe, devuelve su valorm sino estuviera devolveria Bob

valor_nuevo = dic_para_setdefault.setdefault("pais", "España")
# Clave no existe, la inserta y devuelve el valor España que es el
# valor que hemos puesto por defecto
print(f"Valor de 'nombre' con setdefault(): {valor_existente}")
print(f"Valor de 'pais' con setdefault(): {valor_nuevo}")
# Al no existir hemos insertado España
print(f"Diccionario después de setdefault(): {dic_para_setdefault}\n")
#Diccionario después de setdefault(): {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Nueva York', 'profesion': 'ingeniera', 'pais': 'España'}


# 10. update() - Actualiza el diccionario con el par clave-valor que se especifique
print("--- 10. update() ---")
dic_para_update = mi_diccionario.copy()
dic_para_update.update({"edad": 31, "pais": "España"}) # 'edad' se actualiza, 'pais' se añade
#  si las claves existen , los valores se actualizan
# si las claves no existen se añaden clave y valor
print(f"Diccionario después de update(): {dic_para_update}\n")

# 11. values() - Devuelve una lista con los valores del diccionario
print("--- 11. values() ---")
solo_valores = mi_diccionario.values()
print(solo_valores)# dict_values(['Alice', 30, 'Nueva York', 'ingeniera'])
print(f"Valores con values(): {list(solo_valores)}\n")
# Convertimos a lista para ver mejor
# Valores con values(): ['Alice', 30, 'Nueva York', 'ingeniera']