"""
Archivo: test_bubble_nose2.py
Pruebas para Bubble Sort usando nose2
"""
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
import unittest


class TestBubbleSort(unittest.TestCase):

    def test_sort_normal(self):
        """Prueba lista desordenada"""
        arr = [5, 3, 8, 6, 2]
        expected = [2, 3, 5, 6, 8]
        bubble_sort(arr, len(arr))
        self.assertEqual(arr, expected)

    def test_already_sorted(self):
        """Prueba lista ya ordenada"""
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        bubble_sort(arr, len(arr))
        self.assertEqual(arr, expected)

    def test_empty_list(self):
        """Prueba lista vacía"""
        arr = []
        expected = []
        bubble_sort(arr, len(arr))
        self.assertEqual(arr, expected)

    def test_single_element(self):
        """Prueba con un solo elemento"""
        arr = [9]
        expected = [9]
        bubble_sort(arr, len(arr))
        self.assertEqual(arr, expected)


if __name__ == '__main__':
    unittest.main()
"""
    Ejecutar
    Pruebas
bash
# Ejecutar todas las pruebas en el directorio
nose2

# O específicamente para este archivo
nose2 test_bubble_nose2.TestBubbleSort
"""