"""
test_bubble_testify_simple.py - Pruebas para Bubble Sort con Testify (versión simplificada)
"""
from testify import TestCase, assert_equal, run
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
import sys
from io import StringIO


class BubbleSortTest(TestCase):
    """Suite de pruebas para Bubble Sort sin decoradores personalizados"""

    def setUp(self):
        """Redirige stdout antes de cada prueba"""
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restaura stdout después de cada prueba"""
        sys.stdout = self.original_stdout

    def test_sort_normal(self):
        """Prueba con lista desordenada"""
        arr = [5, 3, 8, 6, 2]
        expected = [2, 3, 5, 6, 8]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    def test_already_sorted(self):
        """Prueba con lista ya ordenada"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    def test_empty_list(self):
        """Prueba con lista vacía"""
        arr = []
        expected = []
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    def test_single_element(self):
        """Prueba con un solo elemento"""
        arr = [9]
        expected = [9]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    def test_duplicate_elements(self):
        """Prueba con elementos duplicados"""
        arr = [5, 3, 5, 2, 2]
        expected = [2, 2, 3, 5, 5]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)

    def test_negative_numbers(self):
        """Prueba con números negativos"""
        arr = [-3, -1, -4, -2]
        expected = [-4, -3, -2, -1]
        bubble_sort(arr, len(arr))
        assert_equal(arr, expected)


if __name__ == '__main__':
    run()