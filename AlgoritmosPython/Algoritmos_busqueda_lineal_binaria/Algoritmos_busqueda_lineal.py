"""
la búsqueda lineal.
Entonces decidimos revisar toda la lista buscando a
la persona a autenticar y llegamos a la siguiente
implementación:
"""
from array import array


from pathlib import Path
import pickle # No se usa en este código, pero se mantiene si es relevante para otras partes.
import time

# La función importar_lista debe definirse antes de main()
def importar_lista(archivo):
    lista = []
    with open(archivo, 'r', encoding='utf-8') as tf: # 'r' para leer, 'utf-8' por si hay acentos o ñ
        for line in tf: # Iterar directamente sobre el archivo lee línea por línea
            lista.append(line.strip()) # .strip() para eliminar saltos de línea y espacios en blanco
    return lista

# La función buscar (búsqueda lineal)
def buscar(lista, nombre_buscado):
    # En Python, puedes iterar directamente y usar enumerate para obtener índice y valor
    for indice, valor_actual in enumerate(lista):
        if valor_actual == nombre_buscado:
            return indice # Devuelve la posición si lo encuentra
    return -1 # Devuelve -1 si no lo encuentra

def main():
    # Asegúrate de que la ruta al archivo sea correcta.
    # Si 'lista_alumnos.txt' está en la misma carpeta que el script:
    ruta_archivo = Path('./data/lista_alumnos')

    # Ordenar la lista es bueno si luego harás una búsqueda binaria, pero para lineal no es estrictamente necesario.
    # Sin embargo, mantiene el ejemplo original.
    lista_de_alumnos = sorted(importar_lista(ruta_archivo))
    print(f"Lista de alumnos importada (y ordenada): {lista_de_alumnos}")

    nombre_a_buscar = "Wanessa"
    posicion_del_alumno = buscar(lista_de_alumnos, nombre_a_buscar) # Variable corregida

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
