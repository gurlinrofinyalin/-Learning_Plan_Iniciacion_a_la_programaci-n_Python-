"""
test_bubble_testify_decorated.py - Versión con decoradores
"""
from testify import TestCase, assert_equal
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
import functools

def test(func):
    """Decorador personalizado para mantener estilo similar"""
    @functools.wraps(func)
    def wrapper(self):
        return func(self)
    return wrapper

class BubbleSortTest(TestCase):
    """Clase de pruebas para Bubble Sort"""

    @test
    def test_sort_normal(self):
        arr = [5, 3, 8, 6, 2]
        expected = [2, 3, 5, 6, 8]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    # ... otros tests ...

if __name__ == '__main__':
    from testify import run
    run()