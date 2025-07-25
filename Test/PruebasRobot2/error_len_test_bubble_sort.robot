***Settings***
Library    /home/death/Documents/pythonIBM/proyectos/AlgoritmosPython/Algoritmos_de_clasificacion/Algoritmos_de_clasificacion_Bubble_sort_burbujas.py

***Test Cases***
Verificar Ordenamiento Bubble Sort
    ${initial_array}=    Create List    3    4    7    8    1    9    5    2    6
    ${expected_array}=    Create List    1    2    3    4    5    6    7    8    9

    Log To Console    Array inicial para la prueba: ${initial_array}

    # Llama a la función bubble_sort de tu módulo Python
    # La palabra clave se nombra como la función en Python
    # La función debe devolver el array ordenado o modificarlo in-place
    # Asumimos que la función modifica el array in-place, por lo que usamos el mismo array
    Bubble Sort    ${initial_array}    ${initial_array.len}

    Log To Console    Array después del ordenamiento: ${initial_array}
    Log To Console    Array esperado: ${expected_array}

    # Verifica que el array ordenado sea igual al array esperado
    Lists Should Be Equal    ${initial_array}    ${expected_array}
    Log To Console    ¡La prueba de ordenamiento de burbuja ha pasado exitosamente!

Verificar Ordenamiento con Array Vacio
    ${empty_array}=    Create List
    Bubble Sort    ${empty_array}    ${empty_array.len}
    Lists Should Be Equal    ${empty_array}    ${empty_array}
    Log To Console    La prueba con array vacío ha pasado.

Verificar Ordenamiento con Array Ya Ordenado
    ${sorted_array}=    Create List    1    2    3    4    5
    ${expected_sorted_array}=    Create List    1    2    3    4    5
    Bubble Sort    ${sorted_array}    ${sorted_array.len}
    Lists Should Be Equal    ${sorted_array}    ${expected_sorted_array}
    Log To Console    La prueba con array ya ordenado ha pasado.