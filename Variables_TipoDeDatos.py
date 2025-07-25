'''
Al asignar un valor a una variable, dicho valor pertenece
a un conjunto de valores conocido como tipo de dato.

Un tipo de dato define una serie de características sobre
esos datos y las variables que los contienen como,
por ejemplo, las operaciones que se pueden realizar
con ellos.


En Python, los tipos de datos básicos son
los numéricos (enteros, reales y complejos), los
boolenaos (True, False) y las cadenas de caracteres.'''

# conocer tipo de datos
lista = [1,2,3]
print(type(lista))# <class 'list'>

tupla = (1,2,3)
print(type(tupla))#<class 'tuple'>

diccionario = {
    "yo":'1',
    "tu":'2',
    "el":'3',
}
print(type(diccionario))#<class 'dict'>


otra_lista = [{"a","b","c"},{2,2,2}]
print(type(otra_lista))#<class 'list'>

otra_conjunto = {"a","b","c"}
print(type(otra_conjunto))#<class 'set'>



