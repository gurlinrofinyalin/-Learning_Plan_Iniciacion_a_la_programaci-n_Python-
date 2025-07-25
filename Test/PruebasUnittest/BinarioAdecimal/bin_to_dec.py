"""
Introducción
En este módulo veremos tres casos de uso de testeo de scripts con Unittest.


Ejemplo 1. Binario a decimal
Convierte cadenas binarias a sus equivalentes decimales.

Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1



Archivo bin_to_dec.py:

"""
#binary_str Se espera que sea una cadena de texto que represente un número binario (ej. "1011").
# osease una expresion binaria sin el 0b
def decimal(binary_str):
    print("ENTRAMOS EN decimal(binary_str)")
    """ Convierte cadenas binarias a sus equivalentes decimales.
    Lanzar ValueError si binary_str contiene caracteres distintos de 0 y 1"""

    remove_0_and_1 = binary_str.replace('0', '').replace('1', '')
    #Crea una nueva cadena eliminando todos los '0' y '1' de 'binary_str'.
    # # Si la cadena original solo contiene '0's y '1's, 'remove_0_and_1' quedará vacía.
    # si la cadena no esta vacia lanza una excepcion
    # asi comprobamos que binary_str es una expresion binaria sin 0b
    if len(remove_0_and_1) > 0:
        raise ValueError('La cadena binaria de entrada solo puede contener 0 y 1')

    # asignacion de valor  posicion
    place = 1; # Posición
    # Esta variable representa el valor posicional de cada dígito binario
    # (1, 2, 4, 8, 16, 32 , 64 , 128 etc.).

    dec = 0 # El valor decimal
    # Aquí se acumulará el resultado de la conversión a decimal.

    print(f"binary_str: {binary_str}")
    print(f"posicion : {place}")
    print(f"valor decimal : {dec}")
    # binary_str[::-1] Bucle desde el final de la cadena hasta el principio
    # osease crea una versión invertida de la cadena.
    for bit in binary_str[::-1]:
        # En cada iteración, 'bit' será un dígito binario ('0' o '1'),
        #     empezando por el dígito de más a la derecha.

        # si tenemos un 1 en la expresion binaria
        # debemos sumar el valor de la posicion
        # ejemplo  si tenemos 100
        # posciones 128 64 32 16 8 4 2 1
        # 1 o 0                    1 0 0
        # decimal                         4
        if (bit == '1'): # Si el dígito es un 1, agregue el valor posicional.
                         #  si tenemos un 1 en esa poscicion, debemos sumar lo que vale la posicion
                         # en este caso la posicion seria place
                         # y el digito dec
                         # Si es 0, ignorar.  Si no tenemos valor no sumamos la posicion
            dec += place# aqui sumamos la posicion si en dec tenemos un 1, sino nada

        # Multiplique la posición por 2 para el siguiente valor de posición
        # Multiplica 'place' por 2. Esto prepara 'place' para el siguiente dígito binario
        # (el de su izquierda), que tiene el doble de valor posicional.
        # posciones 128 64 32 16 8 4 2 1
        place *= 2 # vamos cambiando la posicion de derecha a izquierda


        print(f"siguiente posicion : {place}")
        print(f"devuelve valor decimal : {dec}")
    print("SALIMOS DE decimal(binary_str)")
    return dec