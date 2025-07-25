*** Settings ***
Library    /home/death/Documents/pythonIBM/proyectos/AlgoritmosPython/Algoritmos_de_clasificacion/Algoritmos_de_clasificacion_Bubble_sort_burbujas.py
Library    Collections

*** Test Cases ***
Verificar Ordenamiento Bubble Sort
    ${initial_array}=    Create List    3    4    7    8    1    9    5    2    6
    ${expected_array}=    Create List    1    2    3    4    5    6    7    8    9
    ${length}=    Get Length    ${initial_array}

    Log To Console    Array inicial para la prueba: ${initial_array}

    Bubble Sort    ${initial_array}    ${length}

    Log To Console    Array después del ordenamiento: ${initial_array}
    Log To Console    Array esperado: ${expected_array}

    Lists Should Be Equal    ${initial_array}    ${expected_array}
    Log To Console    ¡La prueba de ordenamiento de burbuja ha pasado exitosamente!

Verificar Ordenamiento con Array Vacio
    ${empty_array}=    Create List
    ${length}=    Get Length    ${empty_array}
    Bubble Sort    ${empty_array}    ${length}
    Lists Should Be Equal    ${empty_array}    ${empty_array}
    Log To Console    La prueba con array vacío ha pasado.

Verificar Ordenamiento con Array Ya Ordenado
    ${sorted_array}=    Create List    1    2    3    4    5
    ${expected_sorted_array}=    Create List    1    2    3    4    5
    ${length}=    Get Length    ${sorted_array}
    Bubble Sort    ${sorted_array}    ${length}
    Lists Should Be Equal    ${sorted_array}    ${expected_sorted_array}
    Log To Console    La prueba con array ya ordenado ha pasado.