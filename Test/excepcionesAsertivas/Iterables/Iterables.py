"""
¿Qué es un Iterable en Python?
En Python, un iterable es un objeto del que puedes obtener elementos uno por uno.
 Piensa en ello como algo por lo que puedes "pasar" o "recorrer" para acceder a sus partes.


Los iterables son fundamentales porque son la base de los bucles for.
Cuando escribes for elemento in mi_objeto:, ese mi_objeto tiene que ser un iterable.

Para ser un iterable, un objeto debe implementar el método __iter__,
que devuelve un iterador.

Un iterador es lo que realmente lleva la cuenta de dónde va en la secuencia
y sabe cómo obtener el "siguiente" elemento.



collections.abc.Iterable y isinstance()
collections.abc.Iterable:
Esto es una clase base abstracta (ABC) que se encuentra en el módulo collections.abc.
No es un tipo de dato que crees directamente, sino una "plantilla" que define el
comportamiento que un objeto debe tener para ser considerado un iterable.
Si un objeto implementa el método __iter__, Python lo considera compatible con Iterable.

isinstance(objeto, tipo):
Esta función incorporada de Python se utiliza para verificar si un objeto es una instancia
 de una clase o de un tipo particular (o de una subclase de ese tipo).

Al usar isinstance(mi_variable, Iterable), estamos preguntando:
"¿La mi_variable se comporta como algo que se puede recorrer?
Es decir, ¿implementa el protocolo de iteración (tiene el método __iter__)?"

Explicación del Código Ejemplo
El código demuestra el concepto de iterable con diferentes tipos de datos:

Ejemplo 1: Lista (mi_lista = [3, 6, 4, 2, 1])
isinstance(mi_lista, Iterable) devuelve True.

Explicación: Las listas son uno de los iterables más comunes en Python.
Puedes recorrer una lista con un bucle for para acceder a cada uno de sus elementos.

Ejemplo 2: Número Entero (mi_entero = 5)
isinstance(mi_entero, Iterable) devuelve False.

Explicación: Un solo número entero no puede ser "recorrido".
No tiene "partes" individuales a las que acceder de forma secuencial.
Intentar un for numero in 5: causaría un error.
Por eso, la aserción falla intencionadamente, demostrando que no es un iterable.

Ejemplo 3: Cadena de Texto (mi_cadena = "Hola")
isinstance(mi_cadena, Iterable) devuelve True.

Explicación: Las cadenas de texto son iterables porque puedes recorrerlas carácter
por carácter. Por ejemplo, for letra in "Hola": imprimiría 'H', luego 'o', 'l', 'a'.

Ejemplo 4: Objeto Personalizado (MiClasePersonalizada)
isinstance(mi_objeto, Iterable) devuelve False.

Explicación: Cuando creas tu propia clase (MiClasePersonalizada), por defecto,
sus objetos no son iterables. Para que lo sean, tendrías que definir el método
especial __iter__ dentro de tu clase.
Este método es el que le dice a Python cómo "recorrer" tu objeto.
El ejemplo falla la aserción a propósito para ilustrar esto.

En resumen, el código utiliza isinstance(variable, Iterable) para mostrar de manera
práctica qué tipos de datos en Python se pueden recorrer (son iterables) y cuáles no,
destacando la importancia del protocolo __iter__ para definir un iterable.


"""



from collections.abc import Iterable

print("--- Verificando si una variable es Iterable ---")

# Ejemplo 1: Una lista es un iterable
mi_lista = [3, 6, 4, 2, 1]
es_lista_iterable = isinstance(mi_lista, Iterable)
print(f"¿'{mi_lista}' es un iterable? {es_lista_iterable}")
# Esta aserción pasará sin problemas porque una lista SÍ es iterable
assert es_lista_iterable, "Error de aserción: La lista debería ser iterable."

print("-" * 40) # Línea divisoria para mejor lectura

# Ejemplo 2: Un número entero NO es un iterable
mi_entero = 5
es_entero_iterable = isinstance(mi_entero, Iterable)
print(f"¿'{mi_entero}' es un iterable? {es_entero_iterable}")

# Esta aserción FALLARÁ intencionadamente porque un número entero no es iterable.
# Usamos un bloque try-except para capturar el error y demostrarlo sin detener el programa.
try:
    assert es_entero_iterable, "Error de aserción: El entero NO debería ser iterable."
except AssertionError as e:
    print(f"¡Atención! Se capturó el error esperado: {e}")
    print("Esto confirma que un número entero NO es un iterable.")

print("-" * 40)

# Ejemplo 3: Una cadena de texto (string) es un iterable
mi_cadena = "Hola"
es_cadena_iterable = isinstance(mi_cadena, Iterable)
print(f"¿'{mi_cadena}' es un iterable? {es_cadena_iterable}")
# Esta aserción pasará sin problemas porque una cadena SÍ es iterable
assert es_cadena_iterable, "Error de aserción: La cadena debería ser iterable."

print("-" * 40)

