
"""
Métodos de afirmación de
Python 3.x UnitTest
A continuación, detallamos la lista de todos los
métodos de afirmación de UnitTest:
Método                      Implementación
assertEqual                 a == b
assertNotEqual              a != b
assertTrue                  bool(x) is True
assertFalse                 bool(x) is False
assertIs                    a is b
assertIsNot                 a is not b
assertIsNone                x is None
assertIsNotNone             x is not None
assertIn                    a in b
assertNotIn                 a not in b
assertIsInstance            is instance(a,b)
assertNotIsInstance         not is instance(a,b)
assertRaises                fun(*args,**kwds)
                            raises exc
assertRaisesRegexp          fun(*args,**kwds)
                            raises exc(regex)
assertAlmostEqual           round(a-b,7) == 0
assertNotAlmostEqual        round(a-b,7) != 0
assertGreater               a > b
assertGreaterEqual          a >= b
assertLess                  a < b
assertLessEqual             a <= b
assertRegexpMatches         r.search(s)
assertNotRegexpMatches      not r.search(s)
assertItemsEqual            sorted(a) ==
                            sorted(b)
assertDictContainsSubset    all the key/value
                            pairs in a exist in b
assertMultiLineEqual        strings
assertSequenceEqual         sequences
assertListEqual             lists
assertTupleEqual            tuples
assertSetEqual              sets or frozensets
assertDictEqual             dicts
"""
from setuptools.unicode_utils import try_encode

"""

Escribir declaraciones de
afirmación
Además de usar declaraciones de afirmación
simples, al importar el módulo de tipos de
Python podemos hacer declaraciones de afirmación
más abstractas en Tipos específicos:
"""

import types # Importamos el módulo 'types' para acceder a 'FunctionType' (TipoFunción)


class Test: # Definimos una clase llamada 'Test'
    def __init__(self, id_, first_name, last_name):
        # Este es el método constructor.
        #  Se llama al crear una nueva instancia de la clase.
        # 'self' se refiere a la propia instancia del objeto.
        # 'id_', 'first_name' y 'last_name' son los valores que pasamos al crear el objeto.

        self._id = id_
        # Asignamos 'id_' a un atributo de instancia llamado '_id'.
        # El prefijo de un solo guion bajo ('_') es una convención para indicar que
        # este atributo es 'protegido' o para uso interno de la clase.

        self.first_name = first_name
        # Asignamos 'first_name' a un atributo de instancia llamado 'first_name'.

        self.last_name = last_name
        # Asignamos 'last_name' a un atributo de instancia llamado 'last_name'.

    def subtract(self):
        # Este es un método de instancia
        answer = 5 + 5
        return answer # Devuelve el resultado de la operación.

    def test_lambda_function(self):
        # Este método prueba si una función lambda es del tipo correcto.
        print('Probando si una función anónima (lambda) es de tipo función (debería pasar)...')
        # Definimos una función lambda simple dentro de este método.
        # 'x' es el argumento de la función lambda.
        my_lambda = lambda x: x + 1 # x es el arg que va a recibir
        #        x + 1: Es la expresión que la función lambda ejecuta.
        # Para cada valor x que se le pase, esta función devolverá ese valor x sumado a 1.
        # devuelve x + 1
        """
        lambda: Esta palabra clave se usa para crear una función anónima. 
        "Anónima" significa que no tiene un nombre definido con la palabra clave def 
        (como lo haría una función normal).

        x: Es el argumento (o parámetro) que esta función lambda espera recibir. 
        Piensa en él como una variable que la función usará en su operación.

        : Separa los argumentos de la expresión que la función va a evaluar y devolver.

        x + 1: Es la expresión que la función lambda ejecuta. 
        Para cada valor x que se le pase, esta función devolverá ese valor sumado a 1.

        my_lambda =: Asigna esta función anónima a la variable my_lambda.
         Aunque la función es "anónima" al crearse, al asignarla a una variable, 
         podemos referirnos a ella y usarla como si fuera una función normal.
        """


        # aqui preguntamos si una funcion lambda es una funcion
        # Esta aserción verifica si 'my_lambda' es una instancia de 'types.FunctionType'.
        # Una función lambda es, de hecho, un tipo de función, por lo que esta aserción PASARÁ.
        assert isinstance(my_lambda, types.FunctionType), "Error: La lambda no es de tipo función."
        print('La prueba de la lambda pasó: La lambda es efectivamente una función.')

    #aqui le vamos a preguntar si no es una funcion , como es un metodo  llamado subtract
    # de esta misma clase Test, si que es una funcion , pero como preguntamos negativamente
    def test_subtract_function(self):
        # Este método está diseñado para FALLAR y demostrar un AssertionError.
        print('Probando si el método "subtract" NO es de tipo función (debería fallar intencionalmente)...')

        # Esta aserción está diseñada para fallar.
        # 'self.subtract' es una referencia al método 'subtract' de esta instancia.
        # En Python, los métodos definidos con 'def' son de tipo 'types.FunctionType'.
        # Entonces, 'isinstance(self.subtract, types.FunctionType)' evalúa a TRUE.
        # Al añadir 'not' delante, 'not True' se convierte en FALSE.
        # Por lo tanto, 'assert False' provocará un AssertionError, deteniendo el programa.
        assert not isinstance(self.subtract, types.FunctionType), "¡Error: Esta aserción debería fallar!"
        print('La prueba del método subtract pasó (inesperado si fue diseñada para fallar).')
        # Esta línea de impresión NUNCA se alcanzará si la aserción anterior falla.

# --- Creando una instancia de la clase y probando sus métodos ---
# 'yay' es la variable que contendrá la instancia de nuestra clase 'Test'.
# '123' se pasa como 'id_', 'James' como 'first_name' y 'Phoenix' como 'last_name'.
yay = Test("123", 'James', 'Phoenix')

# Imprimimos los atributos '_id', 'first_name' y 'last_name' del objeto para verificar
# que se asignaron correctamente.
print(f"ID: {yay._id}, Nombre: {yay.first_name} {yay.last_name}")

print("\n--- Ejecutando las pruebas ---")

# Ejecutamos el primer método de prueba. Este debería PASAR y mostrar un mensaje de éxito.
# Corresponde a la línea del resultado original "example_class.test_lambda_function() # Success Example"
yay.test_lambda_function()

print("------")

# Ejecutamos el segundo método de prueba. Este está diseñado para FALLAR
# y generar un 'AssertionError', tal como se indica en el resultado original.
# Corresponde a la línea del resultado original "example_class.test_subtract_function() # Fail Example"
print("\nPreparándose para ejecutar la prueba que debería fallar...")
try:
    yay.test_subtract_function()
except AssertionError:
        print("subtract si que es un objeto  funcion")

# Esta línea de impresión NUNCA se ejecutará si el 'AssertionError' ocurrió en la línea anterior.
print("\nTodas las pruebas pasaron exitosamente (si llegaste aquí, algo no falló como se esperaba).")