"""
Archivo: test_bubble_sort_doctest.py
Pruebas para Bubble Sort usando DocTest - Versión que maneja los prints
"""

import doctest
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort

def test_bubble_sort():
    """
    Pruebas para bubble_sort() manejando la salida impresa.
    Usamos # doctest: +ELLIPSIS para ignorar partes variables de los prints.

    Ejemplos:
    >>> # Test 1 - Lista desordenada
    >>> arr = [5, 3, 8, 6, 2]
    >>> bubble_sort(arr, len(arr))  # doctest: +ELLIPSIS
    --- Comienza la clasificacion  Bubble Sort ---
    --- Va de izquierda a derecha...
    >>> arr
    [2, 3, 5, 6, 8]

    >>> # Test 2 - Lista ya ordenada
    >>> arr = [1, 2, 3, 4, 5]
    >>> bubble_sort(arr, len(arr))  # doctest: +ELLIPSIS
    --- Comienza la clasificacion...
    >>> arr
    [1, 2, 3, 4, 5]

    >>> # Test 3 - Lista vacía
    >>> arr = []
    >>> bubble_sort(arr, len(arr))  # doctest: +ELLIPSIS
    --- Comienza la clasificacion...
    >>> arr
    []

    >>> # Test 4 - Un elemento
    >>> arr = [9]
    >>> bubble_sort(arr, len(arr))  # doctest: +ELLIPSIS
    --- Comienza la clasificacion...
    >>> arr
    [9]
    """
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    print("🔸 Iniciando pruebas de Bubble Sort (manejando output)...")
    test_bubble_sort()
    print("✅ Pruebas completadas")