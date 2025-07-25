"""
test_bubble_nose2.py - Pruebas con generación de reportes
"""
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
import unittest
import time
import os

class TestBubbleSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start_time = time.time()
        cls.report_dir = "test-reports"
        if not os.path.exists(cls.report_dir):
            os.makedirs(cls.report_dir)

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

    @classmethod
    def tearDownClass(cls):
        print(f"\n⏱️  Tiempo total de pruebas: {time.time() - cls.start_time:.4f}s")
        print(f"📊 Reportes generados en: {os.path.abspath(cls.report_dir)}")

if __name__ == '__main__':
    import nose2
    nose2.main()


"""
 
FUNCIONA

# Ejecutar pruebas y generar todos los reportes
nose2 --config nose2.cfg -v

# Generar reporte de cobertura
coverage run -m nose2 --config nose2.cfg
coverage html

"""