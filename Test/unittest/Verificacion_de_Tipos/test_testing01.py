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

 ----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
(.venv) python -m unittest test_testing01.py
-----Test de tipos no compatibles-----
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
(.venv) 


"""

"""
NO sale ningun error porque cuando los 
valores no son enteros o coma flotante decimales 
salta excepcion

Y cuando son negativos tambien
"""