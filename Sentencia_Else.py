"""
Bloques else al finalizar bucles
Como hemos visto, tenemos dos maneras de finalizar
bucles.

La primera es una finalización limpia, sin interrupciones,
y la segunda es mediante el uso de la sentencia break.

Para saber si bucle ha finalizado de cierta manera,
en muchos lenguajes de programación se utilizan flags (banderas)
en el código que luego hay que evaluar.

En Python, esto no es necesario ya que podemos utilizar bloques
else al final de un bucle.

Por ejemplo, veamos un ejemplo donde hacemos
evaluamos si un número es primo o no dentro de un bucle while.
"""
a = 13
b = a // 2 # División entera. P. ej. 13 // 2 == 6
print("b es ", b)
# mientras la division del numero sea mayor que 1 calculamos el modulo
while b > 1:
    print('a es {}  y b es {} '.format(a ,b))
    # comprobacion de que la division de a / b  tiene como resto cero
    if a % b == 0: # % es el operador resto. P. ej. 10 % 5 == 0
        # si es divisible y da 0 el resto m entonces b es factor de a
        print('{b} es factor de {a}'.format(b,a))
        break # • break: Interrumpe el flujo y sale fuera de bucle.
    print("restamos a b , uno=  ", b)
    b -= 1 # b = b - 1
else:
    # si no se ejecuta el break el bucle acaba limpio y se ejcuta else
    print('{} es primo'.format(a)) # 13 es primo

print ('\nFuera del Bucle.')
'''
13 es primom divisible por 1 y por  el numero mismo 

b es  6
a es 13  y b es 6 
restamos a b , uno=   6
a es 13  y b es 5 
restamos a b , uno=   5
a es 13  y b es 4 
restamos a b , uno=   4
a es 13  y b es 3 
restamos a b , uno=   3
a es 13  y b es 2 
restamos a b , uno=   2
13 es primo




En este caso, hemos realizado la búsqueda de
factores del número 13 y, al no haber encontrado
ninguno, no hemos ejecutado break que teníamos
dentro del condicional. Por ello, el bucle ha finalizado
limpiamente por lo que se ha ejecutado el bloque else
al final del while.
'''