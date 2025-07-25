#Casting   # Forzado de tipo, CASTING:

# Forzado de tipo Enteros:
x = int(1) # x Valdrá 1
y = int(2.8) # y Valdrá 2   redondea  hacia abajo
z = int("3") # z Valdrá 3   de texto a entero

# Forzado de tipo Float:
x = float(1) # x Valdrá 1.0
y = float(2.8) # y Valdrá 2.8
z = float("3") # z Valdrá 3.0
w = float("4.2") # w Valdrá 4.2

# Forzado de tipo string:
x = str("s1") # x Valdrá 's1'
y = str(2) # y Valdrá '2'
z = str(3.0) # z Valdrá '3.0'


# CASTING. Reconversión de tipos:

# Casting de int a float:
n_numero = 13
n_numero_2 = float(n_numero)
print(n_numero_2)#13
print(type(n_numero_2))#<class 'float'>

# Casting de float a int:
n_numero_3 = 24.876
n_numero_4 = int(n_numero_3)
print(n_numero_4)#24
print(type(n_numero_4))#<class 'int'>

# Casting de string a int
s_texto = "13"
n_numero_5 = int(s_texto)
print(n_numero_5)#13
print(type(n_numero_5))#<class 'int'>


# Casting de int a string
n_numero_6 = 27
s_texto_2 = str(n_numero_6)
print(s_texto_2)
print(type(s_texto_2))



# COMENTARIOS
# Los comentarios son anotaciones que pondremos en nuestro código que el programa no va a tener en cuenta.
# Existen dos tipos de comentarios:
# Esto es un comentario de una línea
"""Esto es un comentario
que me va a ocupar
varias líneas"""

#Métodos de los strings
# TRABAJAR CON STRINGS
"""Los strings son secuencias de
caracteres de texto.
Todos los objetos en Python se engloban
en dos categorías: 
mutables 
o 
inmutables.

Los tipos básicos mutables son las
listas, los diccionarios y los sets.

Los tipos básicos inmutables son los
números, los strings y las tuplas.


Los objetos mutables pueden ser cambiados en el mismo objeto,
 mientras que los inmutables no.
"""

# Para concatenar textos se hace con “+” o simplemente
# con una coma.
print("Esta frase " + "termina aquí.")
#Esta frase termina aquí.

# Si ponemos coma nos pone entre los textos un espacio,
# con + no lo hace.
print("Esta frase" , "termina aquí.")
#Esta frase, termina aquí.

# Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b # c es "unodos"
# a es "uno"  asique multiplica "uno" por 3
c = a * 3 # c es "unounouno"
#----------------------------------------

