import pytest
import sys
sys.path.append('/home/death/Documents/pythonIBM/proyectos/Test/PyTest/prueba_pytest1')
from Algoritmos_de_clasificacion_Bubble_sort_burbujas import bubble_sort
import io

@pytest.fixture
def suppress_output():
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    yield
    sys.stdout = old_stdout

def test_bubble_sort_unordered_array(suppress_output):
    initial_array = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    expected_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    length = len(initial_array)
    bubble_sort(initial_array, length)
    assert initial_array == expected_array

def test_bubble_sort_empty_array(suppress_output):
    empty_array = []
    length = len(empty_array)
    bubble_sort(empty_array, length)
    assert empty_array == []

def test_bubble_sort_sorted_array(suppress_output):
    sorted_array = [1, 2, 3, 4, 5]
    expected_array = [1, 2, 3, 4, 5]
    length = len(sorted_array)
    bubble_sort(sorted_array, length)
    assert sorted_array == expected_array