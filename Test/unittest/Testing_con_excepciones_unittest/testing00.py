from math import pi

def area(r):
    if r<0:
        #raise ValueError("No se permiten valores negativos")
        print("No se permiten valores negativos")
    areaC = pi*(r**2)
    return areaC

"""
 Testing con excepciones
Uno de los problemas que tenemos con funciones
que reciben valores numéricos es que los valores
introducidos no se encuentran en el rango adecuado.
Por ejemplo, en nuestra función el rango de valores
negativos no es factible.
Si ya sabemos que nuestra función no va a sacar
valores coherentes si los parámetros de entrada son
negativos, lo que tenemos que hacer es crear una
excepción que de lance en dichos casos.
En unittest no solo tenemos que comprobar que la
función nos devuelva los resultados correctos,
también tenemos que asegurarnos de que se
disparan las excepciones correctamente según los
casos.
Ejemplo:
En nuestro archivo testing01.py modificamos la
función a comprobar añadiéndole una excepción:
 
 """