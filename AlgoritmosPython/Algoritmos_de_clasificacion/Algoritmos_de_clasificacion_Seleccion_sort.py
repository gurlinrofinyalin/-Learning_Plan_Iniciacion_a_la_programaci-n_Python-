"""
Selection Sort: Basic Explanation
Ordenación por Selección: Explicación Básica

Selection Sort is similar to Insertion Sort in concept.
This algorithm also divides the array into sorted and unsorted sub-parts.
In each iteration, it finds the minimum element from the unsorted sub-part
and places it at the end of the sorted sub-part.

El orden de selección es similar al orden de inserción en concepto.
Este algoritmo también divide la matriz en subpartes ordenadas y no ordenadas.
Y luego, en cada iteración, tomará el elemento mínimo de la subparte sin clasificar
y lo colocará en la última posición de la subparte ordenada.
"""


def selection_sort(arr, n):
    # Iterate through the entire array
    # Iterar a través de todo el array
    for i in range(n): # rango de 0 a 8 porque array es de 9
        # Store the index of the minimum element in the unsorted part
        # Almacenar el índice del elemento mínimo en la parte no ordenada
        min_element_index = i
        print(arr)# para imprimir
        elementominimo =arr[min_element_index]# para imprimir ,  por defecto -1 lo pongo yo
        # Find the minimum element in the remaining unsorted array
        # Encontrar el elemento mínimo en el resto del array no ordenado
        for j in range(i + 1, n): # para recorrer numero de elementos -1
            # Check and replace the minimum element's index if a smaller one is found
            # Comprobar y reemplazar el índice del elemento mínimo si se encuentra uno más pequeño
            # si el elemento
            ver  = "elemento a comprobar actual ",arr[j] ,"< elemento minimo anterior", arr[min_element_index], "array", arr
            if arr[j] < arr[min_element_index]:
                min_element_index = j
                elementominimo = arr[min_element_index]

            ver += " minimo actual ", elementominimo
            print(ver)


        # Swap the current element (arr[i]) with the found minimum element
        # Intercambiar el elemento actual (arr[i]) con el elemento mínimo encontrado
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
        if arr[min_element_index] == arr[i]:
            print("No hay cambio ya estan ordenados")
        else:
            print("elemento minimo",elementominimo ,"cambio de ", arr[min_element_index] ,"a", arr[i] ,"y viceversa")


