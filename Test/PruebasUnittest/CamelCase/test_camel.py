import unittest
# Importa el módulo 'unittest', que proporciona el marco para escribir pruebas.

from unittest.mock import patch
# Importa 'patch' del módulo 'unittest.mock'. 'patch' se usa para "simular" o "reemplazar"
# temporalmente funciones, métodos o atributos durante las pruebas (mocking).

import camel
# Importa el módulo o archivo 'camel' (que contiene las funciones a probar).

class TestCamelCase(unittest.TestCase):
    # una clase 'TestCamelCase'. Hereda de 'unittest.TestCase',
    # lo que le da acceso a métodos de aserción (como assertEqual)
    # y a la capacidad de ser descubierto y ejecutado por el ejecutor de pruebas de unittest.

    # Los nombres de los métodos de prueba deben comenzar con 'test_'.
    # Un método de prueba para la función 'capitalize' en el módulo 'camel'.

    def test_capitalize(self):
        """
        test_capitalize (test_camel.TestCamelCase.test_capitalize)
        Qué comprueba: Que la función camel.capitalize() convierte una palabra de forma
        que solo la primera letra esté en mayúscula y el resto en minúscula,
        independientemente de la capitalización original.

        Ejemplo de Entrada (input): word = "aBC"
        Ejemplo de Salida Esperada (expected output): "Abc"
        """
        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        # Define una lista de palabras de entrada que se usarán para probar la función.

        capitalized = 'Abc'
        # Define el resultado esperado después de capitalizar correctamente.

        for word in input_words:
            # Itera sobre cada palabra en la lista 'input_words'.

            self.assertEqual(capitalized, camel.capitalize(word))
            # camel.capitalize(word) es una de las funciones del modulo o archivo camel
            # Utiliza 'assertEqual' (un método de 'unittest.TestCase') para verificar
            # que el resultado de llamar a 'camel.capitalize(word)' sea igual a 'capitalized'.
            # Si no son iguales, esta prueba fallará.

    def test_lower(self):
        """
        test_lower (test_camel.TestCamelCase.test_lower)
        Qué comprueba: Que la función camel.lowercase() convierte cualquier palabra
         completamente a minúsculas, sin importar su capitalización original.

        Ejemplo de Entrada (input): word = "ABc"
        Ejemplo de Salida Esperada (expected output): "abc"
        """
        # Un método de prueba para la función 'lowercase'.

        # this isn't really needed, since we can assume that Python's library functions
        # work correctly :)
        # Comentario: Indica que esta prueba es un poco redundante porque se basa
        # en una función interna de Python ('lower()') que ya se asume que funciona.
        # Sin embargo, puede ser útil para una cobertura completa o si 'lowercase'
        # tuviera lógica adicional.

        input_words = ['abc', 'ABC', 'aBC', 'ABc']
        # Lista de palabras de entrada.

        lower = 'abc'
        # Resultado esperado (todas en minúsculas).

        for word in input_words:
            # Itera sobre las palabras de entrada.

            self.assertEqual(lower, camel.lowercase(word))
            # Afirma que la salida de 'camel.lowercase' coincide con el resultado esperado.
            # camel.lowercase(word) es una de las funciones del modulo o archivo camel

    def test_camel_case_single_words(self):
        """
        test_camel_case_single_words (test_camel.TestCamelCase.test_camel_case_single_words)
        Qué comprueba: Que la función camel.camel_case() maneja correctamente las entradas
        de una sola palabra, simplemente convirtiéndolas a minúsculas sin añadir
        capitalización extra (ya que no hay segundas palabras).

        Ejemplo de Entrada (input): sentence = "Hello"
        Ejemplo de Salida Esperada (expected output): "hello"
        """
        # Prueba la función 'camel_case' con palabras individuales (sin espacios).

        input_and_expected_outputs = {
            'hello' : 'hello',
            'Hello' : 'hello',
            'Thisisaverylongwordlalalalalalalalalalala': 'thisisaverylongwordlalalalalalalalalalala',
            'a': 'a'
        }
        # Un diccionario donde las claves son las entradas
        # y los valores son las salidas esperadas.

        # Para palabras individuales, la primera letra debe ser minúscula
        # y no hay otras palabras para capitalizar.
        # osease la segunda y tercera y demas palabras deben estar capitalizadas
        # tener  el primer caracter en mayuscula

        for input_val, output_val in input_and_expected_outputs.items():
            # Itera sobre los pares clave-valor (entrada, salida esperada) del diccionario.
            # obtenemos  "entrada o la clave" con items  osease input_val
            # obtenemos  "salida o el valor"  con items  osease output_val

            self.assertEqual(output_val, camel.camel_case(input_val))
            # Afirma que el resultado de 'camel.camel_case' para la 'input_val'
            # es igual a la 'output_val' esperada.
            # Tras pasar la entrada o clave por la funcion  camel.camel_case del archivo camel

    def test_camel_case_uppercase(self):
        """
        test_camel_case_uppercase (test_camel.TestCamelCase.test_camel_case_uppercase)
        Qué comprueba: Que la función camel.camel_case() convierte correctamente la primera
        palabra a minúsculas y capitaliza el resto, incluso si la entrada original está
        completamente en mayúsculas o tiene capitalización mixta.

        Ejemplo de Entrada (input): sentence = "HeLLo wORlD"
        Ejemplo de Salida Esperada (expected output): "helloWorld"

        """
        # Prueba 'camel_case' con entradas que contienen palabras en mayúsculas.

        input_and_expected_outputs = {
            'HELLO': 'hello',
            'Hello': 'hello',
            'HeLLo wORlD': 'helloWorld'
        }
        # Diccionario de entradas y salidas esperadas.
        # lo mismo , items nos da la clave o entrada ,  y el valor o salida

        for input_val, output_val in input_and_expected_outputs.items():
            # se verifica que la entrada es igual que la salida
            # sino se lanza una excepcion
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_lowercase(self):
        """
        test_camel_case_lowercase (test_camel.TestCamelCase.test_camel_case_lowercase)
        Qué comprueba: Que la función camel.camel_case() convierte correctamente la primera
        palabra a minúsculas y capitaliza el resto, incluso si la entrada original ya está
        en minúsculas o tiene capitalización mixta.

        Ejemplo de Entrada (input): sentence = "heLLo WORlD"
        Ejemplo de Salida Esperada (expected output): "helloWorld"

        """
        # Prueba 'camel_case' con entradas que contienen palabras en minúsculas.

        input_and_expected_outputs = {
            'hello': 'hello',
            'hELLO': 'hello',
            'heLLo WORlD': 'helloWorld'
        }
        # Diccionario de entradas y salidas esperadas.

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_empty_strings(self):
        """

        """
        # Prueba 'camel_case' con cadenas vacías o solo espacios.

        input_and_expected_outputs = {
            '': '',
            ' ': '',
        }
        # Diccionario de entradas y salidas esperadas (ambas deberían resultar en una cadena vacía).

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_many_words(self):
        """
        test_camel_case_many_words (test_camel.TestCamelCase.test_camel_case_many_words)
        Qué comprueba: Que la función camel.camel_case() maneja correctamente frases con
        múltiples palabras, aplicando las reglas de camel case: primera palabra en
        minúsculas, las siguientes palabras con la primera letra en mayúscula y el resto
        en minúsculas, y todas unidas sin espacios.

        Ejemplo de Entrada (input): sentence = "this is a sentence"
        Ejemplo de Salida Esperada (expected output): "thisIsASentence"
        """
        # Prueba 'camel_case' con frases de múltiples palabras.

        input_and_expected_outputs = {
            'two words': 'twoWords',
            'this is a sentence': 'thisIsASentence',
            'Here is a long sentence with many words' : 'hereIsALongSentenceWithManyWords',
        }
        # Diccionario de entradas y salidas esperadas para frases más largas.

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_extra_spaces(self):
        """
        test_camel_case_extra_spaces (test_camel.TestCamelCase.test_camel_case_extra_spaces)
        Qué comprueba: Que la función camel.camel_case() maneja y normaliza múltiples
        espacios, espacios al principio/final, tabulaciones (\t) y saltos de línea (\n),
         convirtiéndolos a un solo espacio entre palabras y eliminando los espacios
          circundantes antes de aplicar el camel case.

        Ejemplo de Entrada (input): sentence = " Spaces Every where "
        Ejemplo de Salida Esperada (expected output): "spacesEveryWhere"
        Ejemplo de Entrada (input): sentence = "\tThere is a \t tab here"
        Ejemplo de Salida Esperada (expected output): "thereIsATabHere"
        """
        # Prueba 'camel_case' con entradas que tienen espacios extra o caracteres de espacio
        # como tabulaciones y saltos de línea.

        input_and_expected_outputs = {
            ' Spaces Before': 'spacesBefore',
            'Spaces after ': 'spacesAfter',
            ' Spaces Every where ': 'spacesEveryWhere',
            '\tThere is a \t tab here': 'thereIsATabHere', # Prueba con tabulaciones
            '\nThere is a \n newline here': 'thereIsANewlineHere', # Prueba con saltos de línea
            'There is a newline here\n': 'thereIsANewlineHere', # Salto de línea al final
            '\nThere is a newline here\n': 'thereIsANewlineHere', # Saltos de línea al principio y al final
        }
        # Diccionario de entradas y salidas esperadas. El 're.sub' y '.strip()'
        # en la función 'camel_case' deberían manejar esto.

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_emojis(self):
        """
        test_camel_case_emojis (test_camel.TestCamelCase.test_camel_case_emojis)
        Qué comprueba: Que la función camel.camel_case() procesa correctamente frases que
        incluyen caracteres emoji, tratándolos como parte de la "palabra" y no introduciendo
         errores ni modificándolos. Los espacios alrededor de los emojis deben eliminarse
          o normalizarse.

        Ejemplo de Entrada (input): sentence = "👽 🌎🌺🐑🌳 🌵🐬"
        Ejemplo de Salida Esperada (expected output): "👽🌎🌺🐑🌳🌵🐬"

        """
        # Prueba 'camel_case' con entradas que contienen emojis.

        input_and_expected_outputs = {
            '👽🌎🌺': '👽🌎🌺', # Emojis sin espacios
            '👽 🌎🌺🐑🌳 🌵🐬': '👽🌎🌺🐑🌳🌵🐬', # Emojis con espacios
        }
        # Diccionario de entradas y salidas esperadas. Se espera que los emojis
        # se traten como caracteres de palabra y no se modifiquen de forma inesperada.

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_camel_case_international(self):
        """
        test_camel_case_international (test_camel.TestCamelCase.test_camel_case_international)
        Qué comprueba: Que la función camel.camel_case() funciona correctamente con
        caracteres internacionales, acentos y caracteres no latinos (como los chinos o
        alemanes con umlaut), capitalizándolos o convirtiéndolos a minúsculas según las
        reglas del camel case.

        Ejemplo de Entrada (input): sentence = "Write a résumé"
        Ejemplo de Salida Esperada (expected output): "writeARésumé"
        Ejemplo de Entrada (input): sentence = "你叫 什么 名字"
        Ejemplo de Salida Esperada (expected output): "你叫什么名字"
        """
        # Prueba 'camel_case' con entradas que contienen caracteres internacionales/acentos.

        input_and_expected_outputs = {
            '你叫 什么 名字': '你叫什么名字', # Chino
            'Write a résumé': 'writeARésumé', # Francés (con acento)
            'Über die Brücke': 'überDieBrücke', # Alemán (con umlaut)
            'Fahre über die Brücke': 'fahreÜberDieBrücke', # Alemán (con umlaut)
        }
        # Diccionario de entradas y salidas esperadas. Se espera que la función maneje
        # correctamente estos caracteres.

        for input_val, output_val in input_and_expected_outputs.items():
            self.assertEqual(output_val, camel.camel_case(input_val))

    def test_input_and_output(self):
        """
        test_input_and_output (test_camel.TestCamelCase.test_input_and_output)
        Qué comprueba: Que la función main() (que interactúa con el usuario) lee
        correctamente una entrada simulada y llama a print() con la salida camel case
        correcta. Esto utiliza "mocking" para evitar la interacción real con la consola
        durante la prueba.

        Ejemplo de Entrada Simulada (input): input('Introduzca la frase: ') (internamente
         simulado por patch para devolver "This IS another SENTenCE")
        Ejemplo de Salida Esperada (expected output): Que print() sea llamado con
        "thisIsAnotherSentence"
        """
        # Este es un test especial para probar la función 'main()' del módulo 'camel',
        # que interactúa con la entrada y salida del usuario. Para ello, utiliza 'patch'.

        # Patch the input. Using with context manager automatically takes care of unpatching.
        with patch('builtins.input', return_value='This IS another SENTenCE'):
            # Usa 'patch' para reemplazar temporalmente la función 'input' (que está en 'builtins').
            # 'return_value='...'' hace que cada vez que se llame a 'input()' durante esta prueba,
            # en lugar de esperar la entrada real del usuario, devuelva la cadena 'This IS another SENTenCE'.
            # El uso de 'with' asegura que 'input' se restaure a su estado original después del bloque.
            """
            Me refiero a que el uso de with en el contexto de patch garantiza que, una vez que el
             código dentro del bloque with (y cualquier bloque anidado with) ha terminado de ejecutarse 
             (ya sea normalmente o por una excepción), la función input (o la función/objeto que estés 
             parcheando) vuelve a ser la función original de Python que era antes de que se aplicara el patch.
             VER ABAJO DEL TODO EXPLICACION
            """


            # And, patch the output
            with patch('builtins.print') as mock_print:
                # Usa 'patch' para reemplazar temporalmente la función 'print' (también en 'builtins').
                # 'as mock_print' asigna el objeto simulado (mock) de 'print' a la variable 'mock_print'.
                # Esto permite inspeccionar cómo fue llamada 'print' durante la ejecución.

                camel.main()
                # Llama a la función 'main()' del módulo 'camel'.
                # Dentro de 'main', se llamará a 'input()' (que devolverá el valor parcheado)
                # y luego a 'print()' (que será el mock_print).

                mock_print.assert_called_with('thisIsAnotherSentence')
                # Esta es una aserción específica para mocks.
                # Verifica que la función 'print' (que ahora es 'mock_print')
                # fue llamada EXACTAMENTE una vez y con el argumento 'thisIsAnotherSentence'.
                # Esto confirma que la lógica de 'main' procesó correctamente la entrada simulada
                # y produjo la salida esperada.

