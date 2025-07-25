#El bucle for

# Ejecuta el print dos veces
for i in [1,10]:
    print("Hola")
"""  se ejecua el numero de veces que elementos en la lista
Hola
Hola
"""



print("-----------------\n---------------")
# Imprime el contenido del diccionario
for i in ["primavera", "verano", "otoño", "invierno"]:
    print(i)
"""
primavera
verano
otoño
invierno
"""

print("-----------------\n---------------")
# Repite el print tantas veces como caracteres hay en el string
# Evaluamos si un mail contiene el caracter @
for i in "frase":
    print("Hola", end=" ")

"""
Hola Hola Hola Hola Hola 
"""


print("\n-----------------\n---------------")
miEmail=input("Introduce email")
email=False
for i in miEmail:
    if i=="@":
        email=True
if email==True: #Se puede simplificar if email:
    print("El email es correcto")
else:
    print("EL mail no es correcto")

"""
Introduce email 
gurlinrofin@hotmail.com   mira si tiene una @
si la tiene  deja en True a email 
El email es correcto
"""

print("-----------------\n---------------")
# Podemos unir valores de texto con valores de variable a la hora de imprimir:
for i in range(5): # el 5 no cuenta , es 0 1 2 3 4
    print(f"Valor de la variable {i}")

    """
    Valor de la variable 0
    Valor de la variable 1
    Valor de la variable 2
    Valor de la variable 3
    Valor de la variable 4
    """
for i in range(5,10): # el 10 no cuenta es de 5 6 7 8 9
    print(f"Valor de la variable {i}")

"""
Valor de la variable 5
Valor de la variable 6
Valor de la variable 7
Valor de la variable 8
Valor de la variable 9
"""

print("-----------------\n---------------")
# Podemos poner un tercer argumento con el que especificamos de cuanto en cuanto va el conteo:
for i in range(5,10,2): # inicio 5  final 9  de dos en dosm 10 no cuenta
    print(f"Valor de la variable {i}")


"""  
Valor de la variable 5
Valor de la variable 7
Valor de la variable 9
"""

print("-----------------\n---------------")
# validar un mail en función de si tiene @ simplemente recorriendo la logitud del string:
valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):  # coge el numero de  caracteres del email  y busca una arroba
    if email[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")

""" 
Introduce tu email: gurlinrofin@hotmail.com
Email correcto
"""

print("-----------------\n---------------")
# Las cadenas son objetos iterables, contienen una secuencia de caracteres:
for x in "banana": # imprime el string cada caracter
    print(x)

"""
b
a
n
a
n
a
"""

print("-----------------\n---------------")

# Con la instrucción break podemos detener el ciclo antes de que haya pasado
# por todos los elementos:
# Salga del bucle cuando x es "banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)
    if x == "banana":
        break # cuando x = banana sale del bucle pero la imprime primero
"""
manzana
banana # cuando x = banana sale del bucle pero la imprime primero
"""

# Salga del bucle cuando x es "banana", pero esta vez el corte se produce antes de la impresión:
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana": # si x es banana sale del bucle y no imprime
        break
    print(x)

"""
manzana # si x es banana sale del bucle y no imprime
"""


# Con la instrucción continue podemos detener la iteración actual del ciclo y continuar con la siguiente:
# En este caso no me imprimiría
"banana"
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    if x == "banana":
        continue # cuando  x es banana , se salta la iteracion y  no imprime
    print(x)    # pero no sale del bucle solo se salta esa iteracion

"""
manzana
cereza
"""

print("-----------------\n---------------")
# Para recorrer un conjunto de código un número específico de veces, podemos usar la función range ()
for x in range(6):  # imprime 0 1 2 3 4 5 el 6 no
    print(x)
"""
0
1
2
3
4
5
"""
print("-----------------\n---------------")
# Función range con parámetro de inicio incrementado por defecto en 1.
for x in range(2, 6):  # imprime 2 3 4 5
    print(x)

"""
2
3
4
5
"""
# Función range con parámetro de inicio incrementado en 3.
for x in range(2, 30, 3):  # imprime del 2 al 29 de 3 en 3 , si contar el 30
    print(x)
"""
2
5
8
11
14
17
20
23
26
29
"""

print("-----------------\n---------------")
# Bucle for anidado
# Imprime cada color para cada fruta:
color = ["verde", "amarilla", "roja"]
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    for y in color:
        print(x, y)

"""   imprime x e y   
pero el primer elemento de frutas  lo recorre por todos los elementos de color 
el segundo igual
tercero igual recorriendo toda la matriz  
filas 3 columnas 3    
siendo frutas la fila, siendo color las columnas 
 
manzana verde
manzana amarilla
manzana roja
banana verde
banana amarilla
banana roja
cereza verde
cereza amarilla
cereza roja
"""

print("-----------------\n---------------")
# Los bucles for no pueden estar vacíos.

# Si por alguna razón tenemos un bucle for sin contenido,
# usaremos la instrucción pass para evitar un error.
for x in [0, 1, 2]:
    pass   # evitamos el error pero esta vacio

