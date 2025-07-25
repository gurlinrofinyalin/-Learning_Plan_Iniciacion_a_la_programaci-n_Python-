from array import array  # Se mantiene si es relevante para otros contextos, aunque no se usa directamente aquí.
from pathlib import Path
import time
import pickle  # Se mantiene si es relevante para otras partes.


# Función para importar lista desde un archivo (corregida)
def importar_lista(archivo_path: Path):  # Acepta un objeto Path
    lista = []
    if not archivo_path.exists():
        print(f"Error: El archivo no se encontró en la ruta: {archivo_path.absolute()}")
        return []  # Devuelve una lista vacía si el archivo no existe

    with open(archivo_path, 'r', encoding='utf-8') as tf:
        for line in tf:
            lista.append(line.strip())  # Lee línea por línea y elimina espacios/saltos de línea
    return lista


# La función buscar (Búsqueda Binaria optimizada)
def buscar(lista, nombre_buscado):
    inicio = 0
    fin = len(lista) - 1  # Corregido 'fim' a 'fin'

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Corregido 'meio' a 'medio'

        # Comprobación de que 'medio' es un índice válido
        if not (0 <= medio < len(lista)):
            break  # Salir si el índice medio es inválido (nunca debería ocurrir con la lógica correcta)

        if lista[medio] == nombre_buscado:
            return medio  # Elemento encontrado
        elif lista[medio] < nombre_buscado:  # Si el elemento del medio es menor, busca en la mitad derecha
            inicio = medio + 1
        else:  # Si lista[medio] > nombre_buscado, busca en la mitad izquierda
            fin = medio - 1

    return -1  # Elemento no encontrado después de revisar toda la lista


def main():
    # Opción 1: Usar una lista hardcodeada directamente (como en tu última petición)
    # **IMPORTANTE: Para búsqueda binaria, esta lista DEBE ESTAR ORDENADA.**
    lista_de_alumnos = ["Brendo", "Erica", "Monica", "Nico", "Paulo", "Rodrigo", "Wanessa"]
    # Si la lista no estuviera ordenada y la obtuvieras de otra fuente, la ordenarías así:
    # lista_de_alumnos = sorted(lista_de_alumnos_original)

    # Opción 2: Importar desde un archivo (asegúrate de que el archivo exista y esté ordenado)
    # Por ejemplo, si tienes 'lista_alumnos.txt' en una carpeta 'data' al mismo nivel que tu script:
    # ruta_archivo = Path('data') / 'lista_alumnos.txt'
    # lista_de_alumnos = sorted(importar_lista(ruta_archivo)) # Asegurarse de ordenar si el archivo no lo garantiza

    print(f"Lista de alumnos: {lista_de_alumnos}")

    nombre_a_buscar = "Wanessa"  # Cambiado a "Wanessa" para un resultado exitoso con la lista hardcodeada
    # Si quieres buscar "Zoraida" y la lista proviene de un archivo, asegúrate que "Zoraida" esté en ese archivo
    # y que el archivo esté ordenado alfabéticamente.

    # La búsqueda y la impresión se realizan una única vez.
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
