"""
La ordenación por inserción es uno de los algoritmos
de ordenación más simples.

Es fácil de implementar, pero a la hora de ordenar matrices
necesitará más tiempo.

No es recomendable para clasificar matrices grandes.

El algoritmo mantiene subpartes ordenadas y no
ordenadas en la matriz dada.

La subparte contiene solo el primer elemento al
comienzo del proceso de clasificación.

Tomaremos un elemento de la matriz no ordenada y los
colocaremos en la posición correcta en la sub-matriz
ordenada.

Veamos las ilustraciones visuales de tipo de
inserción paso a paso con un ejemplo.

subparte ordenada                         subparte sin ordenar
resuelto 4            [4][1][2][5][3]     sin clasificar  1 2 5 3
resuelto 1 4          [1][4](1)[2][5][3]  sin clasificar    2 5 3
resuelto 1 2 4        [1][2][4](2)[5][3]  sin clasificar      5 3
resuelto 1 2 4 5      [1][2][4](5)[3]     sin clasificar        3
resuelto 1 2 3 4 5    [1][2][3][4][5](3)  sin clasificar     Nada
"""



def insertion_sort(arr, n): # array y numero de elementos del array
    for i in range(1, n):  # rango de 1  a 8 , el 9 no cuenta m la ultima cifra esta ordenada
        # Current position and element
        # Posición y elemento actuales
        current_position = i
        current_element = arr[i]

        # Iterate until the first element is reached
        # or the current element is smaller than the previous element
        # Iterar hasta alcanzar el primer elemento
        # o hasta que el elemento actual sea menor que el anterior
        # current_position > 0  es la primera posicion
        #current_element < arr[current_position - 1] m el elemento actual sea menor que el anterior
        while current_position > 0 and current_element < arr[current_position - 1]:
            # Update the current element with the previous element
            # Actualizar el elemento actual con el anterior
            # osease desplazar elemento de la izquierda hacia la derecha
            anterior = arr[current_position -1 ]
            actual = arr[current_position]

            arr[current_position] = arr[current_position - 1]
            # Move to the previous position
            # Mover a la posición anterior
            # coger la posicion de la izquierda
            current_position -= 1
            print(" anterior", anterior, " = actual ", actual, "array ", arr, "guardo", current_element)


        # Update the current position element
        # Actualizar el elemento en la posición actual
        # devolvemos el elemento a la posicion donde estamos ahora despues
        # de habernos desplazado a la izquierda
        arr[current_position] = current_element

        print(arr)

        """
 
[3, 4, 7, 8, 1, 9, 5, 2, 6]
[3, 4, 7, 8, 1, 9, 5, 2, 6]
[3, 4, 7, 8, 1, 9, 5, 2, 6]  inicio en el 8, 1
 anterior 8  = actual  1 array  [3, 4, 7, 8, 8, 9, 5, 2, 6] guardo 1
 anterior 7  = actual  8 array  [3, 4, 7, 7, 8, 9, 5, 2, 6] guardo 1
 anterior 4  = actual  7 array  [3, 4, 4, 7, 8, 9, 5, 2, 6] guardo 1
 anterior 3  = actual  4 array  [3, 3, 4, 7, 8, 9, 5, 2, 6] guardo 1
[1, 3, 4, 7, 8, 9, 5, 2, 6]
[1, 3, 4, 7, 8, 9, 5, 2, 6]
 anterior 9  = actual  5 array  [1, 3, 4, 7, 8, 9, 9, 2, 6] guardo 5
 anterior 8  = actual  9 array  [1, 3, 4, 7, 8, 8, 9, 2, 6] guardo 5
 anterior 7  = actual  8 array  [1, 3, 4, 7, 7, 8, 9, 2, 6] guardo 5
[1, 3, 4, 5, 7, 8, 9, 2, 6]
 anterior 9  = actual  2 array  [1, 3, 4, 5, 7, 8, 9, 9, 6] guardo 2
 anterior 8  = actual  9 array  [1, 3, 4, 5, 7, 8, 8, 9, 6] guardo 2
 anterior 7  = actual  8 array  [1, 3, 4, 5, 7, 7, 8, 9, 6] guardo 2
 anterior 5  = actual  7 array  [1, 3, 4, 5, 5, 7, 8, 9, 6] guardo 2
 anterior 4  = actual  5 array  [1, 3, 4, 4, 5, 7, 8, 9, 6] guardo 2
 anterior 3  = actual  4 array  [1, 3, 3, 4, 5, 7, 8, 9, 6] guardo 2
[1, 2, 3, 4, 5, 7, 8, 9, 6]
 anterior 9  = actual  6 array  [1, 2, 3, 4, 5, 7, 8, 9, 9] guardo 6
 anterior 8  = actual  9 array  [1, 2, 3, 4, 5, 7, 8, 8, 9] guardo 6
 anterior 7  = actual  8 array  [1, 2, 3, 4, 5, 7, 7, 8, 9] guardo 6
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
        """

if __name__ == '__main__':
    # Array initialization
    arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
    insertion_sort(arr, len(arr))  # Use len(arr) for the array size
    # Printing the array
    print(str(arr))

"""
el algoritmo de ordenamiento por inserción 
 
 He realizado un pequeño ajuste en la llamada a la función insertion_sort dentro del 
 bloque if __name__ == '__main__':.

Originalmente tenías insertion_sort(arr, 9).  
Si bien 9 es el tamaño actual del array,  es una buena práctica usar len(arr) en su lugar. 
Esto hace que el código sea más flexible y robusto,  ya que si cambias el número de 
elementos en el array arr,  no necesitarás recordar actualizar manualmente el segundo 
argumento de la función  insertion_sort.

La complejidad temporal de O(n ^ 2 ) 
y la complejidad espacial de O(1) que mencionas son correctas 
para el ordenamiento por inserción. 

La complejidad temporal de O(n ^ 2 ) 
a medida que el tamaño del array (n) aumenta, 
el tiempo que tarda el algoritmo en ejecutarse crece cuadráticamente, 

la complejidad espacial o recursos de O(1) 
mientras que la cantidad de memoria adicional que utiliza permanece constante.
"""



