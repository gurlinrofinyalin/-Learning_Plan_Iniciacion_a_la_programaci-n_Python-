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
  la función all() devuelve True si todos los elementos 
 en un iterable son verdaderos ("truthy"). Si encuentra un solo elemento que sea 
 falso ("falsy"), devuelve False inmediatamente.
"""
class TestAllFunction(unittest.TestCase):
    def test_all_with_numbers(self):
        example = [5, 3, 1, 6, 6]
        # assert all(example) # Success Example
        # Usamos self.assertTrue() porque esperamos que all(example) sea True
        self.assertTrue(all(example))
        print("Test 'all(example)' exitoso.")

    def test_all_with_booleans_fail_example(self):
        booleans = [False, False, True, False]
        # assert all(booleans) # Fail Example
        # Esperamos que all(booleans) sea False, por lo tanto, si usamos assertTrue, fallará.
        # Si quisieramos que pasara, haríamos self.assertFalse(all(booleans))
        self.assertFalse(all(booleans)) # Esto hará que el test PASE
        print("Test 'all(booleans)' exitoso (porque esperábamos que fuera False y lo fue).")


    # Si quieres ver el caso de fallo explícito, usa este test (deberá ser comentado o ignorado si quieres que todos pasen)
    def test_all_with_booleans_explicit_fail(self):
        booleans = [False, False, True, False]
        # Para que falle como "assert all(booleans)", haríamos:
        # self.assertTrue(all(booleans)) # Esto CAUSARÍA un fallo
        # En su lugar, vamos a mostrar un ejemplo de cómo se vería un test que falla intencionadamente
        with self.assertRaises(AssertionError): # Esperamos que esta aserción lance un AssertionError
             self.assertTrue(all(booleans))
        print("Test 'all(booleans)' que espera un fallo de aserción (y lo encontró) - éxito esperado.")



# Para ejecutar los tests si ejecutas este archivo directamente
if __name__ == '__main__':

    # 8. declaracion de afirmación any()
    example = [5, 3, 1, 6, 6]
    booleans = [False, False, True, False]

    assert all(example) == True
    try:
        # todos de booleans son  False no
        # como es falso no salta la excepcion
        assert all(booleans) == False
    except AssertionError:
        print("AssertionError 1")

    all(example)
    all(booleans)

    booleans2 = [False, False, True, False]
    all(booleans2)
    try:
        #todos  booleans2 es True , salta excepcion
        # son False todos con lo cual no son True
        assert all(booleans2) == True
    except AssertionError:
        print("AssertionErro 2")








    unittest.main()


