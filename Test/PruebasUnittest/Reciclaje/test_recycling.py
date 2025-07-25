import unittest
# Importa el módulo 'unittest' para la creación de pruebas.

from unittest.mock import Mock, patch
# Importa 'Mock' (para crear objetos simulados)
# y 'patch' (para reemplazar objetos temporalmente)
# del módulo 'unittest.mock'.

"""
patch internamente cree un objeto Mock para ti, generalmente se sigue importando Mock 
explícitamente junto con patch (from unittest.mock import Mock, patch).
"""




import recycling
# Importa el módulo 'recycling' que contiene las funciones a probar.

class TestRecycling(unittest.TestCase):
    # Define una clase de prueba llamada 'TestRecycling' que hereda de 'unittest.TestCase'.
    # Esto la convierte en una suite de pruebas reconocida por unittest.

    def test_max_values(self):
        # Método de prueba para la función 'max_recycling'.

        # More than one house with the same max value
        # serian 8 casas
        # donde 6 es el numero de cajas  maximo  en el primer ejemplo
        # la 5 y la 7 (índices) tienen 6 cajas en el primer ejemplo
        example_data = [1, 3, 5, 0, 2, 6, 3, 6]
        # Define una lista de datos de ejemplo donde hay más de una casa con el valor máximo.

        max_data = recycling.max_recycling(example_data)
        # Llama a la función 'max_recycling' con los datos de ejemplo y guarda el resultado.

        self.assertEqual(max_data.crates, 6)
        # Afirma que el número máximo de cajas encontrado es 6.

        self.assertEqual(max_data.houses, [5, 7])
        # Afirma que las casas con ese máximo son la 5 y la 7 (índices).

        # Single max value
        # serian 8 casas
        # donde 9 es el numero de cajas  maximo  en el segundo ejemplo
        # la 2  (índices) tienen 9 cajas en el segundo ejemplo
        example_data = [1, 3, 9, 0, 2, 3, 3, 6]
        # Define otro conjunto de datos de ejemplo, esta vez con un único valor máximo.

        max_data = recycling.max_recycling(example_data)
        # Llama a la función de nuevo con los nuevos datos.

        self.assertEqual(max_data.crates, 9)
        # Afirma que el número máximo de cajas es 9.

        self.assertEqual(max_data.houses, [2])
        # Afirma que la casa con ese máximo es la 2 (índice).

    def test_min_values(self):
        # Método de prueba para la función 'min_recycling'.

        # More than one joint min value
        example_data = [1, 0, 3, 5, 0, 2, 6]
        # Define datos de ejemplo con múltiples casas con el mismo valor mínimo.

        min_data = recycling.min_recycling(example_data)
        # Llama a la función 'min_recycling' con los datos de ejemplo.

        self.assertEqual(min_data.crates, 0)
        # Afirma que el número mínimo de cajas es 0.

        self.assertEqual(min_data.houses, [1, 4])
        # Afirma que las casas con ese mínimo son la 1 y la 4.

        # Single min value
        example_data = [1, 3, 5, 0, 2, 6]
        # Define otro conjunto de datos, esta vez con un único valor mínimo.

        min_data = recycling.min_recycling(example_data)
        # Llama a la función de nuevo.

        self.assertEqual(min_data.crates, 0)
        # Afirma que el número mínimo de cajas es 0.

        self.assertEqual(min_data.houses, [3])
        # Afirma que la casa con ese mínimo es la 3.

    def test_total(self):
        # Método de prueba para la función 'total_crates'.

        example_data = [1, 3, 5, 0, 2, 6]
        # Define datos de ejemplo.

        self.assertEqual(recycling.total_crates(example_data), 17)
        # Afirma que la suma total de cajas es 17.

    def test_get_crate_quantities(self):
        # Método de prueba para la función 'get_crate_quantities', que interactúa con el usuario.
        """
        Create a patch to replace the built in input function with a mock.
        The mock is called mock_input, and we can change the way it behaves, e.g. provide
        our desired return values. So when the code calls input(), instead of
        calling the built-in input function, it will call the mock_input mock function,
        which doesn't do anything except for returning the values provided in the
        list of side_effect values - the first time it is called, it returns the first
        side_effect value (1), second time it will return the second value, (3) etc...
        """
        # Docstring: Explica cómo funciona el parcheo de 'input' con 'side_effect'.
        # 'side_effect' es una característica del mock que permite especificar una secuencia
        # de valores a devolver en llamadas sucesivas.

        example_data = [1, 3, 5, 0, 2, 6]
        # Define los valores que el 'input' simulado debe devolver en cada llamada.

        #ACLARACION
        #Estás llamando a recycling.get_crate_quantities con el argumento houses=6.
        # Dentro de get_crate_quantities, el bucle for house in range(houses):
        # se ejecutará 6 veces (para house = 0, 1, 2, 3, 4, 5).
        # Como input() ha sido parcheado con side_effect=example_data
        # (donde example_data tiene 6 elementos: [1, 3, 5, 0, 2, 6]),
        # el mock_input devuelve un elemento diferente de example_data en cada una de esas 6
        # llamadas, hasta que get_crate_quantities ha terminado su bucle
        # y el mock_input ha devuelto todos los valores de example_data.
        """El objeto Mock se crea en el momento en que se ejecuta la sentencia with patch(...).
        Cuando Python llega a esta línea, patch es llamado como un gestor de contexto.
        Internamente, patch realiza la siguiente secuencia de eventos:

Crea un objeto Mock: Instancia un nuevo objeto unittest.mock.Mock.
Configura el Mock: Le asigna el side_effect (o return_value, etc.) que le has proporcionado.
Reemplaza el objeto real: 
Toma el objeto original (builtins.input en este caso)  y lo reemplaza con el Mock recién creado.

Asigna el Mock a la variable: 
El objeto Mock que se creó y reemplazó al input original es el mismo objeto que se asigna 
a la variable mock_input.
Así que, el mock_input es un objeto Mock que se genera y se activa justo al principio del 
bloque with. 
Cuando el bloque with termina (ya sea que el código se complete normalmente o se lance una 
excepción), patch se encarga de restaurar builtins.input a su estado original, 
"limpiando" el entorno de prueba.
        """
        with patch('builtins.input', side_effect=example_data) as mock_input:
            # Parchea la función 'input' (que se encuentra en el módulo 'builtins').
            # 'side_effect=example_data' hace que 'input' devuelva secuencialmente 1, luego 3, luego 5, etc.
            # ACLARACION de que get_crate_quantities se llama 6 veces en el bucle for porque
            #  example_data = [1, 3, 5, 0, 2, 6] son 6 elementos
            # 'as mock_input' asigna el objeto Mock a la variable 'mock_input'.

            # POR LO TANTO AQUI PEDIMOS DATOS PARA 6 CASAS
            """
            Cuando patch asigna el objeto Mock a mock_input, mock_input es un objeto que 
            registra todas las interacciones que ocurren con él. No puedes "imprimir" su 
            estado interno de la misma manera que imprimirías una lista o un diccionario 
            para ver sus valores literales de una sola vez, porque su valor es su comportamiento 
            y los registros de sus llamadas.

            Sin embargo, puedes inspeccionarlo de varias maneras para ver cómo se comportó y qué hay dentro:
            """
            print(
                f"\n--- Antes de llamar a la función ---\n{mock_input}")  # Esto imprimirá el mock antes de ser llamado
            self.assertEqual(recycling.get_crate_quantities(6), example_data)
            print(
                f"\n--- Después de llamar a la función ---\n{mock_input}")  # Esto imprimirá el mock después de ser llamado
            # Llama a 'get_crate_quantities' pidiéndole datos para 6 casas.
            # Debido al parcheo, 'get_crate_quantities' "recibirá" los valores de 'example_data'.
            # Se afirma que la lista devuelta es idéntica a 'example_data'.

    def test_int_input(self):
        # Método de prueba para la función 'positive_int_input', que valida la entrada de usuario.

        # Test with some invalid input
        # Put a valid input at the end or the function will never return
        with patch('builtins.input', side_effect=['-2', '-1000', 'abc', '123abc', '3']) as mock_input:
            # Parchea 'input' con una secuencia de entradas inválidas, y una válida al final.
            # La función 'positive_int_input' seguirá pidiendo entrada hasta que obtenga '3'.

            self.assertEqual(recycling.positive_int_input('example question'), 3)
            # Afirma que la función finalmente devuelve el valor válido '3'.

        #Ultimately, should return the valid value at the end of the list.
        with patch('builtins.input', side_effect=[ '0', '13', '1', '100000000']) as mock_input:
            # Otro parcheo, esta vez con múltiples entradas válidas.

            self.assertEqual(recycling.positive_int_input('example question'), 0)
            # Verifica la primera entrada válida.

            self.assertEqual(recycling.positive_int_input('example question'), 13)
            # Verifica la segunda entrada válida.

            self.assertEqual(recycling.positive_int_input('example question'), 1)
            # Y así sucesivamente...

            self.assertEqual(recycling.positive_int_input('example question'), 100000000)

    def test_main(self):
        # Método de prueba para la función 'main', que coordina todo el programa.
        # Esto es un test de integración a nivel de programa.

        with patch('builtins.input', side_effect=['4', '1', '3', '2', '3']) as mock_input:
            # Parchea 'input' para simular todas las entradas que 'main' pedirá:
            # - '4': para 'How many houses?'
            # - '1', '3', '2', '3': para las crates de cada una de las 4 casas.

            recycling.input = mock_input
            # En algunos casos, si la función 'main' de 'recycling' usa 'input'
            # de una manera que no se puede parchear directamente a través de 'builtins',
            # se puede parchear la referencia local en el módulo.
            # Sin embargo, para builtins.input, el parche en builtins suele ser suficiente.
            # Esta línea puede ser redundante o necesaria dependiendo de cómo 'input' sea referenciada internamente.

            recycling.main() # verify program doesn't crash :) Could also test that it's
            # Llama a la función 'main' del módulo 'recycling'.
            # El comentario indica que el objetivo principal aquí es verificar que el programa
            # no se bloquee.

            # printing correct data with a mock print function.
            # El comentario sugiere que una mejora sería también parchear 'builtins.print'
            # para verificar que las salidas finales impresas por 'main' son correctas.
            # Actualmente, esta prueba solo asegura que 'main' se ejecuta sin errores con la entrada simulada.

if __name__ == '__main__':
    # Este bloque se ejecuta si el archivo de prueba se ejecuta directamente.

    unittest.main()
    # Ejecuta todas las pruebas en la clase 'TestRecycling'.