"""
[3, 4, 7, 8, 1, 9, 5, 2, 6]
('elemento a comprobar actual ', 4, '< elemento minimo anterior', 3, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 7, '< elemento minimo anterior', 3, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 3, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 1, '< elemento minimo anterior', 3, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 1)
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 1, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 1)
('elemento a comprobar actual ', 5, '< elemento minimo anterior', 1, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 1)
('elemento a comprobar actual ', 2, '< elemento minimo anterior', 1, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 1)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 1, 'array', [3, 4, 7, 8, 1, 9, 5, 2, 6], ' minimo actual ', 1)
elemento minimo 1 cambio de  3 a 1 y viceversa
[1, 4, 7, 8, 3, 9, 5, 2, 6]
('elemento a comprobar actual ', 7, '< elemento minimo anterior', 4, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 4)
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 4, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 4)
('elemento a comprobar actual ', 3, '< elemento minimo anterior', 4, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 3, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 5, '< elemento minimo anterior', 3, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 2, '< elemento minimo anterior', 3, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 2)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 2, 'array', [1, 4, 7, 8, 3, 9, 5, 2, 6], ' minimo actual ', 2)
elemento minimo 2 cambio de  4 a 2 y viceversa
[1, 2, 7, 8, 3, 9, 5, 4, 6]
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 7, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 3, '< elemento minimo anterior', 7, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 3, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 5, '< elemento minimo anterior', 3, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 4, '< elemento minimo anterior', 3, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 3)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 3, 'array', [1, 2, 7, 8, 3, 9, 5, 4, 6], ' minimo actual ', 3)
elemento minimo 3 cambio de  7 a 3 y viceversa
[1, 2, 3, 8, 7, 9, 5, 4, 6]
('elemento a comprobar actual ', 7, '< elemento minimo anterior', 8, 'array', [1, 2, 3, 8, 7, 9, 5, 4, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 8, 7, 9, 5, 4, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 5, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 8, 7, 9, 5, 4, 6], ' minimo actual ', 5)
('elemento a comprobar actual ', 4, '< elemento minimo anterior', 5, 'array', [1, 2, 3, 8, 7, 9, 5, 4, 6], ' minimo actual ', 4)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 4, 'array', [1, 2, 3, 8, 7, 9, 5, 4, 6], ' minimo actual ', 4)
elemento minimo 4 cambio de  8 a 4 y viceversa
[1, 2, 3, 4, 7, 9, 5, 8, 6]
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 7, 9, 5, 8, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 5, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 7, 9, 5, 8, 6], ' minimo actual ', 5)
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 5, 'array', [1, 2, 3, 4, 7, 9, 5, 8, 6], ' minimo actual ', 5)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 5, 'array', [1, 2, 3, 4, 7, 9, 5, 8, 6], ' minimo actual ', 5)
elemento minimo 5 cambio de  7 a 5 y viceversa
[1, 2, 3, 4, 5, 9, 7, 8, 6]
('elemento a comprobar actual ', 7, '< elemento minimo anterior', 9, 'array', [1, 2, 3, 4, 5, 9, 7, 8, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 5, 9, 7, 8, 6], ' minimo actual ', 7)
('elemento a comprobar actual ', 6, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 5, 9, 7, 8, 6], ' minimo actual ', 6)
elemento minimo 6 cambio de  9 a 6 y viceversa
[1, 2, 3, 4, 5, 6, 7, 8, 9]
('elemento a comprobar actual ', 8, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 5, 6, 7, 8, 9], ' minimo actual ', 7)
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 7, 'array', [1, 2, 3, 4, 5, 6, 7, 8, 9], ' minimo actual ', 7)
No hay cambio ya estan ordenados
[1, 2, 3, 4, 5, 6, 7, 8, 9]
('elemento a comprobar actual ', 9, '< elemento minimo anterior', 8, 'array', [1, 2, 3, 4, 5, 6, 7, 8, 9], ' minimo actual ', 8)
No hay cambio ya estan ordenados
[1, 2, 3, 4, 5, 6, 7, 8, 9]
No hay cambio ya estan ordenados
[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


if __name__ == '__main__':
    # Array initialization
    # Inicialización del array
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]

    # Sort the array using selection sort
    # Use len(arr) for automatic array size, making the code more robust
    # Ordenar el array usando el algoritmo de ordenación por selección
    # Usar len(arr) para obtener automáticamente el tamaño del array, haciendo el código más robusto
    selection_sort(arr, len(arr))

    # Print the sorted array
    # Imprimir el array ordenado
    print(str(arr))

"""
Analysis of Selection Sort:
Análisis del Ordenamiento por Selección:

The time complexity of Selection Sort is O(n^2).
This is because for an array of n elements, there are n iterations,
and in each iteration, we scan through up to n elements to find the minimum.

La complejidad temporal del Ordenamiento por Selección es O(n^2).
Esto se debe a que para un array de n elementos, hay n iteraciones,
y en cada iteración, se recorren hasta n elementos para encontrar el mínimo.

The space complexity is O(1).
This indicates that the amount of additional memory used remains constant,
regardless of the input array's size, as it only requires a few temporary
variables for swapping.

La complejidad espacial es O(1).
Esto indica que la cantidad de memoria adicional utilizada permanece constante,
independientemente del tamaño del array de entrada, ya que solo requiere unas
pocas variables temporales para el intercambio.
"""
