# sentencia IF
a = 10
b = 3
if a > b:
    print ('SI se cumple la condición')
# Bloque identado 4 espacios
print ('Ya estamos fuera del if')

#SI se cumple la condición
#Ya estamos fuera del if


print('-----------if   else -------------')
"""
• Paréntesis en la evaluación. En Python son opcionales.
• Llaves que encierran el bloque. Python no utiliza llaves para 
separar bloques de código. En su lugar, la anidación se indica 
mediante el uso de bloques indentados, normalmente por cuatro (4) espacios.
• Punto y coma. En Python es opcional y se usa normalmente para delimitar 
varias sentencias en una misma línea (una práctica nada recomendada).

"""



a = 10
b = 3
if a > b:
    print ('Se ha cumplido la condición')
else:
    print ('No se ha cumplido la condición')
print ('Ya estamos fuera del if')

#No se ha cumplido la condición
#Ya estamos fuera del if


print('---------if   elif    else---------------')

a = 10
b = 10
if a > b:
    print ('A es menor que B')
elif a == b:
    print ('A es igual a B')
else:
    print ('A es mayor que B')

print ('Ya hemos salido del condicional')
#A es igual a B
#Ya hemos salido del condicional



print('---------- ternario ------------')
# es una expresión en sí misma y no una sentencia
a = 10
b = 3
# si la condicion a > b es verdad, resultado es 20 sino 30
print(20 if a > b else 30)
#20   es verdadera

"""
sintaxis

x = true_value if condición else
false_value

mejor entre parentesis
x = (true_value if condición else
false_value)


A pesar de que la expresión se lea de izquierda a
derecha, realmente se evalúa en el siguiente orden.
Primero se evalúa condición. Si ésta es verdadera,
entonces se devuelve true_value. Si no lo es, se
devuelve false_value.


es equivalente a

if condición:
... x = true_value
... else:
... x = false_value

"""

"""
las sentencias switch-case

Python no dispone de sentencias switch-case por lo
que este tipo de condicionales múltiples deberá
resolverse utilizando if-elif.
"""

############################# EJEMPLOS


l = list() #Creamos una lista vacia

texto = input("Introduce un número entero por teclado: ")
if texto.isnumeric():  # Comprobamos si son numeros
    #  pregunta si es un string , como si que es un numero hacemos casting
    num = int(texto)# casteamos a entero
    l.append(num) # agregamos a la lista
    print ("Número " + str(num) + " añadido a la lista")
else:
    print("No has introducido un número entero")
"""
Introduce un número entero por teclado: 50
Número 50 añadido a la lista
"""


print('------------------------------')
d = { "50862634": 37 , "43394932" : 32} #Creamos diccionario

texto = input("Introduce un documento de indentidad ")
if texto in d:  #Comprobamos si el texto ingresado esta en el diccionario
    print("La edad de " + texto + " es " + str(d[texto]))
    # muestra el numero y la edad
else: # si no lo esta le pedimos la edad
    edad = input ("Documento no existente. Introduce edad: ")
    if edad.isnumeric(): # si lo introducido es un numero casteamos
        num = int(edad) #   casteamos
        print(d)
        d[texto] = num # agregamos al diccionario siendo texto el dni
        # y num el valor de la edad m asique introduce un nuevo elemento
        # al diccionario
        print("Añadido al diccionario")
print(d)#Mostramos por pantalla el diccionario

"""
Tenemos un diccionario en el que asociamos los
números de los documentos de identidad de ciertas
personas con su edad.
Queremos realizar un programa en el que el usuario introduzca un el
número de un documento de identidad.
Si dicho número ya está en el diccionario debe mostrar la
edad, en caso contrario debe solicitarnos que
introduzcamos la edad, que posteriormente
añadiremos al diccionario.




si el numero esta muestra el numero y la edad
Introduce un número entero por teclado: 34232333
Número 34232333 añadido a la lista


si el numero no esta , pide la edad 
Introduce un documento de indentidad 23232323
Documento no existente. Introduce edad: 33
Añadido al diccionario
{'50862634': 37, '43394932': 32, '23232323': 33}
"""


print('------------------------------------')