if __name__ == '__main__':
    # Este bloque se ejecuta solo cuando el script 'test_camel.py' se ejecuta directamente.

    unittest.main()
    # Descubre y ejecuta todas las pruebas definidas en esta clase 'TestCamelCase'.


"""
(.venv) python -m unittest test_camel
...........
----------------------------------------------------------------------
Ran 11 tests in 0.004s

OK
(.venv) python -m unittest test_camel.py
...........
----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
(.venv) python -m unittest -v test_camel.py
test_camel_case_emojis (test_camel.TestCamelCase.test_camel_case_emojis) ... ok
test_camel_case_empty_strings (test_camel.TestCamelCase.test_camel_case_empty_strings) ... ok
test_camel_case_extra_spaces (test_camel.TestCamelCase.test_camel_case_extra_spaces) ... ok
test_camel_case_international (test_camel.TestCamelCase.test_camel_case_international) ... ok
test_camel_case_lowercase (test_camel.TestCamelCase.test_camel_case_lowercase) ... ok
test_camel_case_many_words (test_camel.TestCamelCase.test_camel_case_many_words) ... ok
test_camel_case_single_words (test_camel.TestCamelCase.test_camel_case_single_words) ... ok
test_camel_case_uppercase (test_camel.TestCamelCase.test_camel_case_uppercase) ... ok
test_capitalize (test_camel.TestCamelCase.test_capitalize) ... ok
test_input_and_output (test_camel.TestCamelCase.test_input_and_output) ... ok
test_lower (test_camel.TestCamelCase.test_lower) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.002s

OK
(.venv) 


"""







