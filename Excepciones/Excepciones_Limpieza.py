#Acciones de finalización y limpieza

"""
Cuando tenemos excepciones, hay situaciones en las
que queremos hacer operaciones de limpieza o
finalización sin importar si la excepción ha saltado o
no.

 Este tipo de operaciones suelen ser, por ejemplo,
asegurarnos que cerramos un fichero, una conexión, etc.
Para esto tenemos la sentencia finally:
"""
def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 10)
finally:
    # ejecutamos el codidigo que esta  aqui justo antes de detenerse
    # el programa
    print('Esto se ejecuta incluso cuando salta la excepción')

"""
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepciones_Limpieza.py", line 17, in <module>
    indexador('Python', 10)
  File "/home/death/Documents/pythonIBM/proyectos/Excepciones/Excepciones_Limpieza.py", line 14, in indexador
    return objeto[indice]
           ~~~~~~^^^^^^^^
IndexError: string index out of range
"""
"""
En este código hemos llamado a indexador de manera errónea 
y hemos producido una excepción. 
Normalmente, cuando esto ocurre, se detiene el flujo de programa. 
En este caso, al tener un bloque finally lo que ocurre es que, 
justo antes de detenerse el flujo de programa, ejecutamos el código 
que esté incluido en nuestro bloque finally.

Notad que el código siguiente, se le parece, pero NO se ejecutará:
"""

def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
    # ESTO DE ABAJO ES DESPUES DE LA EXCEPCION NO SE EJECUTA
    print('Este print no se ejecuta')
finally:
    print('Esto se ejecuta includo cuando salta la excepción')

"""
En este caso vemos que el print no se ha ejecutado
ya que antes ha saltado la excepción y, por lo tanto,
se ha detenido el flujo de ejecución del programa.
"""
"""
Notad también que el finally se ejecuta siempre, salte o no salte 
la excepción, pero si la excepción ha saltado, el flujo de programa 
se detiene justo después del finally.
"""
print("\n"*1+"-" * 30)

def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
finally:
    print('Esto se ejecuta includo cuando salta la excepción')
# ESTO NO SE EJECUTA
print('Este print tampoco se ejecuta')

print("\n"*1+"-" * 30)
"""
Es decir, que el finally sólo asegura que el código de su bloque se
 va a ejecutar, pero impide que el flujo de programa se detenga. 
Para eso, recordad que tenemos el bloque except:


"""
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10)
except IndexError:
    # SI NO TENEMOS UN EXCEPT correcto no capturamos la excepcion
    print('Capturamos la excepción')
finally:
    print('Esto se ejecuta incluso cuando salta la excepción')

print('Se ejecutará este print?')
"""
En este caso, indexador produce una excepción,
que capturamos en el bloque except, por lo que
ejecutamos el código dentro de ese bloque.
Luego, ejecutamos el código finally y, tras ello,
como ejecutamos el código fuera de nuestro
bloque try/except/finally.
"""