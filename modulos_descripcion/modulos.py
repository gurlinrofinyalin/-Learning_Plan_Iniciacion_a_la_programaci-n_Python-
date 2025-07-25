# modulos.py
# Es buena práctica poner los imports al principio, como estamos haciendo.
import palabras# Importamos el módulo 'palabras' completo
import numeros as nums# Importamos el módulo 'numeros' y lo renombramos como 'nums'



print(f"Desde modulos.py: __name__ es '{__name__}'")# salen los 3 de abajo
# Desde palabras.py: __name__ es 'palabras'
#Desde numeros.py: __name__ es 'numeros'
#Desde modulos.py: __name__ es '__main__'

"""
Cuando ejecutas un archivo Python directamente desde tu terminal (por ejemplo, python modulo.py), 
Python asigna automáticamente el valor '__main__' a la variable global __name__ dentro de ese archivo.
Piensa en __main__ como una etiqueta especial que Python usa para identificar el punto de entrada 
principal de tu programa. 
Es la forma en que Python dice: "Este es el script que el usuario ha solicitado ejecutar en este momento".
"""

print("-" * 30)

# --- Accediendo a los elementos de los módulos importados con '.' ---
print("Accediendo a elementos de 'palabras':")# Accediendo a elementos de 'palabras':
print(f"palabras.hola: {palabras.hola}")# palabras.hola: hello
print(f"palabras.mundo: {palabras.mundo}")# palabras.mundo: world
print(f"palabras.saludar(): {palabras.saludar()}") # Accediendo a una función  #palabras.saludar(): hello, world!

print("\nAccediendo a elementos de 'numeros' (como 'nums'):")
print(f"nums.num: {nums.num}")
print(f"nums.num2: {nums.num2}")
print(f"nums.sumar_numeros(): {nums.sumar_numeros()}") # Accediendo a una función

print("-" * 30)


print("Importando objetos específicos:")
from palabras import hola as saludo_especial#Importando del modulo o archivo palabras solo algunos objetos como variable hola  (con renombrar)
from numeros import num, PI_APROX#Importando solo varios objetos de un módulo  llamado numeros (sin renombrarlos)

print(f"saludo_especial (renombrado de palabras.hola): {saludo_especial}")# accedemos a la variable hola renombrada del modulo palabras
print(f"num (de numeros): {num}")# nums.num: 3 # accedemos  a la variable num del modulos numeros
print(f"PI_APROX (de numeros): {PI_APROX}")#nums.num2: 7 # accedemos a la  constante PI_APROX

print("-" * 30)

# --- Explorando el contenido de un módulo con dir() ---
print("Contenido del módulo 'palabras' (usando dir(palabras)):")
print(dir(palabras))
"""
Contenido del módulo 'palabras' (usando dir(palabras)):
['PEDRO', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hola', 'mundo', 'saludar']
"""

print("\nContenido del módulo 'numeros' (usando dir(nums)):")
print(dir(nums))
"""
Contenido del módulo 'numeros' (usando dir(nums)):
['PEDRO', 'PI_APROX', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'num', 'num2', 'sumar_numeros']
"""

print("\nContenido del espacio de nombres global de 'modulos.py' (usando dir()):")
# dir() sin argumentos muestra los nombres en el espacio de nombres actual
print(dir())
"""
Contenido del espacio de nombres global de 'modulos.py' (usando dir()):
['PI_APROX', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'num', 'nums', 'palabras', 'saludo_especial']
"""

print("-" * 30)

# --- Acceso al valor de __name__ en el módulo principal ---
print(f"El valor de __name__ en el script principal 'modulos.py' es: '{__name__}'")
#El valor de __name__ en el script principal 'modulos.py' es: '__main__'

# Path desde el directorio actual (src) a los módulos:
# Si ejecutas 'modulos.py' desde el directorio 'src',
# Python buscará 'palabras.py' y 'numeros.py' en el mismo directorio.
# No hay un "path desde src" que necesites especificar dentro del código
# para importar módulos que están en el mismo nivel o en el PYTHONPATH.
# El path real de los archivos sería:
# - tu_proyecto/src/palabras.py
# - tu_proyecto/src/numeros.py
# - tu_proyecto/src/modulos.py
# siendo proyectos la carpte principal osease src
print(f"Path del archivo 'palabras.py': {palabras.__file__}")
#Path del archivo 'palabras.py': /home/death/Documents/pythonIBM/proyectos/modulos_descripcion/palabras.py
print(f"Path del archivo 'numeros.py': {nums.__file__}")
#Path del archivo 'numeros.py': /home/death/Documents/pythonIBM/proyectos/modulos_descripcion/numeros.py




from palabras import PEDRO #as pedro_de_palabras # se puede renombrar como pedro_de_palabras
from numeros import PEDRO as pedro_de_numeros

print(f"La variable PEDRO de 'palabras' (usando alias) es: {PEDRO}")  # usamos directa
print(f"La variable PEDRO de 'numeros' (usando alias) es: {pedro_de_numeros}") # usamos renombrada