"""
EXPLICACION DE ESTADO ORIGINAL cuando se usa patch 
import builtins
import unittest
from unittest.mock import patch

# Guardar la función input original
original_input = builtins.input

# Parchear manualmente
builtins.input = lambda prompt: "Valor simulado" 
# Esto es una simulación MUY simplificada de lo que hace patch

# Ejecutar el código que usa input
# ...

# Problema: ¡Si olvidamos restaurarla o si ocurre un error, input sigue parcheada!
builtins.input = original_input # Necesario para restaurar



Si olvidas builtins.input = original_input o si ocurre una excepción antes de esa línea, la función input de todo tu programa Python (y de cualquier otra prueba que se ejecute después) seguirá siendo tu versión parcheada. Esto puede llevar a errores muy difíciles de depurar en otras partes de tu suite de pruebas o en tu aplicación.

Con with patch (seguro y limpio)
El patch como gestor de contexto (with patch(...)) se encarga automáticamente de esto:



from unittest.mock import patch
import builtins # No necesitas importarlo si solo vas a parchear sus atributos

def mi_funcion_que_usa_input():
    nombre = input("Dime tu nombre: ")
    print(f"Hola, {nombre}")

# Test
def test_mi_funcion():
    with patch('builtins.input', return_value='Juan'):
        # Aquí, builtins.input es temporalmente 'Juan'
        mi_funcion_que_usa_input() # Cuando llama a input(), recibe 'Juan'
    # Fuera del bloque 'with', builtins.input YA FUE RESTAURADO a su función original.

    # Cualquier código o prueba que se ejecute aquí usará el input REAL
    # Por ejemplo:
    # otro_nombre = input("Dime otro nombre: ") # Pediría al usuario real
A qué me refiero con "estado original":

Antes de entrar al bloque with patch: 
builtins.input es la función de entrada interactiva estándar de Python.

Dentro del bloque with patch: 
builtins.input es temporalmente reemplazada por un objeto Mock que devuelve el return_value 
configurado ('Juan' en el ejemplo).

Después de salir del bloque with patch: 
El patch deshace automáticamente el cambio. 

builtins.input vuelve a ser la función de entrada interactiva estándar de Python.

Este comportamiento de "limpieza automática" es una de las razones principales por 
las que los gestores de contexto (with declaraciones) son tan valiosos,
 especialmente en pruebas unitarias con patch. 
 Garantizan que los cambios temporales no afecten otras pruebas o el estado global de tu 
 programa.

"""



