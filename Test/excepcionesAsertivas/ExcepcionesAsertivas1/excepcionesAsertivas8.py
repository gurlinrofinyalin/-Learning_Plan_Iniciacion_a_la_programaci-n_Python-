"""
Introducción
Las excepciones asertivas (assert) son constructos sintácticas de Python
que se configuran como booleanos puros, es decir, que sólo devuelven
True o False como resultado de la evaluación de una condición implícita.

Saber cómo escribir afirmaciones en Python le permite escribir fácilmente
minipruebas para su código.

Además, los marcos de prueba como PyTest pueden funcionar directamente
con afirmaciones para formar UnitTests en pleno funcionamiento.

En primer lugar, revisemos todos los diferentes tipos
de afirmaciones que podemos hacer para PyTest.
"""


#Lista de declaraciones de afirmación de PyTest Python



# Module Imports
import unittest
from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable

#Nota: Siempre que vea # Ejemplo de éxito, esto significa que la prueba
# de aserción tendrá éxito. Sin embargo, cuando vea # Ejemplo de falla,
# esto significa que la prueba de aserción fallará.


"""
============================= test session starts ==============================
collecting ... 
excepcionesAsertivas8.py:None (excepcionesAsertivas8.py)
excepcionesAsertivas8.py:38: in <module>
    assert any(booleans)== False
E   assert True == False
E    +  where True = any([False, False, True, False])
collected 0 items / 1 error

!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.70s ===============================

"""





"""
La función any() en Python es una función incorporada que se utiliza para determinar
 si cualquier elemento dentro de un iterable (como una lista, tupla o conjunto) es 
 verdadero (True). Devuelve True si al menos un elemento es "truthy" (es decir, 
 se evalúa como verdadero), y False si todos los elementos son "falsy" 
 (se evalúan como falsos).
"""
class TestAnyFunction(unittest.TestCase):
    def test_any_with_numbers(self):
        example = [5, 3, 1, 6, 6]
        # Esto es equivalente a "assert any(example) == True" en un test unitario
        self.assertEqual(any(example), True)
        print("Test 'any(example)' exitoso.") # Solo para ver en la consola, no esencial para el test

    def test_any_with_booleans(self):
        booleans = [False, False, True, False]
        self.assertEqual(any(booleans), True)
        print("Test 'any(booleans)' exitoso.")

# Para ejecutar los tests si ejecutas este archivo directamente
if __name__ == '__main__':

    # 8. declaracion de afirmación any()
    example = [5, 3, 1, 6, 6]
    booleans = [False, False, True, False]

    assert any(example) == True
    try:
        # cualquier de booleans es False , no salta excepcion
        # si que existen False en booleans
        assert any(booleans) == False
    except AssertionError:
        print("AssertionError 1")

    any(example)
    any(booleans)

    booleans2 = [False, False, False, False]
    any(booleans2)
    try:
        # cualquier de booleans2 es True , no salta excepcion
        # si que hay True en booleans2
        assert any(booleans2) == True
    except AssertionError:
        print("AssertionErro 2")








    unittest.main()