# Ejemplo 4: Un objeto personalizado (sin definir iteración) NO es iterable por defecto
class MiClasePersonalizada:
    def __init__(self, valor):
        self.valor = valor

mi_objeto = MiClasePersonalizada(10)
es_objeto_iterable = isinstance(mi_objeto, Iterable)
print(f"¿'{mi_objeto}' es un iterable? {es_objeto_iterable}")
# Esta aserción FALLARÁ intencionadamente porque nuestro objeto personalizado no es iterable por defecto.
try:
    assert es_objeto_iterable, "Error de aserción: El objeto personalizado NO debería ser iterable por defecto."
except AssertionError as e:
    print(f"¡Atención! Se capturó el error esperado: {e}")
    print("Esto confirma que nuestras propias clases no son iterables a menos que implementemos el método __iter__.")

print("\n--- Fin de los ejemplos de verificación de Iterables ---")

# Clase 
class Contador:
    """
    Una clase personalizada que es iterable y cuenta desde un inicio
    hasta un final (exclusivo).
    """
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        """
        Este método hace que la clase sea un iterable.
        Debe devolver un objeto iterador.
        En este caso, la propia instancia de Contador actúa como iterador
        porque también implementa __next__.
        """
        self.valor_actual = self.inicio  # Reinicia el contador para cada nueva iteración
        return self

    def __next__(self):
        """
        Este método es parte del protocolo del iterador.
        Devuelve el siguiente elemento en la secuencia.
        """
        if self.valor_actual < self.fin:
            valor_a_devolver = self.valor_actual
            self.valor_actual += 1
            return valor_a_devolver
        else:
            # Cuando no hay más elementos, se debe lanzar StopIteration
            raise StopIteration

# --- Creando una instancia de la clase iterable ---
mi_contador = Contador(1, 5) # Contará desde 1 hasta 4

print("--- Iterando sobre la instancia de Contador ---")
for numero in mi_contador:
    print(numero) # Debería imprimir 1, 2, 3, 4

print("---")

# --- Verificando si la instancia es iterable con una aserción ---
es_iterable = isinstance(mi_contador, Iterable)
print(f"¿La instancia 'mi_contador' ({mi_contador.inicio} a {mi_contador.fin}) es un iterable? {es_iterable}")

# Esta aserción pasará sin problemas porque hemos implementado __iter__ y __next__
assert es_iterable, "Error de aserción: La clase Contador debería ser iterable."

print("\n¡La aserción pasó! Esto confirma que nuestra clase 'Contador' es efectivamente iterable.")

print("\n--- Intentando iterar de nuevo (debería funcionar porque __iter__ se reinicia) ---")
for numero in mi_contador:
    print(numero) # Debería imprimir 1, 2, 3, 4 de nuevo



"""
Explicación del Código
from collections.abc import Iterable: Importamos Iterable para poder usarlo con
 isinstance() y verificar si nuestra clase cumple con el protocolo de iterable.

class Contador:: Definimos nuestra clase.

__init__(self, inicio, fin): El constructor inicializa nuestra instancia con un valor 
de inicio y un valor de fin para nuestra secuencia de conteo.

__iter__(self): ¡Este es el método clave que hace que Contador sea un iterable!

Cada vez que se llama a iter(mi_contador) (lo que ocurre automáticamente cuando inicias 
un bucle for o una función como list()), este método se ejecuta.

Establecemos self.valor_actual = self.inicio para asegurarnos de que el contador siempre
 comience desde el principio cuando se itera sobre él.

Devuelve self: En este ejemplo, la propia instancia de Contador actúa también como el 
iterador. Esto es posible porque Contador también implementa el método __next__. 
Esto es un patrón común y conciso, pero también podrías definir una clase iteradora 
separada.

__next__(self): Este es el método que hace que la instancia sea un iterador.
 Es llamado repetidamente por el bucle for (o la función next()).

Comprueba si self.valor_actual es menor que self.fin.

Si lo es, guarda el valor_actual, lo incrementa (self.valor_actual += 1), y devuelve
 el valor guardado.

Si self.valor_actual ya no es menor que self.fin (es decir, ya no quedan elementos),
 lanza la excepción StopIteration. Esta es la señal que el bucle for usa para saber
  que ya no hay más elementos y debe terminar.

Instancia y Uso:

mi_contador = Contador(1, 5): Creamos una instancia de nuestra clase que contará del 1 al 4.

for numero in mi_contador:: Aquí demostramos que podemos iterar directamente sobre 
    mi_contador. Los métodos __iter__ y __next__ son llamados automáticamente por el 
    bucle for.

Aserción:

es_iterable = isinstance(mi_contador, Iterable): Usamos isinstance para verificar
 programáticamente que mi_contador se reconoce como un iterable por Python.

assert es_iterable, ...: La aserción confirmará que es_iterable es True, validando 
que nuestra clase fue diseñada correctamente para ser iterable.

Este ejemplo te muestra cómo implementar el protocolo de iteración en Python para
 crear tus propias clases que puedan ser recorridas con un bucle for, de manera
  similar a como lo harías con listas o cadenas.

"""
