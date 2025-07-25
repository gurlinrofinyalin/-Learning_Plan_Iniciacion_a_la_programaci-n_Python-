#Operadores lógicos
a = True
b = False
# si los dos son tal, entonces tal
resultado = a and b #False
print(resultado)

#o
resultado = a or b
print(resultado)# True

# lo contrario o negacion
resultado = not a
print(resultado)# False
#----------------------------------


# Sintaxis simplificada para varios operadores lógicos
edad = int(input('Introduce tu edad: '))
veintes = edad >= 20 and edad < 30
print(veintes)

edad = int(input('Introduce tu edad: '))
treintas = edad >= 30 and edad <40
print(treintas)

edad = int(input('Introduce tu edad: '))
if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
if veintes:
    print('Dentro de los 20\'s')
elif treintas:
    print('Dentro de los 30\'s')
else:
    print("No está dentro de los 20's ni 30's")


"""

Introduce tu edad: 33
False
Introduce tu edad: 23
False
Introduce tu edad: 22
Dentro de rango (20's) o (30's)
No está dentro de los 20's ni 30's
"""


