"""
Ya sabemos que nuestra función está bien realizada,
hace su trabajo, pero dependiendo de los valores que
le pasemos, puede dar problemas.

Hace cálculos que
no se deberían llevar a cabo e incluso da error
cuando le pasamos una cadena de texto.
Este es un test muy primitivo. Haciendo uso de
unittest podemos automatizar el proceso de prueba
de nuestro código.


Para usar unittest tenemos que seguir un protocolo,
vamos a tener que crear otro archivo en el que se va
a encontrar el propio código de unittest.


Deberemos crear un archivo con el siguiente nombre:
test_nombreArchivo.py

El nombre deberá empezar por la palabra test_


seguido del nombre del archivo sobre el que vamos a
realizar las pruebas.


De tal forma que, si nuestro
archivo se llama, por ejemplo, funcionRadio.py, el
archivo de testing se debería llamar


test_funcionRadio.py  archivo de pruebas
del archivo  funcionRadio.py



En nuestro caso el archivo a probar se va a llamar
testing01.py y el archivo de pruebas
test_testing01.py

test_testing01.py     archivo de pruebas
testing01.py          archivo de  codigo

Para ejecutarlo, pondremos en la consola:
python -m unittest test_testing01.py



Donde test_testing01.py será el nombre de mi archivo de pruebas.
Nota: Podemos ejecutar automáticamente las pruebas usando el comando:
python -m unittest discover
automatico sin poner el nombre del archivo



Con esta sintaxis no necesitamos mencionar el
nombre de archivo de la prueba. Unittest encontrará
las pruebas utilizando la convención de
nomenclatura que seguimos.
Entonces, debemos nombrar nuestros archivos de
prueba con la palabra clave test en el arranque.
Importamos unittest:
import unittest
Importamos la función sobre la cual se van a ejecutar
los test:
from testing01 import area
Y en nuestro caso tendremos que importar también
PI:
from math import pi
Lo siguiente será crear una clase que herede de la
clase TestCase:
class TestArea(unittest.TestCase):
En esta clase es donde vamos a poner nuestros test.
Vamos a crear al primero. Lo que haremos es crear
un método cuyo nombre debe empezar por la palabra
test.
Ahora, dependiendo del tipo de test que queramos
hacer, deberemos invocar un método de la clase
TestCase. Los más usados son:
assertTrue() o assertFalse() para verificar una
condición.

"""

"""
python -m unittest test_testing01.py

auto sin decir el nombre del aerchivo
python -m unittest discover
"""
import unittest
#Importamos la función sobre la cual se van a ejecutar los test: quew es area
"""
def area(r):
    areaC = pi*(r**2)
    return areaC

"""


from testing01 import area
#Y en nuestro caso tendremos que importar también PI:
from math import pi# hace falta

#Lo siguiente será crear una clase que herede de la clase TestCase:
"""En esta clase es donde vamos a poner nuestros test.
Vamos a crear al primero. 

Lo que haremos es crear
un método cuyo nombre debe empezar por la palabra
test.


Ahora, dependiendo del tipo de test que queramos
hacer, deberemos invocar un método de la clase
TestCase. 



Los más usados son:
assertTrue() 
o assertFalse() para verificar una condición.


assertRaises() para asegurar que se lanza una
excepción específica. 


Se utilizan estos métodos en
lugar de la sentencia assert para que el ejecutor de
pruebas pueda acumular todos los resultados de la
prueba de cara a realizar un informe.



Los métodos setUp() y tearDown() permiten definir
instrucciones que han de ser ejecutadas antes y
después, respectivamente, de cada método de
prueba.


assertAlmostEqual() para comprobar si el resultado
de una prueba es exactamente igual a un dato que
conocemos, por ejemplo una variable en concreto.

El quid de cada test es la llamada
a assertEqual() para verificar un resultado esperado.


Ejemplos de uso
Veamos ejemplos de uso de alguno de estos
métodos.


El primer test que vamos a crear es para saber si
nuestra función ha generado un valor que sabemos
que es correcto. 

Vamos a meter un valor conocido y
ver si el resultado corresponde a lo que sabemos que
debería dar.


Para ello debemos invocar al método assertAlmostEqual() pasando como primer
parámetro nuestra función con el parámetro de entrada 
y como segundo parámetro el resultado que sabemos que debe da
"""
class TestArea(unittest.TestCase):
    def test_area(self):
        print('-----Test valores de resultado conocido - ----')

        """
        assertAlmostEqual() para comprobar si el resultado
        de una prueba es exactamente igual a un dato que
        conocemos,
        
            Para ello debemos invocar al método assertAlmostEqual() pasando como primer
            parámetro nuestra función con el parámetro de entrada 
            y como segundo parámetro el resultado que sabemos que debe da
            """
        self.assertAlmostEqual(area(1),pi)
        self.assertAlmostEqual(area(0),0)
        self.assertAlmostEqual(area(3),pi * (3 ** 2))




"""
Recordemos que tenemos que ejecutar nuestro test
poniendo en la consola:
python -m unittest test_testing01.py



No nos indica ningún fallo, por lo que podemos decir
que las pruebas fueron positivas. Es decir, todos los
resultados reales son iguales a los esperados.
Vamos a ejecutar de nuevo, pero forzando a que se
produzca un fallo para ver la diferencia. En la línea 10
de nuestro programa hemos cambiado el valor
esperado de 0 por un 1, que sabemos que no sería
correcto
"""