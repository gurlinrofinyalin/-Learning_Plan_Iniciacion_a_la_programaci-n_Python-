"""
10. Objetos personalizados
Es posible identificar si una clase es un tipo
específico de objeto. Podemos hacer esto usando:
"""
import pandas as pd

""" objeto__name__
Cuando aplicas .__name__ a un tipo de objeto, como en type(df).__name__, lo que 
obtienes es el nombre de la clase (o tipo) del objeto como una cadena de texto.
"""


print(type(object).__name__)# type
df = pd.DataFrame()
print(type(df).__name__)#DataFrame
print(type([]).__name__)#list

"""
== (igualdad de valor): Este operador comprueba si el valor de dos objetos es el 
mismo. Es lo que casi siempre quieres usar cuando comparas cadenas, números, 
listas, etc
"""
"""
is (igualdad de identidad): Este operador comprueba si dos variables se refieren 
al mismo objeto exacto en la memoria.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(lista1 == lista2)  # True (los valores son los mismos)
print(lista1 is lista2)  # False (son dos objetos de lista diferentes en memoria, aunque contengan los mismos valores)

lista3 = lista1
print(lista1 is lista3)  # True (lista3 ahora apunta al MISMO objeto que lista1 en memoria)

"""
print(type(df).__name__ == 'DataFrame') # True (los valores son los mismos)  Boolean
print(type(df).__name__ is 'DataFrame') # True por SyntaxWarning Boolean
#SyntaxWarning: "is" with a literal. Did you mean "=="? en la línea
"""
El SyntaxWarning te está diciendo:
"Estás usando is para comparar el valor de dos cadenas. 
Aunque podría funcionar en este caso debido al internamiento de literales,
 esto no es lo que is está diseñado para hacer y es un patrón propenso a errores.
  Probablemente querías comparar sus valores, en cuyo caso deberías usar ==."

¿Por qué el SyntaxWarning con is y literales de cadena?
Cuando comparas una cadena con un literal de cadena usando is, Python puede hacer
 algo llamado "string interning" (internamiento de cadenas). Esto significa que 
 para cadenas cortas o literales repetidos, Python a veces almacena solo una 
 copia de esa cadena en memoria para optimizar el uso de recursos.

Por ejemplo, es posible que 'DataFrame' y type(df).__name__ (que también es 
'DataFrame') apunten al mismo objeto en memoria debido a este internamiento, 
lo que haría que is devolviera True en este caso.

Pero esto no está garantizado ni es un comportamiento en el que debas confiar. 
El internamiento de cadenas es una optimización de implementación de CPython 
y puede variar. No todas las cadenas, especialmente las más largas o las generadas
 dinámicamente, serán "internadas" de la misma manera.


"""

print(type(df).__name__ == type([]).__name__) # False Boolean
print(type(df).__name__ is type([]).__name__) # False Boolean

assert(type(df).__name__ == 'DataFrame') # Success Example

try:
    assert(type(df).__name__ == type([]).__name__) # Fail Example
except AssertionError:
    print("AssertionErro 2")


"""

Un DataFrame (abreviado comúnmente como df) es la estructura de datos 
principal de la librería pandas en Python. Es, en esencia, una tabla 
bidimensional, mutable en tamaño y potencialmente con datos heterogéneos.

Imagina una hoja de cálculo de Excel o una tabla en una base de datos SQL. 
Un DataFrame es muy similar a eso en concepto.

 

Bidimensional: Tiene filas y columnas, como una tabla.
Etiquetado (Labeled):

Cada columna tiene una etiqueta (un nombre), 
lo que facilita el acceso y lamanipulación de los datos por su nombre.

Cada fila también tiene una etiqueta, conocida como "índice" (o index), que 
puede ser numérico, de fecha, o cualquier otro tipo que sirva para
 identificar las filas de forma única.
 
 columna tiene nombre   fila tiene  index (numerico fecha etc unico)

Heterogéneo: Las columnas pueden contener diferentes tipos de datos (por 
ejemplo, una columna puede ser de números enteros, otra de texto, otra de
 fechas, otra de valores booleanos, etc.). 
 
 Sin embargo, dentro de una misma  columna, los datos suelen ser del mismo tipo (o al menos compatibles).
 
Mutable en tamaño: Puedes añadir o eliminar columnas y filas.

Mutable en valor: Puedes modificar los valores de las celdas.

¿Para qué se usa un DataFrame?
Los DataFrames son fundamentales en el análisis de datos y la ciencia de
 datos con Python por varias razones:

Almacenamiento de datos: Son excelentes para cargar y almacenar datos de
 diversas fuentes (CSV, Excel, bases de datos SQL, JSON, etc.).

Limpieza de datos: Permiten manejar valores faltantes, duplicados, errores
 de formato, etc.

Transformación de datos: Facilitan operaciones como filtrar, ordenar, agrupar,
 pivotar, unir (merge), etc.

Análisis exploratorio de datos (EDA): 
Proveen métodos para obtener estadísticas
descriptivas, visualizar distribuciones, identificar relaciones, etc.

Preparación de datos para modelos: Son el formato preferido para preprocesar
 datos antes de alimentarlos a algoritmos de machine learning.

Ejemplo Básico de Creación y Manipulación:
 

"""

# 1. Crear un DataFrame desde un diccionario
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [25, 30, 35, 28],
    'Ciudad': ['Nueva York', 'Londres', 'París', 'Madrid'],
    'Puntuacion': [85.5, 92.0, 78.9, 95.1]
}
#pd es la convención de alias estándar (o apodo) para la librería pandas
""" pd.DataFrame(): Llama al constructor  (la función que crea nuevas instancias) d
e la clase DataFrame de la librería pandas.
data: Le pasa a ese constructor una variable llamada data."""
df = pd.DataFrame(data)

