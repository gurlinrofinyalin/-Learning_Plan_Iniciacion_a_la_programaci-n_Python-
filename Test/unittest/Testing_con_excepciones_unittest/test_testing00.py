import unittest
from testing00 import area
from math import pi
class TestArea(unittest.TestCase):
    #Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos-----')
        #Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, -1)


        #Al ejecutar el código con python -m unittest test_testing01.py

"""
Hemos creado la misma función, pero le hemos
añadido una excepción que se disparará en el caso
de encontrar parámetros de entrada negativos. Para
el resto de valores la función se ejecuta como antes.
En nuestro archivo test_testing01.py creamos una
nueva función que compruebe la correcta ejecución
en caso de valores de entrada negativos


Para ello tendremos que usar el método assertRaises
al que hay que pasarle tres parámetros; el tipo de
excepción, la función a comprobar y el valor de salida
esperado:


Como vemos, no nos saca ningún mensaje de error,
lo que significa que la excepción se ha lanzado
correctamente.
Vamos a ver qué hubiese pasado si no tenemso
prevista la excepción en nuestro código.
Modificamos nuestra función, comentamos la línea
de la excepción y la sustituimos simplemente por un
print():
"""




"""  NO SE LANZA LA EXCEPCIKON ASIQUE FALLA
(.venv) python3 -m unittest test_testing00.py
-----Test de valores negativos-----
No se permiten valores negativos
F
======================================================================
FAIL: test_negativos (test_testing00.TestArea.test_negativos)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Test/unittest/Testing_con_excepciones_unittest/test_testing00.py", line 9, in test_negativos
    self.assertRaises(ValueError, area, -1)
AssertionError: ValueError not raised by area

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
(.venv) 



"""