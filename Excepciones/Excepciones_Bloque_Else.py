#El bloque 'else' en las excepciones
"""
La última sentencia útil en el uso de excepciones es la sentencia else.

En el caso de excepciones, la sentencia else se comporta de manera
muy parecida a cómo lo hacía al ponerla tras un bucle:
ejecuta el código de su bloque sólo si NO salta la excepción en
el bloque try/except:
"""

# CON ELSE te cercioras de que no ha habido una excepcion
# porque si hay una no puede funciona el else

# EL ELSE SE USA SI LA OPERACION ES CORRECTA PARA  HACER ALGO
def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:  # atrapa si hay una excepcion de tipo
        print('No se puede dividir por cero')
    else: # se ejecuta si no salta la excepcion
        print('El resultado es: ', resultado)
    finally: # se ejecuta siempre
        print('Ejecutamos el finally')

print("\n"*1+"@"*30)
divide(4, 12) # no hay excepcion  salta el else
"""
El resultado es:  0.3333333333333333
Ejecutamos el finally
"""
print("\n"*1+"@"*30)
divide(4, 0)#  hay excepcion no salta el else
"""
No se puede dividir por cero         salta la excepcion  except
Ejecutamos el finally
"""
print("\n"*1+"@"*30)

"""
En este ejemplo intentamos hacer una división, y
controlamos dentro de un bloque try/except si
hemos intentado hacer una división por 0. Si el
usuario intenta dividir por 0, capturamos la
excepción en el except. 

Si la operación es correcta, entonces mostramos el 
resultado en el bloque else.
La ventaja del bloque else nos ahorra tener que
evaluar si tenemos resultado o no (podríamos no
haber obtenido un resultado en el caso de división
por cero).
"""