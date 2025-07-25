
# -------------------------------------
# FUNCIONES
# -------------------------------------
# Definición de una función. Importante la identación:
def my_funcion():
    print("Estamos ejecutando la función.")
# Llamada a la función.
# En otra parte de mi código, llamamos a la función para que se ejecute:
my_funcion()
# Estamos ejecutando la función.

print("\n-----------\n")
def suma():
    num1 = 3
    num2 = 5
    print("suma =", num1+num2)
suma()# suma = 8      solo realiza la suma
print("\n-----------\n")
# Otra opción:
def suma():
    num1 = 3
    num2 = 5
    resultado = num1 + num2
    return resultado
print(suma())# 8    hay que imprimirla porque solo devuelve

print("\n-----------\n")
#El bloque de código que ejecutará la función incluye todas
# las declaraciones con indentación

# dentro de la función.
def miFunción():
    print('this will print')
    print('so will this')
x = 7
# la asignación de x no es parte de la función ya que no está indentada

print("\n-----------\n")
#Las variables definidas dentro de una función solo existen dentro
# del ámbito de esa función.
def duplica(num):
    z = num * 2
    return z
try:
    print(z) # error - x no está definida
except NameError:
    print("la variable z  esta dentro de la funcion ")
print(duplica(4)) # muestra 8

print("\n-----------\n")
#Si la definición de una función incluye parámetros,
# debe proporcionar el mismo número
# de parámetros cuando llame a la función.
def multiplica(arg1, arg2):
    return arg1 * arg2
try:
    print(multiplica(3))
except TypeError:
    print("TypeError: multiplica() missing 1 required positional argument: 'arg2'")
# TypeError: multiplica() utiliza exactamente 2 argumentos (1 proporcionados)


print(multiplica('a', 5)) # 'aaaaa' mostrado en la consola

try:
    print(multiplica('a', 'b')) # TypeError: Python no puede multiplicar dos strings
except TypeError:
    print("TypeError: Python no puede multiplicar dos strings")

print("\n-----------\n")
#Puedes pasar los parámetros en el orden que desees, utilizando el nombre del parámetro.
def suma(a, b):
    return a + b
result = suma(b=2, a=3)
print(result) # result = 5

print("\n-----------\n")
#También podríamos pasar varios valores que retornar a return.
def f(x, y):
    return x * 2, y * 2

a, b = f(1, 2)  # crea una tupla pero se pueden acceder
print(a)#2
print(b)#4

""" Sin embargo, esto no quiere decir que
las funciones Python puedan de-volver varios valores,
lo que ocurre en realidad es que Python 
crea una tupla al vuelo cuyos elementos
son los valores a retornar, y esta única
variable es la que se devuelve."""
print("\n-----------\n")
# función con un parámetro
# Declaración de una función
def miFuncion(num1, num2):
    return(num1+num2)
# Llamada a la función
print(miFuncion(2, 3))# 5


print("\n-----------\n")
def holaConNombre(name):
    print("Hola " + name + "!")
holaConNombre("Angel") # llamada a la función, 'Hola Angel!' se muestra en la consola
# Hola Angel!

print("\n-----------\n")
# Funcion con parametro por defecto   iva
def imprimir(precio, iva = 1.21):
    print(precio * iva)
imprimir(300, 1.08)# 324.0

print("\n-----------\n")

# Funciones con argumentos variables
# Me crea una tupla de nombre "otros"   , los variables se ponen al final
# osease *otros esta al final
def varios(param1, param2, *otros):
    # otros es una tupla con un asterisco
    for val in otros:
        print(val)
print("aqui")
varios(1, 2)#  NO HAY NADA EN OTROS ASIQUE NO IMPRIME NADA
varios(1, 2, 3)# 3  IMPRIME EN EL BUCLE
varios(1, 2, 3, 4) #3 y 4  las imprime en lineas separadas

#varios(1, 2): No imprime nada porque otros es una tupla vacía ().
#varios(1, 2, 3): Imprime 3. Esto es correcto.
#varios(1, 2, 3, 4): Imprime 3 y luego 4 (en líneas separadas). Esto es correcto.

"""
También se puede preceder el nombre del último parámetro con **,
en cuyo caso en lugar de una tupla se utilizaría un diccionario.

Las claves de este diccionario serían los nombres de los parámetros
indicados al llamar a la función y los valores del diccionario,
los valores asociados a estos parámetros.
"""

