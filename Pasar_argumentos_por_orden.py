# ORDEN PREDETERMINADO
# por defecto los argumentos se pasan por posicion
def f(a, b, c):
    print(a, b, c) # 1 2 3   en orden
f(1, 2, 3) # se pasan por defecto


'''
ORDEN ESTABLECIDO
En lugar de llamar a la función con sus argumentos
en orden, se le pasan especificando el nombre del
argumento seguido del valor que le queremos pasar.
la sintaxis nombre=valor. 
'''
def f(a, b, c):
    print(a, b, c)# 1 2 3   en orden
f(c=12, a=10, b=100)# se pasan con la sintaxis nombre=valor.
    
