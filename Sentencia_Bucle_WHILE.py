

"""  el bucle while repite un trozo de
código iterativamente mientras se cumpla una
determinada condición.

Al comenzar cada iteración la expresión de inicio del
while es evaluada.

Si la expresión se cumple (devuelve True),
se vuelve a entrar en el while.
Si no se cumple (devuelve False),
el while deja de ejecutarse y pasamos a la
siguiente sentencia tras el while.


si a vale 3 ni siquiera entras en el while
"""
a = 0
# mientras a valga menor que 3
while a<3:
    # Acabamos con espacios en lugar de salto de línea
    print (a, end=' ')
    # esta es la condicion que hace que no sea infinito
    # debido a que empieza de a=0 y va sumando 1
    a += 1 # Equivalente    a = a + 1

print (a) # Estamos fuera del bucle while


print('Hemos salido fuera del while')
'''
0 1 2 3
Hemos salido fuera del while
'''



