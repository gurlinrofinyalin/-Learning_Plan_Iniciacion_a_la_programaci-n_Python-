"""
Explicación detallada de wrapper.llamadas
wrapper es una función (la función interna del decorador)

.llamadas es un atributo dinámico que le agregamos a esa función

Se crea exactamente como dices:

Primero el nombre de la función (wrapper)

Luego el nombre del atributo (llamadas)


¿Qué es wrapper.llamadas?
Es un atributo dinámico que se agrega a la función wrapper.

Funciona como contador: Almacena cuántas veces se ha llamado a la función decorada.

Persiste entre llamadas: A diferencia de variables locales, no se reinicia.


¿Por qué usar wrapper.llamadas y no una variable normal?
Variable Normal (local)	wrapper.llamadas (atributo)
Se reinicia en cada llamada	Persiste entre llamadas
Solo accesible dentro de wrapper	Accesible desde fuera (ej: saludar.llamadas)



def decorador_contador(func):          # Paso 1: Recibe la función a decorar func
    def wrapper(*args, **kwargs):      # Paso 2: Define la función wrapper
        wrapper.llamadas += 1          # Paso 3: Accede/modifica el atributo
        print(f"Llamada #{wrapper.llamadas}")
        return func(*args, **kwargs)

    wrapper.llamadas = 0               # Paso 4: Crea el atributo inicialmente
    return wrapper                     # Paso 5: Retorna la función modificada

"""


def decorador_contador(func):
    def wrapper(*args, **kwargs):
        #print(args) # lista
        #print(kwargs)# diccionario
        wrapper.llamadas += 1 # ← Esto es un contador
        print(f"Llamada #{wrapper.llamadas} a {func.__name__}")
        return func(*args, **kwargs)
    wrapper.llamadas = 0  # ← Contador de llamadas# ← Inicializa el contador
    return wrapper # retorna la funcion  modificada

@decorador_contador
def saludar():
    print("¡Hola!")

saludar()
saludar()
"""
Llamada #1 a saludar
¡Hola!
Llamada #2 a saludar
¡Hola!
"""
print(saludar.llamadas)  # Output: 2


"""
Un decorador es una función especial que modifica o extiende el comportamiento de otra función o método sin cambiar su código original. Es una herramienta poderosa para añadir funcionalidad de manera limpia y reutilizable.
"""