"""
Ejemplo 2. Camel case
Un diccionario de entradas con salidas esperadas.

También utiliza parches para parchear las funciones
integradas de entrada y salida para probar la entrada
del usuario y la salida correcta que se está
imprimiendo.

Observe el uso del administrador de contexto de parches,
que se encarga de quitar los parches cuando haya terminado.

De lo contrario, es posible que deba reemplazar las funciones de
entrada/impresión originales.

"""

# Importa el módulo 're' (regular expressions), que se utilizará para manipular cadenas.
import re

def capitalize(word):
    # Define una función llamada 'capitalize' que toma una 'word' (palabra) como entrada.
    """ Convierta la palabra para que tenga la primera letra en mayúscula, el resto en
    minúsculas"""
    # Docstring: Explica lo que hace la función.
    return word[0:1].upper() + word[1:].lower()
    # Toma la primera letra de la palabra (word[0:1]), la convierte a mayúscula (.upper()).
    # Toma el resto de la palabra (word[1:]), lo convierte a minúscula (.lower()).
    # Concatena ambos resultados y los devuelve.
    # Los segmentos (slices) no producen errores de tipo "index out of bounds" (índice fuera de límites).
    # Así que esto todavía funciona en cadenas vacías y cadenas de longitud 1.
    # Por ejemplo, si word es "", word[0:1] es "" y word[1:] es "", resultando en "".
    # Si word es "a", word[0:1] es "a", word[1:] es "", resultando en "A".

def lowercase(word):
    # Define una función llamada 'lowercase' que toma una 'word' (palabra) como entrada.
    """convierte una palabra a minúsculas"""
    # Docstring: Explica lo que hace la función.
    return word.lower()
    # Devuelve la palabra completamente convertida a minúsculas utilizando el método incorporado de cadenas.

def camel_case(sentence):
    # Define la función principal 'camel_case' que toma una 'sentence' (frase) como entrada.

    remove_multiple_spaces = re.sub(r'\s+', ' ', sentence)
    # Reemplaza cualquier grupo de espacios en blanco con un solo espacio

    # Utiliza la expresión regular 're.sub' para reemplazar una o más (\s+) ocurrencias
    # de espacios en blanco (incluyendo espacios, tabulaciones, saltos de línea) con un solo espacio.
    # Esto limpia la frase de espacios redundantes.(deja 1 solo espacio si lo hay)

    remove_surrounding_space = remove_multiple_spaces.strip()
    # elimina cualquier espacio en blanco restante
    # Utiliza el método '.strip()' para eliminar cualquier espacio en blanco
    #  (al principio o al final de la cadena resultante.

    words = remove_surrounding_space.split(' ') # Segmenta por espacios
    # Divide la cadena limpia en una lista de palabras,
    # utilizando un solo espacio como delimitador.

    first_word = lowercase(words[0]) # Pasa a minúsculas la primera palabra
    # Toma la primera palabra de la lista (words[0]) y la convierte completamente a minúsculas
    # utilizando la función 'lowercase' definida anteriormente.

    # Escribe con mayúscula la segunda palabra y las siguientes y las pone en una nueva lista.
    capitalized_words = [ capitalize(word) for word in words[ 1: ] ]
    # Usa una comprensión de lista (list comprehension) para iterar sobre todas las palabras
    # de la lista 'words' EXCEPTO la primera (words[1:]).
    # la primera palabra seria words[0]
    # Para cada una de estas palabras, aplica la función 'capitalize' y el resultado se añade
    # a la nueva lista 'capitalized_words'.

    # Reúne todas las palabras en una lista
    camel_cased_words = [first_word] + capitalized_words
    # Crea una nueva lista concatenando 'first_word' (que está en minúsculas)
    # con la lista de 'capitalized_words' (el resto de palabras con mayúscula inicial).

    # Vuelve a juntar las palabras
    camel_cased_sentance = ''.join(camel_cased_words)
    # Une todos los elementos de la lista 'camel_cased_words' en una sola cadena,
    # sin ningún separador entre ellas (porque se usa una cadena vacía '').
    # Esto forma la cadena en formato camel case final.
    # palabraPalabraPalabraPalabra

    return camel_cased_sentance
    # Devuelve la frase convertida a camel case.

def main():
    # Define la función 'main', que es el punto de entrada principal cuando el script se ejecuta directamente.

    sentence = input('Introduzca la frase: ')
    # Pide al usuario que introduzca una frase y guarda la entrada en la variable 'sentence'.

    camelcased = camel_case(sentence)
    # Llama a la función 'camel_case' con la frase introducida por el usuario
    # y guarda el resultado en 'camelcased'.

    print(camelcased)
    # Imprime la frase convertida a camel case en la consola.

if __name__ == '__main__':
    # Este bloque de código se ejecuta solo si el script se está ejecutando directamente
    # (no si está siendo importado como un módulo en otro script).

    main()
    # Llama a la función 'main()' para iniciar la ejecución del programa.