def varios2(param1, param2, **otros):
    # otros es un diccionario con 2 asteriscos , estamos accediendo a tercero=3 con items
    for i in otros.items():
        print(i)
varios2(1, 2, tercero=3)# ('tercero', 3)



print("\n-----------\n")
# ARGUMENTOS VARIABLES EN FUNCIONES.
# EL ARGUMENTO CON * SERÁ UNA TUPLA
# PYTHON NO TIENE SOBRECARGA DE FUNCIONES

####################################*args (Tupla) vs. **kwargs (Diccionario)
print("\n-----------\n")


def listarNombres(*nombres):
    # nombres es una tupla
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'María','Ernesto')
listarNombres('Laura', 'Carlos')

"""
Juan
Karla
María
Ernesto
"""
"""
Laura
Carlos
"""
print("\n-----------\n")

# HACER LO MISMO PERO PASANDO DICCIONARIOS COMO ARGUMENTOS.KWARGS

def listarTerminos(**KWARGS):
    # **KWARGS es un diccionario
    for clave, valor in KWARGS.items():  # items nos da clave y valor del dic
        print(f'{clave}: {valor}')

listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')

"""
IDE: Integrated Developement Environment
PK: Primary Key
"""
"""
DBMS: Database Management System
"""

print("\n-----------\n")

def mi_funcion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido} ')# con llaves un f delante
    # Sería como imprimir así:
    print('Nombre:', nombre, 'Apellido:', apellido) # con comas

mi_funcion('Juan', 'Perez')
mi_funcion('Karla', 'Lara')
"""
saludos desde mi función
Nombre: Juan, Apellido: Perez 
Nombre: Juan Apellido: Perez
"""
"""
saludos desde mi función
Nombre: Karla, Apellido: Lara 
Nombre: Karla Apellido: Lara
"""

print("\n-----------\n")
# RETURN
print("\n-----------\n")

# function definiciones de function no pueden estar vacías,
# pero si por alguna razón tiene
# una definición de function sin contenido,
# ingrese la instrucción pass para evitar un error.
def myfunction():
    pass

print("\n-----------\n")
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f'Resultado sumar: {resultado}')# Resultado sumar: 8

# También podíamos haber llamado a la función dentro de nuestro método print
print(f'Resultado sumar: {sumar(5, 3)}')
#Resultado sumar: 8


print("\n-----------\n")
# función con múltiples parámetros con una sentencia de retorno
def multiplica(val1, val2):
    return val1 * val2
print(multiplica(3, 5))  # muestra 15 en la consola



print("\n-----------\n")
# esta es una función básica de suma
def suma(a, b):
    return a + b
result = suma(1, 2)
print(result) # result = 3


print("\n-----------\n")
# VALORES POR DEFECTO
print("\n-----------\n")
# esta es una función básica de suma con balores predeterminados
def suma(a, b=3):
    return a + b # a sera 1
result = suma(1) # result = 4
print("\n-----------\n")
print("\n----TIPOS ->int  es una anotación de tipo, no una obligación estricta.----\n")
# Indico de qué tipo de dato vamos a manejar:
#Python aceptara si le mandas cadenas , a menos que la operacion que intentes no tenga sentido
def sumar(a: int = 0, b: int = 0) -> int: # def sumar(a = 0, b = 0):
    return a + b
resultado = sumar()
print(f'Resultado sumar: {resultado}')

print(f'Resultado sumar: {sumar(45,654)}')

# aunque le hemos dicho el tipo de los parámetros no estamos obligados a cumplirlo.
# porque usamos string en vez de int
print(f'Resultado sumar: {sumar("aNGEL","Garcia")}')
# ERRRROORORORORO
try:
    print(sumar("a", 3))  # DEBERI TENER UN  return a + str(b) PARA QUITAR ERROR
except TypeError:
    print("TypeError: can only concatenate str (not \"int\") to str")


print("\n-----------\n")
"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado , la suma de todos los valores pasados como argumentos.
"""
# Definimos nuestra funcion para sumar valores
def sumar_valores(*args):
    #  args es una tupla
    resultado = 0
    # Iteramos cada elemento de la tupla
    for valor in args:
    # resultado = resultado + valor
        resultado += valor
    return resultado

# Llamada a la funcion
print(sumar_valores(3, 5, 9, 4, 6, 45, 444))#516


print("\n-----------\n")
# Distintos tipos de datos como argumentos en Python
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres = ['Juan', 'Karla', 'Guillermo']
"""
Juan
Karla
Guillermo
"""
desplegarNombres(nombres)
desplegarNombres('Carlos')# carlos es un string por lo tanto un array
"""
C
a
r
l
o
s
"""
desplegarNombres((8, 9))
"""
8
9
"""

desplegarNombres([10, 11])
"""
10
11
"""
print("\n-----------\n")


# FUNCIONES RECURSIVAS
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

"""
factorial(6)
= 6 * factorial(5)
= 6 * 5 * factorial(4)
= 6 * 5 * 4 * factorial(3)
= 6 * 5 * 4 * 3 * factorial(2)
= 6 * 5 * 4 * 3 * 2 * factorial(1)

