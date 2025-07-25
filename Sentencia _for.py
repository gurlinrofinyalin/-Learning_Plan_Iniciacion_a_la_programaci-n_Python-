

"""El bucle for
La sintaxis del bucle for es muy sencilla y parecida a
la del bucle while, con la excepción que en la
cabecera del for, en lugar de evaluar una expresión
en cada iteración, vamos asignando elementos de un
iterador a una variable.

for elem in objeto: # Vamos asignado elementos de objeto en elem
    sentencias
    if test: # Podemos usar breaks
        break
    if test: # Podemos usar continues
        continue
else: # Si no hemos salido a través de break
    sentencias
"""


for s in ['Me', 'gusta', 'Python!']:
    print(s, end=' ')
#Me gusta Python!
"""
En este ejemplo vamos recorriendo elementos de
una lista de strings y vamos imprimiéndolos en
pantalla.   siendo end un espacio  al final  
"""


#esta vez sumando números
# suma todos los numeros de la lista
a = 0
for x in [1, 2, 3, 4]:
    a += x # a = a + x
print(a) # 10


#esta vez con strings:
# un string es como un array asique cada caracter
# lo recorre como  un  elemento, la c es el carcater
#  pone un espacio cada iteracion de c
for c in 'Me gusta Python!':
    print(c, end=' ')
#M e g u s t a P y t h o n !
print("\n")
"""
Este bucle recorre un string letra a letra y las va
mostrando por pantalla, añadiendo un espacio tras
cada impresión en pantalla.
"""

"""
recorriendo un diccionario, ya que uno de los usos más frecuentes
del bucle for es recorrer objetos iterables, diccionarios, tuplas…etc:
for k in d:
    print(k, end=' ')
Apellidos edad nombre

Por defecto, al pasarle un diccionario a un for, lo
recorremos por sus claves. 
Hay varias maneras de extraer los valores de un diccionario. 
Más adelante,
aprenderemos cómo recorrer simultáneamente las
claves y valores, pero de momento veamos una
manera muy sencilla de hacerlo:
"""
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario con zip
print(d)#{'nombre': 'Guido', 'apellidos': 'van Rossum', 'edad': '60'}

# siendo d el diccionario y k el elmento
# con k accedemos a la clave
# con d[k] accedemos al valor
for k in d:
    # cada {} es sustituida por parametros  k o d[k]
    info = '{}: {}'.format(k, d[k])
# Texto formateado con claves y valores
print(info)

'''
El método str.format sustituye las llaves
de la cadena de texto por los parámetros
que le pasamos al llamarlo. En cada
iteración del ejemplo le estamos pasando
la clave (k) del diccionario y el valor del
diccionario correspondiente a esa clave
(d[k]).
'''