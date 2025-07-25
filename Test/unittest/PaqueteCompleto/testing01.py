from math import pi

def area(r):
    #Verificamos los tipos correctos
    # si no es entero o decimal coma flotante
    # lanzamos la excepcion
    if type(r) not in [float, int]:
        raise TypeError("Solo números enteros o de coma flotante.")
    # si es negativo lanzamos la excepcion
    if r<0:
        raise ValueError("No se permiten valores negativos")
    # sino hacemos la operacion
    areaC = pi * (r**2)
    return areaC