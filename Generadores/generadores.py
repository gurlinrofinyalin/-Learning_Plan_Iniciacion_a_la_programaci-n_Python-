"""

Un generador en Python es una forma especial de función o un tipo de
iterable que te permite crear iteradores de una manera más sencilla y eficiente en
 cuanto a memoria.

La clave para entender los generadores es que no construyen toda la secuencia de
 elementos en memoria de una vez, sino que producen un elemento a la vez y "pausan"
 su ejecución hasta que se solicita el siguiente elemento. Esto se conoce como
  evaluación perezosa (lazy evaluation) o producción bajo demanda.

¿Cómo se crea un generador?
La principal característica que convierte una función normal en una función
generadora es el uso de la palabra clave yield en lugar de return.

Ejemplo básico:

Python
"""
def mi_primer_generador():
    print("Primer elemento")
    yield 1
    print("Segundo elemento")
    yield 2
    print("Tercer elemento")
    yield 3

# Llamamos a la función generadora, pero NO ejecuta el código todavía.
# En su lugar, devuelve un OBJETO GENERADOR.
gen = mi_primer_generador()
print(f"Tipo de objeto: {type(gen)}") # Salida: <class 'generator'>

# Para obtener los valores, debemos iterar o usar next()
print("\nIterando con next():")
print(next(gen)) # Imprime "Primer elemento", luego devuelve 1
print(next(gen)) # Imprime "Segundo elemento", luego devuelve 2
print(next(gen)) # Imprime "Tercer elemento", luego devuelve 3

try:
    print(next(gen)) # Intentar obtener otro elemento lanzará StopIteration
except StopIteration:
    print("Fin del generador: StopIteration")

print("\nIterando con un bucle for (más común):")
for numero in mi_primer_generador():
        # Se crea un nuevo objeto generador cada vez que se llama
    print(numero)

"""
Salida del ejemplo:

Tipo de objeto: <class 'generator'>

Iterando con next():
Primer elemento
1
Segundo elemento
2
Tercer elemento
3
Fin del generador: StopIteration

Iterando con un bucle for (más común):
Primer elemento
1
Segundo elemento
2
Tercer elemento
3
Características clave de los generadores:
Palabra clave yield:

Cuando Python encuentra yield en una función, la función se convierte automáticamente
 en una función generadora.
IMPORTANTE
yield hace que la función "entregue" (yield) un valor al llamador, pero a diferencia 
de return, no termina la función. 
IMPORTANTE
La función queda en un estado "pausado", recordando
 dónde se detuvo y todas sus variables locales.
IMPORTANTE
Cuando se solicita el siguiente valor, la ejecución de la función se reanuda desde
 donde se quedó, hasta que encuentra el siguiente yield o la función termina.

Evaluación Perezosa (Lazy Evaluation):

Los generadores solo calculan el siguiente valor cuando se les pide. Esto contrasta 
con las listas, tuplas u otras colecciones, que construyen todos sus elementos en
 memoria de una vez.

Beneficio: Esto es crucial para trabajar con secuencias muy grandes o infinitas, 
ya que no consumes grandes cantidades de memoria.

Memoria eficiente:

Al producir valores uno a uno, los generadores son muy eficientes en el uso de memoria. Solo guardan el estado interno necesario para reanudar su ejecución, no toda la secuencia de valores.

Son iteradores:

Un objeto generador es su propio iterador. Esto significa que puedes usarlo
 directamente en un bucle for, que es la forma más común de consumir sus valores.

Solo una pasada:
IMPORTANTE
Una vez que un generador ha agotado todos sus valores (es decir, la función generadora
 ha terminado de ejecutarse y no hay más yields), no puedes volver a usarlo para 
 generar los valores desde el principio. Tendrías que crear una nueva instancia del
  generador llamando de nuevo a la función generadora.

¿Cuándo usar generadores?
Para secuencias grandes o infinitas: Cuando necesitas procesar una gran cantidad de 
datos que no caben en memoria, o cuando necesitas generar una secuencia que 
teóricamente es infinita (como números Fibonacci).

Eficiencia de memoria: Cuando la memoria es una preocupación importante.

Pipeline de datos: Cuando encadenas operaciones donde cada paso produce datos para el
 siguiente.

Cuando el cómputo de cada elemento es costoso: Si calcular un elemento lleva tiempo,
 un generador te permite obtenerlo y trabajar con él mientras el siguiente se calcula en segundo plano (o cuando sea necesario).

Expresiones generadoras (Generator Expressions)
Similar a las compresiones de lista, puedes crear un generador de una sola línea
 usando una "expresión generadora", que tiene una sintaxis similar pero usa paréntesis () en lugar de corchetes []:

"""

# Compresión de lista (crea una lista completa en memoria)
# es una lista  porque usamos []
lista_cuadrados = [x*x for x in range(1000000)] # Consumirá mucha memoria
print(type(lista_cuadrados)) #  <class 'list'>

# es un generador porque usamos ()
# Expresión generadora (crea un generador, valores producidos bajo demanda)
generador_cuadrados = (x*x for x in range(1000000)) # Muy eficiente en memoria

print(type(generador_cuadrados)) #  <class 'generator'>

# Puedes iterar sobre él
for cuadrado in generador_cuadrados:
    print(f"{cuadrado} {type(cuadrado)}")
    # print(cuadrado) # Se imprimen los cuadrados uno a uno
    if cuadrado > 100:
        break # Puedes parar cuando quieras sin haber calculado todos


"""
En resumen, los generadores son una herramienta poderosa en Python para escribir
 código más eficiente en memoria y más legible cuando trabajas con colecciones de 
 datos que no necesitan ser cargadas completamente en memoria a la vez.
"""