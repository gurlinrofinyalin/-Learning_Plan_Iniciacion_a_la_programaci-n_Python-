"""
Verificación de tipos
Vamos a ver ahora cómo comprobar si el tipo de
datos que está recibiendo la función mediante
parámetro es correcto o no.
Para este tipo de test vamos a usar nuevamente el
método assertRaises() y el tipo de excepción que
estamos esperando que se lance es de tipo
TypeError.
Creamos una prueba para cada tipo de dato que
sabemos con certeza que no nos va a valer en
nuestra función:



"""


import unittest
from testing01 import area
from math import pi
class TestArea(unittest.TestCase):
    # Test de tipos no compatibles.
    # Verificamos si el tipo de los parámetros es el correcto.
    # El tipo de la excepción debe ser TypeError
    # Hacemos una prueba para que cada tipo conocido no válido
    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola')
        self.assertRaises(TypeError, area, 2+3j)


"""
Si nuestra función lanza una excepción al recibir este
tipo de datos, nuestro test no nos dará ningún error.
Si la función no lanza una excepción, entonces el test
sí nos dará errores.
"""

"""

(.venv) python -m unittest test_testing01.py
-----Test de tipos no compatibles-----
F
======================================================================
FAIL: test_tipos (test_testing01.TestArea.test_tipos)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Test/unittest/Verificacion_de_Tipos/test_testing01.py", line 11, in test_tipos
    self.assertRaises(TypeError, area, True)
AssertionError: TypeError not raised by area

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

"""

"""
Vemos que nuestro test ha lanzado errores. En
concreto se queja de que la ejecución
correspondiente a la línea 37 ha fallado. Es decir, que
nuestra función no lanza errores si el tipo de dato
recibido es un boolean.
Ya tenemos información de los cambios que
debemos hacer en nuestra función area.
"""

"""

Ahora sí tenemos el test sin fallos. Lo que significa
que ya tenemos tratados los casos en los que los
valores de entrada no sean números enteros
positivos o números de coma flotante positivos.
Como podemos ver los unittest son una herramienta
sencilla y poderosa con la que poder automatizar el
proceso de testing de nuestro código. Comprobando
los valores que conocemos con certeza que son
válidos, los que conocemos con certeza que no lo son
y las excepciones de nuestro código.
A continuación se expone un decálogo de buenas
prácticas a la hora de crear pruebas unitarias.
"""