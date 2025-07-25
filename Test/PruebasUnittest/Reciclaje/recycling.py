"""
Ejemplo 3. Reciclaje
Eres un conductor de camión de reciclaje. Le gustaría
recopilar algunas estadísticas sobre cuánto recicla
cada casa. Suponga que los números de las casas
son 0, 1, 2, 3...
Cada casa puso su reciclaje en cajas.
Calcula el número de la casa con la mayor cantidad
de reciclaje y la cantidad de cajas que recicla la casa.
Lo mismo para la casa con menos y el número de
cajas para esa casa.
Archivo recycling.py
"""
from collections import namedtuple
# Importa 'namedtuple' del módulo 'collections'.
# namedtuple es una subclase de tuple que permite acceder a los elementos por nombre
# (además de por índice).

CrateData = namedtuple('CrateData', ['houses', 'crates'])
# Define una nueva namedtuple llamada 'CrateData'.
# Tendrá dos campos: 'houses' (una lista de índices de casa) y 'crates' (el número de cajas).
# Esto mejora la legibilidad al devolver múltiples valores de una función.

def max_recycling(crates):
    # Define la función 'max_recycling' que encuentra el número máximo de cajas y las casas con esa cantidad.
    # 'crates' es una lista de números que representan las cajas en cada casa.

    """Returns the index with the largest value in the list and the number of crates for
    that house.
    Raises ValueError if list is empty."""
    # Docstring: Describe lo que hace la función y qué errores puede lanzar.

    if crates is None or len(crates) == 0:
        # Comprueba si la lista 'crates' es None (nula) o está vacía.
        raise ValueError('A list with at least one element is required')
        # Si es así, lanza un ValueError porque la función necesita al menos un elemento para operar.



    max_houses = []
    # Inicializa una lista vacía para almacenar los índices de las casas que tienen el número máximo de cajas.

    max_crates = crates[0]
    # Inicializa 'max_crates' con el valor de la primera casa. Se asume que es el máximo inicial.

    # 'houses' (una lista de índices de casa)
    # 'crates' (el número de cajas).
    # aqui  el número maximo  en las cajas
    for crate in crates:
        # Itera sobre cada 'crate' (cantidad de cajas) en la lista 'crates'.
        if crate > max_crates:
            # Si el valor de la 'crate' actual es mayor que el 'max_crates' encontrado hasta ahora:
            max_crates = crate
            # Actualiza 'max_crates' al nuevo valor máximo.
            # Nota: Este bucle solo encuentra el valor máximo, no las casas. Las casas se encuentran en el siguiente bucle.

    # aqui el número maximo en las cajas y las casas con esa cantidad maxima
    for house, crates_value in zip (range(len(crates)), crates):
        # Itera de nuevo sobre la lista 'crates', pero esta vez usando 'zip' para obtener
        # tanto el índice ('house') como el valor de las cajas ('crates_value') simultáneamente.
        # 'range(len(crates))' genera los índices (0, 1, 2, ...).
        # 'crates' son los valores de las cajas.

        if crates_value == max_crates:
            # Si el valor de las cajas para la casa actual es igual al valor máximo encontrado:
            max_houses.append(house)
            # Agrega el índice de esa casa a la lista 'max_houses'.

    return CrateData(max_houses, max_crates)
    # Devuelve una instancia de CrateData que contiene la lista de casas con el máximo
    # y el valor máximo de cajas.
    # max_houses para la lista de casas y max_crates para el valor

def min_recycling(crates):
    # Define la función 'min_recycling' para encontrar el número mínimo de cajas y las casas con esa cantidad.
    """Returns the smallest value in the list
    and a list of house number (list indexes) with that value.
    Raises ValueError if list is None or empty."""
    # Docstring similar a max_recycling.

    if crates is None or len(crates) == 0:
        # Comprueba si la lista es nula o vacía.
        raise ValueError('A list with at least one element is required')
        # Lanza un ValueError si la lista no es válida.

    min_houses = []
    # Inicializa una lista vacía para los índices de las casas con el mínimo.

    min_crates = crates[0]
    # Inicializa 'min_crates' con el valor de la primera casa. Se asume que es el mínimo inicial.
    # 'houses' (una lista de índices de casa)
    # 'crates' (el número de cajas).
    # aqui  el número mínimo en las cajas
    for crate in crates:
        # Itera sobre cada 'crate' en la lista.
        if crate < min_crates:
            # Si el valor de la 'crate' actual es menor que el 'min_crates' encontrado hasta ahora:
            min_crates = crate
            # Actualiza 'min_crates' al nuevo valor mínimo.

    # aqui el número mínimo en las cajas y las casas con esa cantidad minima
    for house, crates_value in zip (range(len(crates)), crates):
        # Itera de nuevo sobre la lista 'crates', obteniendo índice y valor.
        # siendo range(len(crates) los indices
        # crates  los valores

        if crates_value == min_crates:
            # Si el valor de las cajas para la casa actual es igual al valor mínimo encontrado:
            min_houses.append(house)
            # Agrega el índice de esa casa a la lista 'min_houses'.

    return CrateData(min_houses, min_crates)
    # Devuelve una instancia de CrateData con la lista de casas y el valor mínimo.

