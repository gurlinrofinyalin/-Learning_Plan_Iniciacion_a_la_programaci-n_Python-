def descomposicion_factores_primos(numero):
    """
    Realiza la descomposición en factores primos de un número.

    Args:
        numero (int): El número entero a descomponer.

    Returns:
        list: Una lista con los factores primos del número.
              Devuelve una lista vacía si el número es menor o igual a 1.

    """
    factores = []

    if numero <= 1:
        return factores # devuelve listy vacia si el numero es menor de 1

    # Dividir por 2 hasta que el número sea impar
    while numero % 2 == 0:
        factores.append(2) # se añade un 2 si se puede dividir
        numero //= 2 # actualizamos numero ya dividido

# despues de  division por 2, luego van los impares,  3 5 ...
    # Dividir por números impares a partir de 3
    # Solo necesitamos verificar hasta la raíz cuadrada del número
    '''

    La condición del bucle while i * i <= numero: 
     Si un número tiene un factor primo mayor que su raíz cuadrada, 
    entonces debe tener también un factor primo menor que su raíz cuadrada.
     Por lo tanto, solo necesitamos verificar los divisores hasta la raíz 
     cuadrada del número.'''


    i = 3
    while i * i <= numero:
        while numero % i == 0:  # sale cuando no es divisible por 3
            factores.append(i)
            numero //= i
        i += 2  # Saltar al siguiente número impar
                # suma 2 al 3 ejemplo

   # se suma el numero si  sigue siendo mayor que 1
    # Si después de las divisiones el número restante es mayor que 1,
    # significa que es un factor primo
    if numero > 1:
        factores.append(numero)

    return factores

# Ejemplos de uso:
print(f"Factores primos de 12: {descomposicion_factores_primos(12)}")
print(f"Factores primos de 1: {descomposicion_factores_primos(1)}")
print(f"Factores primos de 0: {descomposicion_factores_primos(0)}")
print(f"Factores primos de 7: {descomposicion_factores_primos(7)}")
print(f"Factores primos de 100: {descomposicion_factores_primos(100)}")
print(f"Factores primos de 210: {descomposicion_factores_primos(210)}")

