
"""
También podemos probar más de una cosa a la vez al
tener múltiples afirmaciones dentro del mismo
método de Python:
"""


# Hereda de 'object', que es la clase base para todas las clases en Python 3
# (aunque en Python 3 ya no es estrictamente necesario ponerlo, es una buena práctica).
class Test(object):

    # es el método constructor de la clase.
    # Se llama automáticamente cada vez que creas una nueva instancia de 'Test'.
    # 'self' se refiere a la instancia actual de la clase.
    # 'first_name' y 'last_name' son los argumentos que debes pasar al crear un objeto 'Test'.
    def __init__(self, first_name,last_name ):
        self.first_name = first_name
        self.last_name = last_name

    #  método dentro de la clase 'Test'
    # Este método está diseñado para probar los atributos 'first_name' y 'last_name'.
    # 'self' es necesario para acceder a los atributos de la instancia (como self.first_name).
    def test_all_class_arguments(self):
        print('Testing both of the class variables to see whether they are both strings!')


        # Crea una lista temporal con los valores de 'self.first_name' y 'self.last_name'.
        # la lista se crea porque tiene [] entre los dos argumentos
        # El bucle iterará sobre cada elemento de esta lista.
        # '_' es una convención en Python para una variable cuyo valor no se usará directamente
        # dentro del cuerpo del bucle, solo nos interesa iterar sobre los elementos.
        for _ in [self.first_name,self.last_name]:
            print(f"{str(_)} {type(_)}")
            assert(type(_) is str)#  si es falsa la condicion crea una excepcion
            # la afirmación (assertion) clave.
            # assert Comprueba si la condición dentro de los paréntesis es Verdadera (True).
            # 'type(_)' obtiene el tipo del elemento actual en la iteración (ya sea first_name o last_name).
            # 'is str' comprueba si ese tipo es exactamente 'str' (una cadena de texto).
            # Si la condición es Falsa (False), 'assert' levantará un error 'AssertionError'
            # y el programa se detendrá.
            # Si es True, el programa continúa. osease no se lanza una excepcion

        print('------')
        print('Pasados todos los test')

yay = Test('James' , 'Phoenix') # Success Example
# 'yay = Test('James', 'Phoenix')' crea una nueva instancia (objeto) de la clase 'Test'.
# 'James' se pasa como 'first_name' y 'Phoenix' como 'last_name' al constructor '__init__'.
# La variable 'yay' ahora contiene este nuevo objeto.


yay.test_all_class_arguments()
# 'yay.test_all_class_arguments()' llama al método 'test_all_class_arguments'
# en la instancia 'yay'. Esto ejecuta las pruebas definidas en ese método.

"""
(.venv) python PruebaaVariosComandos.py
Testing both of the class variables to see whether they are both strings!
James <class 'str'>
Phoenix <class 'str'>
------
Pasados todos los test

"""


# error
# Si hubiéramos hecho:
nay = Test(123, 'Phoenix')#
try:
    nay.test_all_class_arguments()
except AssertionError:
        print("la aserción para '123' (que es un int, no un str) fallaría y se lanzaría un AssertionError.")


"""
Testing both of the class variables to see whether they are both strings!
123 <class 'int'>
la aserción para '123' (que es un int, no un str) fallaría y se lanzaría un AssertionError.

"""


yay = Test(5 , 'Phoenix') # Fail Example
try:
    yay.test_all_class_arguments()
except AssertionError:
        print("la aserción para '5' (que es un int, no un str) fallaría y se lanzaría un AssertionError.")






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