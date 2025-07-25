"""
Ordenación por Mezcla: Explicación Básica

El Ordenamiento por Mezcla (Merge Sort) es un algoritmo de ordenación eficiente,
basado en comparaciones, que sigue el paradigma de "divide y vencerás".
Divide la lista no ordenada en 'n' sublistas, cada una conteniendo un solo elemento
(una lista de un elemento se considera ordenada).

Luego, fusiona repetidamente las sublistas para producir nuevas sublistas ordenadas
hasta que solo queda una sublista, que será la lista completamente ordenada.
"""


def merge(arr, left_index, mid_index, right_index):
    print(f"\n//////////////////////// ENTRANDO A merge: Rango [{left_index}, {right_index}] ///////\n")
    # Imprimir lo que la función merge está haciendo
    print(f"\n@@@@ FUSIONANDO: rango[{left_index},{right_index}] ARRAY SELECCIONADO : {arr[left_index:right_index + 1]} @@@@")

    # Crear sub-arrays izquierdo y derecho
    # El 'mid_index' es el último elemento del sub-array izquierdo
    left_array = arr[left_index: mid_index + 1]
    right_array = arr[mid_index + 1: right_index + 1]

    # Obtener las longitudes de los sub-arrays izquierdo y derecho
    left_array_length = mid_index - left_index + 1
    right_array_length = right_index - mid_index

    print(f"SUBARRAY izquierdo: {left_array} SUBARRAY derecho: {right_array}")

    # Índices para iterar a través de los dos sub-arrays
    i = 0  # Índice para left_array
    j = 0  # Índice para right_array

    # Índice para colocar elementos de nuevo en el array original 'arr'
    k = left_index

    # Iterar sobre los dos sub-arrays, comparando elementos y fusionándolos
    while i < left_array_length and j < right_array_length:
        # Comparar elementos de los sub-arrays izquierdo y derecho
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            print(f"Colocado {left_array[i]} del SUBARRAY izquierdo (izquierdo[{i}] < derecho[{j}])")
            i += 1
        else:
            arr[k] = right_array[j]
            print(f"Colocado {right_array[j]} del SUBARRAY derecho (izquierdo[{i}] >= derecho[{j}])")
            j += 1
        k += 1  # Mover a la siguiente posición en el array principal

    # Agregar los elementos restantes del sub-array izquierdo
    # (si el sub-array derecho se agotó primero)
    while i < left_array_length:
        print(f"Añadiendo el elemento restante {left_array[i]} del SUBARRAY izquierdo")
        arr[k] = left_array[i]
        i += 1
        k += 1

    # Agregar los elementos restantes del sub-array derecho
    # (si el sub-array izquierdo se agotó primero)
    while j < right_array_length:
        print(f"Añadiendo el elemento restante {right_array[j]} del SUBARRAY derecho")
        arr[k] = right_array[j]
        j += 1
        k += 1

    print(f"@@@@RESULTADO DE FUSIÓN para el rango [{left_index}, {right_index}]: {arr[left_index:right_index + 1]}@@@@\n")
    print(f"\n////////////////////////SALIENDO de merge: Rango [{left_index}, {right_index}] ///////\n")

def merge_sort(arr, left_index, right_index):
    # Imprimir cuando se entra a una llamada de merge_sort
    print(f"\n--------ENTRANDO A merge_sort: Rango [{left_index}, {right_index}]--------\n")

    # Caso base para la función recursiva: si el sub-array tiene 0 o 1 elemento
    if left_index >= right_index:
        print(f"El SUBARRAY [{left_index}, {right_index}] tiene 0 o 1 elementos.Regresando.")
        return  # termina la ejecución de la llamada actual de la función merge_sort
        # y devuelve el control a la función que la llamó

    # Encontrar el índice medio para dividir el array en dos mitades
    mid_index = (left_index + right_index) // 2

    # Imprimir la división del segmento actual del array
    print(f"Dividiendo el array de rango indices [{left_index} a {right_index}] \nArray seleccionado elementos  {arr[left_index : right_index + 1]} en:")
    print(F"SUBARRAY Izquierdo (llamada recursiva): arr[{left_index}:{mid_index + 1}] -> {arr[left_index: mid_index + 1]} "
          F"SUBARRAY Derecho (llamada recursiva): arr[{mid_index + 1}:{right_index + 1}] -> {arr[mid_index + 1: right_index + 1]}\n")

    # Llamadas recursivas para la mitad izquierda
    merge_sort(arr, left_index, mid_index)

    # Llamadas recursivas para la mitad derecha
    merge_sort(arr, mid_index + 1, right_index)

    # Después de las llamadas recursivas, fusionar los dos sub-arrays ordenados
    merge(arr, left_index, mid_index, right_index)

    # Imprimir cuando una llamada a merge_sort termina su fusión
    print(f"\n--------SALIENDO DE merge_sort: El rango [{left_index}, {right_index}] terminó de fusionarse.\n"
        f" Array general actual: {arr} --------\n")


if __name__ == '__main__':
    # Inicialización del array
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    print(f"Array Original: {arr}\n")

    # Llamar a merge_sort con el array y su rango de índices completo
    # Usar len(arr) - 1 para el right_index para manejar arrays de cualquier tamaño
    merge_sort(arr, 0, len(arr) - 1)

    # Imprimir el array ordenado final
    print(f"Array Ordenado Final: {str(arr)}")

"""
Análisis del Ordenamiento por Mezcla:

La complejidad temporal del Ordenamiento por Mezcla es O(n log n).
Esto se debe a que el array se divide en dos mitades en cada paso (log n pasos),
y el proceso de fusión toma un tiempo de O(n). Esto lo hace muy eficiente para grandes conjuntos de datos.

La complejidad espacial es O(n).
Esto se debe a que se crean arrays temporales (`left_array` y `right_array`)
durante el proceso de fusión, lo que requiere un espacio proporcional al tamaño de la entrada.
(Nota: Tu enunciado mencionaba una complejidad espacial de O(1), pero para una
implementación típica de merge sort que trabaja in-place, es O(n) debido a los arrays auxiliares.
Algunas implementaciones de merge sort in-place muy optimizadas y complejas pueden lograr O(1),
pero la implementación común es O(n)).
"""