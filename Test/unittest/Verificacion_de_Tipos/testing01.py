"""
Vamos a crear una nueva excepción que trate los
casos en los que el parámetro de entrada no sea un
número entero o de coma flotante:

"""

#Función con la excepción TypeError y verificación de negativos
from math import pi
def area(r):
    #Verificamos los tipos correctos
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    #Verificamos los valores negativos
    if r<0:
        raise ValueError("No se permiten valores negativos")
    areaC = pi*(r**2)
    return areaC


"""
Sabemos que a esta función no podemos darle
determinados valores, como por ejemplo valores
negativos, strings o booleans.
Vamos a hacer una prueba, de momento sin usar
unittest. Vamos a crear una lista con una serie de
valores que vamos a pasar como parámetro y vamos
a ver el comportamiento que tiene esa función con
esos valores.

"""

#valores = [1, 3, 0, -1, -3, 2+3j, True,'hola']
"""
Viendo el comportamiento de la función al pasarle los
parámetros sabremos si la función está trabajando
correctamente, aunque nosotros le estemos pasando
valores erróneos.
Es una forma de poder conocer con qué valores va a
funcionar correctamente mi función y con cuáles no.
Recorremos nuestra función pasándole los
parámetros de nuestra lista:
"""
# for v in valores:
#     areaCalculada = area(v)
#     print('Para el valor', v, 'el área es', areaCalculada)

"""

Para el valor 1 el área es 3.141592653589793
Para el valor 3 el área es 28.274333882308138
Para el valor 0 el área es 0.0
Para el valor -1 el área es 3.141592653589793
Para el valor -3 el área es 28.274333882308138
Para el valor (2+3j) el área es (-15.707963267948966+37.69911184307752j)
Para el valor True el área es 3.141592653589793
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Test/unittest/Proceso_automatizacion/inicio.py", line 31, in <module>
    areaCalculada = area(v)
                    ^^^^^^^
  File "/home/death/Documents/pythonIBM/proyectos/Test/unittest/Proceso_automatizacion/inicio.py", line 3, in area
    areaC = pi*(r**2)
                ~^^~
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

Process finished with exit code 1

"""

"""
Vemos que:
- Para los valores 1, 3 y 0 nos da resultados
correctos
- Para -1 y -3 nos da valores que no son lo que
debería dar, por lo que ya sabemos que,
cuando ingresemos radios negativos,
tendremos que hacer algo al respecto, como
por ejemplo lanzar una excepción.
- Para el número complejo (2+3j) el resultado
tampoco es lo esperado.
- Para el valor True el resultado tampoco es lo
esperado.
- Para el valor ‘hola’ directamente obtenemos
un error de tipo.
"""
