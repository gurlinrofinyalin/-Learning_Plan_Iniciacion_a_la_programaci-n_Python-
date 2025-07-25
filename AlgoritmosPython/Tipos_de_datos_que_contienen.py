#las tuplas listas diccionarios conjuntos pueden tener cualquier tipo de dato en python

#Una de las características más potentes y flexibles de Python es que sus colecciones (tuplas, listas, diccionarios y conjuntos) pueden contener elementos de cualquier tipo de dato diferente (son heterogéneas). No están limitadas a un solo tipo de dato, a diferencia de algunos otros lenguajes de programación.


#Listas:
mi_lista = [1, "Hola", 3.14, True, [4, 5], {"clave": "valor"}]
#Tuplas:
mi_tupla = (10, "Mundo", False, ("anidada",), None)
#Diccionarios:
mi_diccionario = {
    "nombre": "Ana",
    "edad": 30,
    "casado": False,
    1: "un número",
    "lista_hobbies": ["leer", "viajar"],
    (1, 2): "clave de tupla" # Las tuplas pueden ser claves si son inmutables
}
#Conjuntos:
# Los conjuntos solo pueden contener elementos inmutables
mi_conjunto = {1, "texto", 3.5, True, (1, 2, 3)}
# No se pueden añadir listas o diccionarios directamente a un conjunto
# porque son mutables y no hasheables.