""" SI INTENTAMOS  HACERLO CON lambda


lambda prompt: "Valor simulado"





si usaras esto , seria hacer lo mismo




Sí, en esencia, lambda prompt: "Valor simulado" sería hacer lo mismo en el sentido de que también está creando una función anónima que devuelve un valor fijo cuando se llama.

Sin embargo, hay una diferencia crucial en cómo y cuándo lo usarías y en la capacidad de la simulación:

Contexto de unittest.mock.patch:
Cuando usas unittest.mock.patch, tú no le pasas una función lambda directamente para que la use como reemplazo. En su lugar, le pasas el atributo return_value. La magia de patch es que crea su propio objeto Mock internamente, y ese Mock es el que se comporta como una función (o cualquier otro objeto) y devuelve return_value cuando se le llama.

Con patch:

Python

from unittest.mock import patch
with patch('builtins.input', return_value='Valor simulado'):
    # Aquí, 'builtins.input' es ahora un objeto Mock,
    # y cuando se le llama, devolverá 'Valor simulado'.
    # No estamos asignando directamente una lambda.
    pass
Parcheo manual (como en el ejemplo anterior original_input = builtins.input):
Si estuvieras parcheando manualmente sin unittest.mock.patch (lo cual no es recomendable para pruebas serias por los problemas de limpieza que mencionamos), entonces sí, podrías asignar una función lambda directamente:

Python

import builtins

# Guardamos la función original para restaurarla después
original_input = builtins.input

# Parcheamos manualmente con una lambda
builtins.input = lambda prompt: "Valor simulado"
print(input("Dame algo: ")) # Esto imprimirá "Valor simulado"

# Restauramos la función original (¡MUY IMPORTANTE!)
builtins.input = original_input
print(input("Dame algo de nuevo: ")) # Esto ahora sí pedirá al usuario
Diferencias y Ventajas de unittest.mock.patch sobre una simple lambda manual:

Restauración Automática: patch con with se encarga automáticamente de restaurar el objeto original, evitando efectos secundarios no deseados en otras pruebas. Una lambda manual no hace esto.

Capacidades de Mock: El objeto Mock que patch crea es mucho más potente que una simple lambda:

Puede verificar si fue llamado (mock_object.called).

Puede verificar con qué argumentos fue llamado (mock_object.assert_called_with(...)).

Puede simular efectos secundarios (lanzar excepciones, devolver diferentes valores en llamadas sucesivas).

Puede simular atributos y métodos de un objeto.
Una simple lambda solo hace una cosa: devuelve un valor.

Claridad y Estándar: Usar unittest.mock.patch es la forma estándar y recomendada en Python para realizar este tipo de simulaciones en pruebas, lo que hace el código más legible y mantenible para otros desarrolladores familiarizados con unittest.

Entonces, mientras la lambda podría lograr el mismo efecto de devolver un valor fijo, patch es la herramienta superior y más segura para la simulación en pruebas, ya que no solo se encarga del valor de retorno, sino también del ciclo de vida del parcheo y de proporcionar poderosas herramientas de aserción.

"""