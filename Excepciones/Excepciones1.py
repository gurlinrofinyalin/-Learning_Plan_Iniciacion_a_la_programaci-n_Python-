#Los roles de las excepciones en Python

"""
• Manejo de errores: Se utilizan para informar de errores y/o de una situación
anómala así como de detener el flujo de programa.

• Notificación de eventos: P. ej. terminar una búsqueda sin resultados sin
tener que usar variables de control.

• Manejo de casos especiales: Podemos dejar el manejo de algunas situaciones
especiales que ocurren con poca frecuencia a excepciones.

• Acciones de limpieza/finalización: Operaciones de limpieza que se ejecutan
tanto como si ha habido errores como si no y que nos ayudan a asegurarnos que
este tipo de operaciones ocurren siempre, independientemente de que haya habido
un error o no. Esto es útil para asegurarnos que cerramos una conexión, un  fichero, etc.



En Python disponemos de 4 sentencias que podemos utilizar para manejar excepciones:
• try/except: Intercepta y recupera excepciones disparadas por Python o por nuestro código.
• try/finally: Realiza tareas de limpieza ocurran las excepciones o no.
• raise: Dispara una excepción manualmente en el código.
• assert: Dispara una excepción condicionalmente.


En esta unidad veremos cuándo utilizar cada una de estas sentencias, así como ejemplos
de las mismas. Nuestra primera excepción

A continuación, vamos a crear un código que generará una excepción si se le introduce
un parámetro adecuado.

Primero creamos una función, que devuelve el elemento que le pidamos de una secuencia
según el índice que le pidamos:
"""
def indexador(objeto, indice):
    return objeto[indice]
print(indexador('Python', 0))# P
"""
Como vemos, si le pedimos un índice que existe en la secuencia nos devuelve el elemento
 alojado en ese indice. 
"""


""" 
En cambio, si pedimos un índice demasiado rande, veremos que obtenemos un error de tipo
IndexError.
"""
def indexador(objeto, indice):
    return objeto[indice]
indexador('Python', 10) #Produce un error

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepciones1.py", line 51, in <module>
    indexador('Python', 10) #Produce un error
    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepciones1.py", line 50, in indexador
    return objeto[indice]
           ~~~~~~^^^^^^^^
IndexError: string index out of range


Notad que en otras unidades hemos simplificado las
salidas de las excepciones, en este no lo haremos
para que podáis ver toda la información relativa al
error que ha ocasionado la excepción.


Por ejemplo, en la llamada que acabamos de hacer, el intérprete ha
 lanzado la excepción, ha detenido el programa, 
 y además nos ha mostrado información a
la excepción:

1. Primero muestra el tipo de la excepción: IndexError
2. Luego nos muestra la traza de la misma, es decir la cadena de 
llamadas que la ha producido 
y la línea de código donde se ha producido

3. Finalmente, el intérprete nos muestra de nuevo el tipo de excepción 
y una cadena de información describiendo el error: 
‘IndexError: string index out of range’. 

En este caso nos explica que el índice de la cadena está fuera de rango.


Notad que diferentes intérpretes pueden daros la
información relativa a una excepción con un formato
ligeramente diferente, pero en esencia, casi siempre
muestran los tres campos que acabamos de
mencionar
"""



