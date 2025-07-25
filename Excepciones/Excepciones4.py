
# ejemplos de
#Un IndexError ocurre cuando intentas acceder a un índice que está fuera
# del rango válido de una secuencia (como una lista, tupla o cadena).

### Ejemplo 1: Manejando un índice fuera de rango en una lista

# Intenta acceder a un índice que no existe en una lista
mi_lista = [10, 20, 30]
indice_a_acceder = 4

print(f"Lista original: {mi_lista}")
print(f"Intentando acceder al índice: {indice_a_acceder}")

try:
    valor = mi_lista[indice_a_acceder]
    print(f"Valor en el índice {indice_a_acceder}: {valor}")
except IndexError:
    # Este bloque se ejecuta si ocurre un IndexError
    print(f"ERROR: El índice {indice_a_acceder} está fuera de rango para la lista.")
    print(f"La lista solo tiene {len(mi_lista)} elementos (índices del 0 al {len(mi_lista) - 1}).")

print("\nEl programa continúa después del manejo de errores.")

### Ejemplo 2: Manejando un índice negativo fuera de rango en una cadena

# Intenta acceder a un carácter en una posición muy negativa, que no
# existe.
mi_cadena = "Hola"
indice_a_acceder = -6 # Índice negativo demasiado lejano

print(f"Cadena original: '{mi_cadena}'")
print(f"Intentando acceder al índice: {indice_a_acceder}")

try:
    caracter = mi_cadena[indice_a_acceder]
    print(f"Carácter en el índice {indice_a_acceder}: {caracter}")
except IndexError:
    # Este bloque se ejecuta si ocurre un IndexError
    print(f"ERROR: El índice {indice_a_acceder} está fuera de rango para la cadena.")
    print(f"La cadena '{mi_cadena}' tiene una longitud de {len(mi_cadena)}.")

print("\nEl programa continúa después del manejo de errores.")

### Ejemplo 3: Acceder a un índice en una tupla vacía

# Una tupla vacía no tiene ningún índice válido.
tupla_vacia = ()
indice_a_acceder = 0

print(f"Tupla original: {tupla_vacia}")
print(f"Intentando acceder al índice: {indice_a_acceder}")

try:
    elemento = tupla_vacia[indice_a_acceder]
    print(f"Elemento en el índice {indice_a_acceder}: {elemento}")
except IndexError:
    # Este bloque se ejecuta si ocurre un IndexError
    print(f"ERROR: No se puede acceder al índice {indice_a_acceder} en una tupla vacía.")

print("\nEl programa continúa después del manejo de errores.")


# ejemplos de
#Un TypeError ocurre cuando intentas realizar una operación o función en
# un objeto de un tipo inadecuado. Es como intentar usar un martillo para
# atornillar un tornillo; el tipo de herramienta no es el adecuado para
# la operación


#Un `TypeError` ocurre cuando se intenta realizar una operación o
# función en un objeto de un tipo inadecuado.

### Ejemplo 1: Manejando tipos incompatibles en una operación
# Intentando concatenar una cadena de texto con un número entero.
nombre = "Carlos"
edad = 30

print(f"Nombre: '{nombre}', Edad: {edad}")
print("Intentando concatenar nombre + edad...")

try:
    combinado = nombre + edad
    print(f"Resultado combinado: {combinado}")
except TypeError:
    # Este bloque se ejecuta si ocurre un TypeError
    print("ERROR: No se puede concatenar directamente una cadena y un número entero.")
    print("Podrías necesitar convertir el número a cadena primero (por ejemplo, str(edad)).")

print("\nEl programa continúa después del manejo de errores.")

### Ejemplo 2: Manejando un intento de llamar a un objeto no-callable


# Una variable que contiene un número entero no puede ser "ejecutada"
# como una función.
mi_numero = 100

print(f"Mi número: {mi_numero}")
print("Intentando llamar a mi_numero()...")

try:
    mi_numero() # Esto lanzará un TypeError
    print("Se llamó al número con éxito.")
except TypeError:
    # Este bloque se ejecuta si ocurre un TypeError
    print("ERROR: Un objeto de tipo entero no puede ser llamado como una función.")
    print("Asegúrate de que intentas llamar a una función o un objeto invocable.")

print("\nEl programa continúa después del manejo de errores.")

### Ejemplo 3: Manejando una llamada a método inválida para un tipo de objeto


# El método .append() es para listas, no para cadenas.
texto = "aprendiendo Python"

print(f"Texto original: '{texto}'")
print("Intentando usar texto.append(' es divertido!') en la cadena...")

try:
    texto.append(" es divertido!") # .append() es un método de lista, no de cadena
    print(f"Texto modificado: {texto}")
except TypeError:
    # Este bloque se ejecuta si ocurre un TypeError
    print("ERROR: Las cadenas (strings) no tienen un método '.append()'.")
    print("Quizás quisiste usar la concatenación de cadenas '+' o trabajar con una lista.")

print("\nEl programa continúa después del manejo de errores.")

#Estos ejemplos demuestran cómo los bloques `try-except` permiten que
# tu programa maneje situaciones inesperadas de manera **elegante**,
# proporcionando mensajes informativos en lugar de detenerse abruptamente.
# Esto es crucial para crear aplicaciones robustas y fáciles de usar.