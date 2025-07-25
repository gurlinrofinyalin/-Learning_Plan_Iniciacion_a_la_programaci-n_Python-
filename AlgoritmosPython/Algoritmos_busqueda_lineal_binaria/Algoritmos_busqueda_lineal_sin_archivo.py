"""
la búsqueda lineal.
Entonces decidimos revisar toda la lista buscando a
la persona a autenticar y llegamos a la siguiente
implementación:
"""

from array import array
from pathlib import Path
import pickle  # No se usa en este código, pero se mantiene si es relevante para otras partes.

import time
# La función importar_lista se mantiene aquí, pero no será usada en main()
def importar_lista(archivo):
    lista = []
    # Usamos .exists() para verificar antes de abrir
    if not archivo.exists():
        print(f"Error: El archivo no se encontró en la ruta: {archivo.absolute()}")
        return []

    with open(archivo, 'r', encoding='utf-8') as tf:
        for line in tf:
            lista.append(line.strip())
    return lista


# La función buscar (búsqueda lineal)
def buscar(lista, nombre_buscado):
    for indice, valor_actual in enumerate(lista):
        if valor_actual == nombre_buscado:
            return indice
    return -1


def main():
    # La lista de alumnos se proporciona directamente aquí (hardcodeada)
    # y ya no se intenta importar de un archivo.
    lista_de_alumnos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]

    # Si quisieras que la lista estuviera ordenada para una búsqueda binaria posterior,
    # descomentarías la siguiente línea, pero para búsqueda lineal no es estrictamente necesario.
    # lista_de_alumnos = sorted(lista_de_alumnos)

    print(f"Lista de alumnos a buscar: {lista_de_alumnos}")

    nombre_a_buscar = "Wanessa"

    # La búsqueda se realiza y se imprime una única vez (sin el bucle for)
    posicion_del_alumno = buscar(lista_de_alumnos, nombre_a_buscar)

    if posicion_del_alumno != -1:
        print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))
    else:
        print(f"El alumno(a) {nombre_a_buscar} no se encontró en la lista.")


if __name__ == "__main__":
    start_time = time.time()  # Registra el tiempo de inicio

    main()  # Llama a la función principal

    end_time = time.time()  # Registra el tiempo de finalización
    execution_time = end_time - start_time  # Calcula la duración

    print(f"\nTiempo de ejecución de main(): {execution_time:.6f} segundos")
