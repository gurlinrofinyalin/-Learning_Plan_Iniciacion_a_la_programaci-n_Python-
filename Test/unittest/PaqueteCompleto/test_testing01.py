import unittest
from testing01 import area
# archivo que se importa para  ejecutar la funcion area
from math import pi

class TestArea(unittest.TestCase):
    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        # damos el valor que entra en la funcion area
        # ejemplo 1 , area(1)
        # y el valor que da cuando ya se ha ejecutado la funcion
        # osease lo que devuelve la funcion cuando la funcion
        # recibe 1 , luego 0  luego 3
        self.assertAlmostEqual(area(1),pi)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(3),pi*(3**2))

    # Test de valores negativos
    def test_negativos(self):
        print('-----Test de valores negativos-----')
        # Indicamos el tipo de excepción, la función y el valor esperado.
        self.assertRaises(ValueError, area, -1)

    # Test de tipos no compatibles. Verificamos si el tipo de los parámetros es el correcto.
    # El tipo de la excepción debe ser TypeError
    # Hacemos una pueba para que cada tipo conocido no válido
    def test_tipos(self):
        print('-----Test de tipos no compatibles-----')
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 'hola' )
        self.assertRaises(TypeError, area, 2 + 3j )



# python -m unittest test_testing01.py