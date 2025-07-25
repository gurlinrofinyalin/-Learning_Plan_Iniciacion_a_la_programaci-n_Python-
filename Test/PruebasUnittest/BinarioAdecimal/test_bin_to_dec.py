import unittest
import bin_to_dec # importamos el archivo a probar

import unittest # Importamos el módulo unittest, fundamental para crear pruebas unitarias.

class TestBinaryToDecimal(unittest.TestCase):
    # Esta clase hereda de unittest.TestCase, lo cual le otorga todas las funcionalidades
    # necesarias para escribir y ejecutar pruebas unitarias.

    # Este es el primer método de prueba. Los métodos de prueba en unittest
    # deben comenzar con 'test_' para que el ejecutor de pruebas los descubra automáticamente.
    # Aquí probamos la función de conversión de binario a decimal con entradas válidas.
    def test_binario_decimal_con_entradas_validas(self):

        # El método bin de Python hace la conversión de binario a decimal
        # Los bucles son útiles: testeamos un rango de números
        # Iteramos a través de números decimales del 0 al 99.
        for d in range(100):

            binary = bin(d)  # En formato '0b10101' , siendo d de 0 a 99
            # Convertimos el número decimal 'd' a su representación binaria
            #                                         En formato '0b10101'
            # usando la función incorporada 'bin()'.
            #                          El resultado incluirá un prefijo '0b'.
            # Ejemplo: bin(5) devuelve '0b101'.

            binary = binary[2:]  # Quitar la inicial '0b'
            # Eliminamos el prefijo '0b' del string binario, ya que nuestra función
            # 'bin_to_dec.decimal' probablemente espera solo '0's y '1's.

            dec_output = bin_to_dec.decimal(binary) # funcion que espera 0 y/o 1
            # Llamamos a la función 'decimal' (que suponemos está en un módulo  o
            # archivo que hemos importado 'bin_to_dec')
            # para convertir la cadena binaria a su valor decimal.

            self.assertEqual(d, dec_output)
            # Esta es una aserción. Verifica si el valor decimal original 'd' es igual
            # al resultado 'dec_output' de nuestra función.
            # Si no son iguales, la prueba falla.

        # Testeamos algunos números más grandes
        test_vals = [4000, 4001, 4002, 1024, 1099511627776, 1099511627777, 1099511627775]
        # Definimos una lista de números decimales más grandes para probar.

        for d in test_vals:
            # Iteramos sobre esta lista de valores de prueba.
            binary = bin(d)  # En formato '0b10101'
            # Convertimos cada número grande a su representación binaria.

            binary = binary[2:]  # Quitar la inicial '0b'
            # Eliminamos el prefijo '0b'.

            dec_output = bin_to_dec.decimal(binary)
            # Convertimos la cadena binaria de vuelta a decimal usando nuestra función.

            self.assertEqual(d, dec_output)
            # Afirmamos que el valor original y el valor convertido son iguales.


        # Test con strings
        test_bin_str = ['101010', '1111', '000111', '0', '1']
        # Definimos una lista de cadenas binarias de prueba.

        expected_dec = [42, 15, 7, 0, 1]
        # Definimos una lista de los valores decimales esperados correspondientes.

        for binary_input, expected_dec_output in zip(test_bin_str, expected_dec):
            # el resultado de zip son dos listas
            print(3*"-")
            print(f"CADENA BINARIA binary_input {binary_input} de tipo {type(binary_input)}")
            print(3 * "-")
            print(f"CADENA DECIMAL expected_dec_output {expected_dec_output} de tipo {type(expected_dec_output)}")
            print(3 * "-")
            # Iteramos sobre ambas listas simultáneamente usando 'zip'.

            dec = bin_to_dec.decimal(binary_input)
            # Convertimos "cada cadena binaria" de la lista a decimal.

            self.assertEqual(dec, expected_dec_output)
            # Afirmamos que el resultado de nuestra función es igual al valor esperado.


    # Este es el segundo método de prueba, dedicado a probar el manejo de errores
    # de la función cuando "se le dan entradas no válidas".
    def test_binario_decimal_con_entradas_invalidas(self):


        # Testeamos que se genere un error con cadenas que no estén compuestas por 0 y 1.
        # estas cadenas son validas
        valid = '010101' # Esta variable no se usa en el test real, es solo un comentario.
        valid2 = '1111111' # Esta variable tampoco se usa.

        invalid = ['123456', '101010012', 'abc', '@#$%$%^%^&']
        # Definimos una lista de cadenas que no son representaciones binarias válidas.
        # porque tienene valores distitos de 0 o/y 1

        for invalid_input in invalid: # Iteramos sobre cada entrada inválida.

            with self.assertRaises(ValueError):
                # Este es un gestor de contexto especial de unittest.
                # Asegura que el código dentro de este bloque (la siguiente línea)
                # DEBE generar un 'ValueError'. Si no lo hace, o si genera otro error,
                # la prueba falla. Esto es ideal para probar el manejo de excepciones.

                bin_to_dec.decimal(invalid_input)
                # Intentamos convertir la entrada inválida. de binario a decimal
                # Se espera que esta línea lance un ValueError si la función
                # 'bin_to_dec.decimal' está implementada correctamente
                # para manejar entradas no binarias.



