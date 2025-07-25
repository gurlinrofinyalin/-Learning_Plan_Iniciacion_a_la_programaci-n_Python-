import unittest
import sys
import os

# Añadir la ruta del directorio que contiene tu script bubble_sort al PYTHONPATH
# Esto es crucial para que Python pueda encontrar tu módulo
script_dir = os.path.dirname('/home/death/Documents/pythonIBM/proyectos/Test/unittest/prueba_unittest/test_bubble_sort_unittest.py') # Directorio donde está este script de prueba
# Ruta a la carpeta "Algoritmos_de_clasificacion" que contiene tu archivo bubble_sort
# Ajusta esta ruta si tu test_bubble_sort_unittest.py no está en el mismo nivel
# que 'proyectos/Test/'
bubble_sort_path = os.path.join(
    os.path.expanduser("~"), # Equivalente a /home/death
    "Documents",
    "pythonIBM",
    "proyectos",
    "AlgoritmosPython",
    "Algoritmos_de_clasificacion"
)
sys.path.insert(0, bubble_sort_path)

# Ahora puedes importar tu función bubble_sort
try:
    from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
except ImportError as e:
    print(f"Error al importar bubble_sort: {e}")
    print(f"Asegúrate de que el archivo 'Algoritmos_de_clasificacion_Bubble_sort_burbujas.py' está en: {bubble_sort_path}")
    sys.exit(1)


class TestBubbleSort(unittest.TestCase):

    def test_ordenamiento_bubble_sort(self):
        """
        Verifica el ordenamiento de un array numérico con bubble sort.
        """
        initial_array = [3, 4, 7, 8, 1, 9, 5, 2, 6]
        expected_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n = len(initial_array)

        # Llama a tu función bubble_sort que modifica el array in-place
        bubble_sort(initial_array, n)

        # Verifica si el array ordenado es igual al esperado
        self.assertEqual(initial_array, expected_array, "El array no se ordenó correctamente.")
        print(f"Prueba 'test_ordenamiento_bubble_sort' PASÓ. Array final: {initial_array}")

    def test_ordenamiento_con_array_vacio(self):
        """
        Verifica el comportamiento de bubble sort con un array vacío.
        """
        empty_array = []
        expected_array = []
        n = len(empty_array)

        bubble_sort(empty_array, n)

        self.assertEqual(empty_array, expected_array, "El array vacío no se manejó correctamente.")
        print(f"Prueba 'test_ordenamiento_con_array_vacio' PASÓ. Array final: {empty_array}")

    def test_ordenamiento_con_array_ya_ordenado(self):
        """
        Verifica el comportamiento de bubble sort con un array ya ordenado.
        """
        sorted_array = [1, 2, 3, 4, 5]
        expected_sorted_array = [1, 2, 3, 4, 5]
        n = len(sorted_array)

        bubble_sort(sorted_array, n)

        self.assertEqual(sorted_array, expected_sorted_array, "El array ya ordenado no se mantuvo correctamente.")
        print(f"Prueba 'test_ordenamiento_con_array_ya_ordenado' PASÓ. Array final: {sorted_array}")

    def test_ordenamiento_con_elementos_duplicados(self):
        """
        Verifica el comportamiento de bubble sort con elementos duplicados.
        """
        duplicate_array = [5, 2, 8, 2, 5, 1]
        expected_array = [1, 2, 2, 5, 5, 8]
        n = len(duplicate_array)

        bubble_sort(duplicate_array, n)

        self.assertEqual(duplicate_array, expected_array, "El array con duplicados no se ordenó correctamente.")
        print(f"Prueba 'test_ordenamiento_con_elementos_duplicados' PASÓ. Array final: {duplicate_array}")

    def test_ordenamiento_con_un_solo_elemento(self):
        """
        Verifica el comportamiento de bubble sort con un array de un solo elemento.
        """
        single_element_array = [42]
        expected_array = [42]
        n = len(single_element_array)

        bubble_sort(single_element_array, n)

        self.assertEqual(single_element_array, expected_array, "El array de un solo elemento no se manejó correctamente.")
        print(f"Prueba 'test_ordenamiento_con_un_solo_elemento' PASÓ. Array final: {single_element_array}")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


"""
python -m unittest test_bubble_sort_unittest.py
O simplemente:


python test_bubble_sort_unittest.py



EXPLICACION DEL CODIGO
Explicación del código unittest:

import unittest: Importa el módulo de pruebas unitarias de Python.

import sys, os: Se utilizan para manipular la ruta de importación de Python.

sys.path.insert(0, bubble_sort_path): Esto es CRUCIAL. Agrega la ruta donde se encuentra tu archivo Algoritmos_de_clasificacion_Bubble_sort_burbujas.py al PYTHONPATH para que Python pueda encontrarlo cuando intentemos importarlo. He usado os.path.expanduser("~") que se expande a tu directorio home (ej. /home/death), haciendo la ruta más portable.

from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort: Importa específicamente la función bubble_sort de tu script.

class TestBubbleSort(unittest.TestCase):: Defines una clase de prueba que hereda de unittest.TestCase. Esto te da acceso a varios métodos de aserción (verificaciones) como assertEqual.

def test_ordenamiento_bubble_sort(self):: Cada método que comienza con test_ se considera un caso de prueba independiente por unittest.

initial_array = [...]: Defines el array de entrada.

expected_array = [...]: Defines el resultado esperado después del ordenamiento.

n = len(initial_array): Obtienes la longitud de la lista. Aquí len() es el len() de Python estándar, y siempre devuelve un entero.

bubble_sort(initial_array, n): Llama a tu función bubble_sort con los dos argumentos que espera.

self.assertEqual(initial_array, expected_array, "Mensaje de error si falla"): Esta es la aserción principal. unittest comparará el initial_array (modificado por tu función) con el expected_array. Si no son iguales, la prueba fallará y mostrará el mensaje proporcionado.

**`if name == 'main':
"""