"""
Un aspecto que es importante es que el except sólo
captura las excepciones indicadas en la sentencia.

Es decir, si dentro del try se produce una excepción no
contemplada en el except, no seremos capaces de
capturarla.

Eso sí, es posible capturar varios tipos de excepciones a la vez:
"""

# en este caso capturamos las excepciones IndexError, TypeError
#Un IndexError ocurre cuando intentas acceder a un índice que está fuera
# del rango válido de una secuencia (como una lista, tupla o cadena).
#Un TypeError ocurre cuando intentas realizar una operación o función en
# un objeto de un tipo inadecuado. Es como intentar usar un martillo para
# atornillar un tornillo; el tipo de herramienta no es el adecuado para
# la operación


def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 'h')
# interceptar varias excepciones.
except (IndexError, TypeError): # Captura varios errores
    print('Error.')
    print('Hemos salido del try-catch')


# captura todos los errores sin poner NADA al lado de exceps
try:
    indexador('Python', 'h')
except: # Captura todos los errores. No recomendado.
    print('Error.')

print('Hemos salido del try-catch')

"""
En este código estamos mostrando dos maneras de interceptar varias excepciones.
La primera es la que nosotros recomendamos y consiste en un listado (una tupla) de
Excepciones que pueden saltar en nuestro bloque try. 

Cuando salte cualquiera de las Excepciones indicadas en nuestra tupla,
entraremos en el bloque except. 
"""

"""
La segunda opción, es válida sintácticamente en Python, pero está menos recomendada
 porque captura cualquier excepción.
 
 Esto es peligroso porque podríamos estar silenciando 
 excepciones no previstas por nosotros, por lo que estaríamos ocultando errores que luego 
 serán difíciles de encontrar. 
 
 Utilizad esta segunda opción con mucho cuidado y conociendo
  el riesgo al que os exponéis. 
  
  Una limitación de las dos aproximaciones anteriores es que,
   a pesar de que somos capaces de interceptar las excepciones indicadas, 
   las estamos tratando indistintamente. 
   
   Es decir, que vamos a tratar la excepción
    capturada de la misma manera independientemente que fuera una u otra. 
    
    Si queremos 
    hacer un tratamiento especial a un tipo de excepciones, lo podemos hacer encadenando
     bloques except uno detrás de otro, de manera similar a bloques elif en los 
     condicionales: def indexador(objeto, indice)
"""

# tratamos a cada excepcion de distinta manera
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 'h')
except IndexError: # Captura IndexError
    print('Error de índice.')
except TypeError: # Captura TypeError
    print('El índice tiene que ser un número.')

print('Hemos salido del try-catch')


"""
En este caso, hemos llamado a indexador
produciendo una excepción de tipo TypeError.
Estas excepciones saltan cuando intentamos hacer
una operación no admitida por el tipo que estamos
utilizando. En este caso hemos intentado acceder al
índice de una cadena de texto con otra cadena de
texto en lugar de un número, por lo que hemos
producido una excepción de tipo.
"""