if __name__ == '__main__':
    # Esta es una construcción estándar en Python.
    # Significa: "Si este script se está ejecutando directamente (no importado como un módulo)".

    unittest.main()
    # Si el script se ejecuta directamente, 'unittest.main()' se llama.
    # Esta función descubre automáticamente todos los métodos de prueba (los que comienzan con 'test_')
    # en las clases que heredan de unittest.TestCase en este archivo, y los ejecuta.
    # También proporciona un informe de los resultados de las pruebas.


"""
__name__ es __main__
si se ejecuta:
en terminal:  python test_bin_to_dec.py
si ejecutas en pycharm en el play   

__name__ NO ES __main__
si importas el archivo test_bin_to_dec.py como modulo a otro archivo

"""


"""


Entendiendo if __name__ == '__main__':
Esta es una construcción común en Python que verifica si el script actual se está 
ejecutando directamente.

__name__: Esta es una variable especial incorporada en Python. 
Su valor depende de cómo se esté ejecutando el script:

Si un script de Python se ejecuta directamente 
(por ejemplo, python tu_script.py), 
la variable __name__ para ese script se establece en la cadena '__main__'.

Si un script de Python se importa como un módulo en otro script, 
la variable __name__ para el script importado se establece con el nombre real del 
módulo del script (por ejemplo, 'test_bin_to_dec' en tu caso).

Botón "Play" de PyCharm vs. Línea de Comandos
Cuando ejecutas con el botón "Play" de PyCharm:
Cuando haces clic en el botón "Play" en PyCharm, este, en efecto, 
ejecuta el script como el punto de entrada principal. 
PyCharm está ejecutando tu archivo test_bin_to_dec.py directamente. 
En este escenario, la variable __name__ dentro de test_bin_to_dec.py 
se establecerá en '__main__'.


Por lo tanto, la condición if __name__ == '__main__': se evalúa como True, 
y unittest.main() se ejecuta. 
El mecanismo de ejecución interno de PyCharm está tratando a test_bin_to_dec.py 
como el script principal a ejecutar, convirtiéndolo en el "main".

Cuando ejecutas con python test_bin_to_dec.py en la consola:
De manera similar, cuando ejecutas python test_bin_to_dec.py en tu terminal, 
le estás diciendo explícitamente a Python que ejecute test_bin_to_dec.py 
como el script principal. 
Al igual que con el botón de PyCharm, __name__ dentro de test_bin_to_dec.py 
será '__main__'.

Así que, en ambos casos (el botón "Play" de PyCharm y la ejecución desde la consola 
con python tu_script.py), 
el bloque if __name__ == '__main__': se ejecuta porque __name__ es '__main__'.


IMPORTANTE 
El Papel de unittest.main()
unittest.main() está diseñado para descubrir y ejecutar pruebas cuando el propio 
archivo de prueba se ejecuta directamente. 


El bloque if __name__ == '__main__': es la forma estándar de asegurar que 
unittest.main() se llama solo cuando tienes la intención de ejecutar las pruebas, 
no cuando el archivo de prueba es importado como un módulo por otra parte de tu código.



"""


"""
El argumento -m le dice al intérprete de Python que ejecute un módulo como un script.

Cuando usas:
python -m unittest test_bin_to_dec.py

Lo que estás haciendo es:

python: Invocas el intérprete de Python.

-m unittest: 
Le indicas a Python que ejecute el módulo unittest como si fuera un script. 
Esto le permite a unittest tomar control del proceso de ejecución de pruebas.

test_bin_to_dec.py: 
Este es un argumento que se le pasa al módulo unittest, 
indicándole qué archivo de prueba debe ejecutar.

¿Por qué se usa -m unittest en lugar de simplemente python test_bin_to_dec.py?
Aunque python test_bin_to_dec.py 
(si unittest.main() está en el if __name__ == '__main__': bloque) 
funciona para ejecutar las pruebas, 
usar python -m unittest es a menudo preferible por varias razones:

Forma canónica de ejecutar pruebas: 
Es la forma recomendada y más robusta de ejecutar pruebas con unittest. 
Permite a unittest manejar la búsqueda de pruebas de manera más sofisticada
 (por ejemplo, descubrir pruebas en múltiples archivos o directorios).

Independencia del if __name__ == '__main__':: 
Aunque tu archivo de prueba lo tiene, si por alguna razón no lo tuviera o lo tuvieras 
configurado de otra manera, 
python -m unittest aún podría descubrir y ejecutar tus pruebas.

Funcionalidades adicionales: 
El módulo unittest tiene muchas más opciones y subcomandos cuando se ejecuta con -m 
(por ejemplo, -m unittest discover para descubrir automáticamente todas las pruebas 
en un directorio).


python -m unittest test_bin_to_dec.py
python -m unittest discover 



python -m unittest test_bin_to_dec.py: Este comando le indica al módulo unittest que 
ejecute específicamente 
las pruebas contenidas en el archivo test_bin_to_dec.py. Es útil cuando sabes exactamente
 qué archivo de prueba quieres ejecutar.

python -m unittest discover: Este comando es mucho más potente para proyectos con múltiples
archivos de prueba. Lo que hace es:

Buscar (descubrir) archivos de prueba: Por defecto, discover buscará archivos .py que comiencen
 con test_ (por ejemplo, test_something.py) en el directorio actual y en todos sus subdirectorios
  de forma recursiva.

Ejecutar todas las pruebas encontradas: Una vez que encuentra esos archivos, carga todas las 
clases de prueba (que heredan de unittest.TestCase) y ejecuta todos los métodos de prueba
 (que comienzan con test_) que contienen.


"""

