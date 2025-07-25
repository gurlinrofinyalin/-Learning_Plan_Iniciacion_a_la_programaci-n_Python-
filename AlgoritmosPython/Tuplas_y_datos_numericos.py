#
#Python puede interpretar los paréntesis como parte de la expresión
#matemática y definir un tipo numérico, en lugar de una tupla
notuplas = (2)
print(type(notuplas))#<class 'int'>

# sintaxis num, poner la coma
tuplas = (2, )
print(type(tuplas))#<class 'tuple'>

tupla = (1,2,3,4)

# una tupla de varios elemetos puede asignarse a varias variables
num1,num2,num3,num4 = tupla
print(num1)#1
print(num2)#2
print(num3)#3
print(num4)#4

# el numero de variables debe de coincidir con el numero de elementos de la tupla


try:
    num1, num2, num3= tupla
except ValueError:
    print(" el numero de variables debe de coincidir con el numero de elementos de la tupla")


# el mecanismo de desempaquetado es el que se utiliza para devolver varias variables
# desde una funcion

def func():
    return 5,6 # aqui no se indican los parentesis despues return
               # porque no es necesario poner parentesis para definir una tupla

num1,num2 = func()
print(num1)#5
print(num2)#6


# definicion de tupla sin parentesis
tupla = 1,3,5
print(tupla)#(1, 3, 5)
print(type(tupla))# <class 'tuple'>