print("DataFrame inicial:")
print(df)
# Salida:
#     Nombre  Edad      Ciudad  Puntuacion
# 0    Alice    25  Nueva York        85.5
# 1      Bob    30     Londres        92.0
# 2  Charlie    35       París        78.9
# 3    David    28      Madrid        95.1

print("\nAcceder a una columna llamada nombre:")
print(df['Nombre'])
# Salida:
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David
# Name: Nombre, dtype: object

print("\nFiltrar filas (ej. personas mayores de 30):")
# df['Edad'] es la fila
# df[  columna  >  30]       es el filtro
print(df[ df['Edad'] > 30])
# Salida:
#     Nombre  Edad Ciudad  Puntuacion
# 2  Charlie    35  París        78.9

print("\nAñadir una nueva columna:")
# df['EsMayor']  es la nueva columna
# df['Edad']  es una columna
# la condicion es True o False.   valor_columna  >=  18
df['EsMayor'] = df['Edad'] >= 18
print(df)
# Salida:
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
En resumen, un DataFrame es la estructura de datos más potente y utilizada en 
pandas para trabajar con datos tabulares, ofreciendo una gran flexibilidad y
 una amplia gama de funcionalidades para el análisis de datos.
"""



"""
2. Acceder a Filas y Columnas Específicas (por índice/etiqueta o posición):

Pandas proporciona dos "indexadores" principales para esto: .loc y .iloc.

.loc (Location-based indexing): Acceso por ETIQUETA 
                        (nombre de índice o nombre de columna).
Sintaxis: 
df.loc[fila_etiquetas, columna_etiquetas]
"""
print("Acceder a la fila con índice 0 (usando .loc):")
print(df.loc[0]) # Accede a la fila completa con el índice 0
# en este caso la primera  0    Alice    25  Nueva York        85.5     True

#original
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
Acceder a la fila con índice 0 (usando .loc):
Nombre          Alice
Edad               25
Ciudad     Nueva York
Puntuacion       85.5
Name: 0, dtype: object
------------------------------
"""
print("-" * 30)
print("Acceder a las filas con índices 1 y 3 (usando .loc):")
print(df.loc[[1, 3]]) # Se pasa una lista de índices
# filas 1 u 3 completas

#original
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
Acceder a las filas con índices 1 y 3 (usando .loc):
   Nombre  Edad   Ciudad  Puntuacion
1     Bob    30  Londres        92.0
3   David    28   Madrid        95.1
------------------------------
"""

#Acceder a una celda específica (fila por índice, columna por nombre):
print("Acceder a la columna 'Edad' de 'la fila con índice 2'' (Charlie):")
#  df.loc[ fila indice , columna nombre]
print(df.loc[2, 'Edad'])
print("-" * 30)
"""  se veria el 35, es un acceso a la CELDA
Acceder a la 'Edad' de la fila con índice 2 (Charlie):
35
"""




"""
.iloc (Integer-location based indexing): Acceso por POSICIÓN NUMÉRICA 
(índice entero).

Sintaxis: 
df.iloc[fila_posiciones, columna_posiciones]

Piensa en esto como acceder a elementos en una lista de listas por su posición
 (0-indexed).
"""

print("Acceder a la fila en la posición 0 (primera fila, usando .iloc):")
#           indice posicion
print(df.iloc[0])



#original
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
Acceder a la fila en la posición 0 (primera fila, usando .iloc):
Nombre          Alice
Edad               25
Ciudad     Nueva York
Puntuacion       85.5
Name: 0, dtype: object
------------------------------
"""

# seria lo mismo que
# df.iloc[0]
# df.loc[0]


#Acceder a múltiples filas por sus posiciones:
print("Acceder a las filas en las posiciones 1 y 3 (usando .iloc):")
print(df.iloc[[1, 3]])
#original
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
Acceder a las filas en las posiciones 1 y 3 (usando .iloc):
   Nombre  Edad   Ciudad  Puntuacion
1     Bob    30  Londres        92.0
3   David    28   Madrid        95.1
------------------------------
"""



#Acceder a una celda específica (fila por posición, columna por posición):
print("Acceder a la edad de la persona en la posición 2 (tercera persona):")
print(df.iloc[2, 1]) # Fila en posición 2, columna en posición 1 ('Edad')

# estos indices les pongo yo
#ind     0      1
# original
#     Nombre  Edad      Ciudad  Puntuacion  EsMayor
# 0    Alice    25  Nueva York        85.5     True
# 1      Bob    30     Londres        92.0     True
# 2  Charlie    35       París        78.9     True
# 3    David    28      Madrid        95.1     True
"""
Acceder a la edad de la persona en la posición 2 (tercera persona):
35
------------------------------
"""



"""
¿Cuándo usar .loc y cuándo .iloc?
Usa .loc cuando te importa la etiqueta/nombre del índice o columna. 
Es más robusto si el orden de las filas o columnas puede cambiar,
 pero sus etiquetas permanecen las mismas.

Usa .iloc cuando te importa la posición numérica (orden) de la fila o columna. 
Es útil para iteraciones o cuando trabajas con rangos numéricos.
Para acceder a las filas por "el index" como lo mencionas, .loc es la herramienta
 principal si te refieres al valor del índice,
  y .iloc si te refieres a su posición numérica dentro del DataFrame. 
  En el caso predeterminado de pandas, donde el índice son números 
  enteros (0, 1, 2...), loc 
  e iloc para acceder a una sola fila por ese número coincidirán. 
  Sin embargo, si cambias el índice, la diferencia entre loc e iloc se vuelve 
  crucial.


"""