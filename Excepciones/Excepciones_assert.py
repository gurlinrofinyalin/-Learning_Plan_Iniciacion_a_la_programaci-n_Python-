#La sentencia ‘assert’
"""
Además de lanzar excepciones manualmente, es posible hacerlo
condicionalmente.

Para ello, Python proporciona la sentencia assert que nos permite
lanzar una excepción si se cumple una condición determinada.


Es muy común utilizar la sentencia assert durante el proceso de
depuración, para asegurarnos que se cumplen ciertas condiciones previas.


La sintaxis de assert es la siguiente:
assert(condición), ‘Mensaje de error’
Veamos un ejemplo:
"""
a = 10
b = 0

# Si se cumple no salta el error
# si a es mayor que b
assert(a > b), 'A tiene que ser mayor que B!'

print('Si se muestra esto es que no ha saltado el assert')

print("\n"*1+"@"*30)
"""
En este caso, como se cumple la condición, no salta el assert, 
y el programa sigue ejecutándose normalmente. 
"""

#Veamos un caso en el que sí salta la excepción producida por el assert:

a = 10
b = 0
c = 5
try:
    # como a no es igual a c, saltam el argumento vacio
    assert(a == c)
except AssertionError as e:
    print(f"Argumentos de la excepción: {e.args}")
    # vemos que el argumento  esta vacio asique no vemos nada
    if e.args:
        print(f"Mensaje específico (primer argumento): {e.args[0]}")

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepciones_assert.py", line 38, in <module>
    assert(a == c)
           ^^^^^^
AssertionError
"""
"""
Una nota importante sobre esta la sentencia assert:
su uso es muy útil para detectar errores en
depuración, 
pero no se recomienda el uso de assert en producción.
"""



