
#Capturando excepciones
#Para capturar excepciones utilizamos el bloque de sentencias try/except:
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')


print('Hemos salido del try-catch')
"""
En el bloque try se incluye el código propenso a causar la Excepción 
que queremos capturar en la sentencia except. 

La sentencia except está compuesta por la palabra clave que da nombre 
a la sentencia junto con la clase de la excepción que queremos capturar.

Por ejemplo, IndexError es una excepción que ocurre cuando intentamos 
acceder al índice de una secuencia y este índice está fuera de rango.


Dentro del bloque except incluimos el código necesario para manejar 
la situación cuando capturamos la excepción. 

En el ejemplo, simplemente estamos notificando en pantalla que el
usuario ha puesto un índice fuera de rango. 

Notad que sólo entramos en el except en caso que salte excepción IndexError:
"""
def indexador(objeto, indice):
    return objeto[indice]
try:
    print(indexador('Python', 3))
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')

print('Hemos salido del try-catch')

# en el segundo no  se produce la captura de la excepcion porque
# la excepcion no se produce