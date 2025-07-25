'''
Desempaquetando una colección de
argumentos posicionales o por keyword
Cuando llamamos a una función se le pude utilizar la
sintaxis de * para desempaquetar una colección en
una serie de argumentos separados por posición.
'''

# POR POSICION args
def mi_funcion(a, b, c, d):
    print(a, b, c, d) # Aquí, a, b, c y d ya son los valores desempaquetados

# Creamos una lista (o tupla) con los argumentos en el orden correcto
argumentos_posicionales = [1, 20, 300, 4000]
print("\nTipo de 'argumentos_posicionales':", type(argumentos_posicionales))
# Desempaquetamos la lista 'argumentos_posicionales' con *
# Esto es equivalente a llamar mi_funcion(1, 20, 300, 4000)
mi_funcion(*argumentos_posicionales)


print('-----')
#POR CLAVE  kargs
def f(a, b, c, d):
    print(a, b, c, d)# aqui  estan desempaquetados

argumentos = {'b':20, 'a':1, 'c':300,'d':4000}
print("\nTipo de 'argumentos':", type(argumentos))#Tipo de 'argumentos': <class 'dict'>
f(**argumentos) # Desempaquetando diccionario argumentos con **
# 1 20 300 4000

argumentos = {'b':200, 'c':300, 'd':400}
print("\nTipo de 'argumentos':", type(argumentos))#Tipo de 'argumentos': <class 'dict'>
f(10, **argumentos) # Podemos combinar argumentos posicionales con dict
# 10 200 300 400