= 6 * 5 * 4 * 3 * 2 * 1
= 720
"""

"""  # 0! = 1   por definicion matematica
 ¿Por qué 0! = 1 y no 0?
Imagina esto:

 1. Factorial como número de formas de ordenar cosas
El factorial se usa para contar cuántas formas distintas se pueden ordenar n elementos.

Si tienes 3 objetos:
→ puedes ordenarlos de 3! = 6 formas.

Si tienes 1 objeto:
→ solo 1 forma: 1! = 1.

Si tienes 0 objetos, ¿cuántas formas hay de ordenarlos?
❗ Aunque no hay nada que ordenar, hay una única forma válida de "no hacer nada".
 Entonces: 0! = 1



. Por coherencia con fórmulas combinatorias
En combinatoria usamos fórmulas como: 
C(n, k) = n! / (k! * (n - k)!)
Si dijéramos que 0! = 0, entonces se romperían muchas fórmulas:
 
C(4, 4) = 4! / (4! * 0!) = 24 / (24 * 1) = 1 (correcto)

"""


def factorial(numero):
    if numero == 1:
        return 1
    else:
        # llama  a la funcion hasta que el numero sea 1
        # entonces sale, porque devuelve uno
        # mientras
        return numero * factorial(numero-1)
numero = 6
resultado = factorial(numero)# El factorial de 6 es 720
print(f'El factorial de {numero} es {resultado}')


print("\n-----------\n")
"""
Imprimir numeros de 5 a 1 de manera
descendente usando funciones recursivas.
Puede ser cualquier valor positivo,
ejemplo, si pasamos el valor de 5, debe
imprimir:
5
4
3
2
1


En caso de pasar el valor de 3, debe imprimir:
3
2
1


Si se pasan valores negativos no imprime
nada
"""
def imprimir_numero_recursivo(numero):
    if numero >= 1:
        print(numero)
        imprimir_numero_recursivo(numero- 1)# sale va al return porque numero es 0
    elif numero == 0:
        return # El return sin valor simplemente finaliza
               # la ejecución de una función y devuelve None
    elif numero < 0: # si es negativo
        print('Valor incorrecto...')
try:
    imprimir_numero_recursivo(5)
    imprimir_numero_recursivo(3)
    imprimir_numero_recursivo(5000000)
except RecursionError:
    print("""has superado el límite de veces que una 
          "función puede llamarse a sí misma antes de que Python 
          "detenga la ejecución para evitar que se agote la memoria.""")
"""
    5000000
    4999999
    4999998
4999006
4999005
4999004
excepcion   RecursionError:
"""
#RecursionError: maximum recursion depth exceeded while calling a Python object



print("\n-----------\n")
print("\n-----------\n")
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero) # el numero se imprime si es mayor que 0
        cuenta_regresiva(numero) # llama a la funcion para seguir
    else: # si no es mayor que 0, es que es 0, asique fuera
        print ("Boooooooom!")
        print ("Fin de la función")

cuenta_regresiva(5)
"""
4
3
2
1
Boooooooom!
"""

print("\n-----------\n")
"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total
de un pago incluyendo un impuesto
aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""


# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto:'))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')

"""
Proporcione el pago sin impuestos: 100.333
Proporcione el monto del impuesto:2222222
Pago con impuesto: 2229722.33226
"""

print("\n-----------\n")
"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de
grados celsius a fahrenheit y viceversa.
"""
# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
#* y / tienen la misma prioridad y se ejecutan de izquierda a derecha.
#Luego se ejecuta +.



# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
#Paréntesis primero: (fahrenheit - 32)
#Luego *
#Luego /
#(y recuerda: * y / también se hacen de izquierda a derecha)



# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)

# Imprimimos el resultado
print(f'{celsius} C a F:{resultado:.2f}')


# Realizamos la prueba de grados fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:0.2f}')