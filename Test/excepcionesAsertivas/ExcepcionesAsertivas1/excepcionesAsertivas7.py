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

from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable

#Nota: Siempre que vea # Ejemplo de éxito, esto significa que la prueba
# de aserción tendrá éxito. Sin embargo, cuando vea # Ejemplo de falla,
# esto significa que la prueba de aserción fallará.

#7. El módulo % es igual a [valor]

print(30*"-")
assert 2 % 2 == 0 # Success Example

print(30*"-")
try:
    assert 2 % 2 == 1 # Fail Example
except AssertionError:
        print("AssertionError")

print(30*"-")
"""
 Traceback (most recent call last):
  File "/home/death/Documents/pythonIBM/proyectos/Test/excepcionesAsertivas/ExcepcionesAsertivas1/excepcionesAsertivas7.py", line 35, in <module>
    assert 2 % 2 == 1 # Fail Example
           ^^^^^^^^^^
AssertionError
"""