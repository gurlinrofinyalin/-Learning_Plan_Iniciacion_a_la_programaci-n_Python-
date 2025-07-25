'''En Python, los argumentos mutables se refieren a pasar objetos
que pueden ser modificados (mutados) dentro de una función, como listas,
diccionarios o conjuntos. Esto puede tener efectos secundarios inesperados
si no se maneja con cuidado.

¿Qué son los argumentos mutables?
Son parámetros de función que reciben objetos cuyo estado interno puede cambiar
(mutar).

Los tipos mutables comunes en Python incluyen:
Listas (list): [1, 2, 3]
Diccionarios (dict): {"a": 1}
Conjuntos (set): {1, 2, 3}
Objetos personalizados (si sus atributos son modificables).



Ejemplo clave: Lista como argumento mutable
'''
def agregar_elemento(lista, elemento):
    lista.append(elemento)  # Modifica la lista original

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista, 4)
print(mi_lista)  # Salida: [1, 2, 3, 4] (¡La lista original cambió!)
'''
¿Por qué es importante entenderlo?
Efectos secundarios:
Si modificas un argumento mutable dentro de una función,
el cambio afectará al objeto original fuera de la función.
'''


def borrar_ultimo(lista):
    lista.pop()  # Elimina el último elemento de la lista original

datos = [10, 20, 30]
borrar_ultimo(datos)
print(datos)  # Salida: [10, 20] (¡Se modificó!)


'''
Valores por defecto mutables:
Un error común es usar listas o diccionarios como valores por defecto en parámetros.
'''
# MAL Solución: Usar None y crear una nueva lista dentro de la función.
def funcion_peligrosa(lista=[]):  # ¡Mismo objeto en cada llamada!
    lista.append(1)
    return lista

print(funcion_peligrosa())  # [1]
print(funcion_peligrosa())  # [1, 1] (¡Acumula valores!)

#BIEN Solución: Usar None y crear una nueva lista dentro de la función.
def funcion_segura(lista=None):
    if lista is None:
        lista = []
    lista.append(1)
    return lista

'''
Cómo evitar problemas con argumentos mutables
Copiar el argumento mutable si no quieres modificar el original:
'''
def procesar_lista(lista):
    lista = lista.copy()  # Crea una copia
    lista.append(100)
    return lista

original = [1, 2, 3]
nueva = procesar_lista(original)
print(original)  # [1, 2, 3] (original no cambió)
print(nueva)     # [1, 2, 3, 100]  (la nueva lista devuelta)

'''
Documentar el comportamiento:
Si la función modifica el argumento, debes indicarlo en el docstring.
'''
def modificar_lista(lista):
    """Esta función modifica la lista pasada como argumento."""
    lista.append("modificado")

'''    
Usar tuplas para datos inmutables si no se requiere modificación:
'''
def procesar_datos(datos):
    datos = tuple(datos)  # Convierte lista a tupla (inmutable)
    # datos.append(1)  # ¡Error! Las tuplas no permiten append.

    '''
Diferencia entre mutable vs. inmutable
Tipo	    Ejemplo	        ¿Mutable?
Lista	    [1, 2, 3]	    Sí
Diccionario	{"a": 1}	    Sí
Conjunto	{1, 2, 3}	    Sí
Tupla	    (1, 2, 3)	    No
Entero	    5	            No
Cadena	    "hola"	        No
'''


'''
Los argumentos mutables pueden ser modificados dentro de una función, 
afectando al objeto original.

Usa copias (copy(), list(), dict()) si necesitas evitar efectos secundarios.

Evita valores por defecto mutables (usa None en su lugar).
'''