def total_crates(crates):
    # Define la función 'total_crates' para calcular la suma de todas las cajas.
    """ Return the total of all the values in the crates list"""
    # Docstring.

    total = 0
    # Inicializa el total en 0.

    for crate in crates:
        # Itera sobre cada 'crate' en la lista.
        total += crate
        # Suma el valor de la 'crate' actual al total.

    return total
    # Devuelve el total acumulado.

# con el numero de casas tenemos que introducir el numero de cajas de cada casa
def get_crate_quantities(houses):
    # Define la función 'get_crate_quantities' para pedir al usuario la cantidad de cajas por casa.
    """ Ask user for number of crates for each house"""
    # Docstring.

    crates = []
    # Inicializa una lista vacía para almacenar las cantidades de cajas introducidas.

    # recorremos la lista de casas
    for house in range(houses):
        # Itera para cada casa, desde 0 hasta 'houses - 1'.
        # positive_int_input  es LA ENTRADA DE USUARIO numero de cajas por casa
        # usamos la misma funcion para pedir un entero
        crates.append(positive_int_input('Enter crates for house {}'.format(house)))
        # Llama a 'positive_int_input' para obtener una entrada válida del usuario para cada casa.
        # Agrega la entrada validada a la lista 'crates'.

    return crates
    # Devuelve la lista de cantidades de cajas por casa.


# meter el numero de casas  y luego el numero de cajas por casa
def positive_int_input(question):
    # Define la función 'positive_int_input' para validar que el usuario ingrese un entero positivo.
    """ Valdiate user enters a positive integer """
    # Docstring.

    while True:
        # Inicia un bucle infinito que continuará hasta que se devuelva un valor válido.
        try:
            integer = int(input(question + ' '))
            # Intenta convertir la entrada del usuario a un entero.
            # 'question + ' '' agrega un espacio al final del mensaje de pregunta.

            if integer >= 0:
                # Si el entero es mayor o igual a 0 (considerado positivo en este contexto, incluyendo cero):
                return integer
                # Devuelve el entero válido, saliendo del bucle y de la función.
            else:
                # Si el entero es negativo:
                print('Please enter a positive integer.')
                # Imprime un mensaje de error y el bucle continúa.
        except ValueError:
            # Si la conversión a int falla (por ejemplo, el usuario ingresa texto no numérico):
            print('Please enter a positive integer.')
            # Imprime un mensaje de error y el bucle continúa.

def main():
    # Define la función 'main', que es el punto de entrada principal del programa.

    print('Recycling truck program')
    # Imprime un mensaje de bienvenida.

    houses = positive_int_input('How many houses?')
    # Pide al usuario el número de casas y valida que sea un entero positivo.

    crates = get_crate_quantities(houses)
    # Llama a 'get_crate_quantities' para obtener la cantidad de cajas para cada casa.

    maximums = max_recycling(crates)
    # Llama a 'max_recycling' para obtener los datos del máximo.

    minimums = min_recycling(crates)
    # Llama a 'min_recycling' para obtener los datos del mínimo.

    total = total_crates(crates)
    # Llama a 'total_crates' para obtener el total.

    print('The total number of crates set out on the street is {}'.format(total))
    # Imprime el total de cajas.

    print('The max number of crates from any house is {}'.format(maximums.crates))
    # Imprime el valor máximo de cajas.

    print('The house(s) with the most recycling is {}'.format(maximums.houses))
    # Imprime la(s) casa(s) con el mayor número de cajas.

    print('The min number of crates from any house is {}'.format(minimums.crates))
    # Imprime el valor mínimo de cajas.

    print('The house(s) with the least recycling is {}'.format(minimums.houses))
    # Imprime la(s) casa(s) con el menor número de cajas.

if __name__ == '__main__':
    # Este bloque se ejecuta solo si el script se ejecuta directamente.

    main()
    # Llama a la función 'main' para iniciar el programa.


"""
Recycling truck program
How many houses? 10
                            (es un error si no das un entero solo)
                            Enter crates for house 0 1 2 3 4 5  
                            Please enter a positive integer.
Enter crates for house 0 10
Enter crates for house 1 10
Enter crates for house 2 10
Enter crates for house 3 20
Enter crates for house 4 25
Enter crates for house 5 30
Enter crates for house 6 40
Enter crates for house 7 33
Enter crates for house 8 33
Enter crates for house 9 22
The total number of crates set out on the street is 233
The max number of crates from any house is 40
The house(s) with the most recycling is [6]
The min number of crates from any house is 10
The house(s) with the least recycling is [0, 1, 2]
"""